//
// Author: Vinhthuy Phan (2018)
//

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"sync"
)

type Configuration struct {
	IP      string
	Port    int
	Address string
}

type SubmissionData struct {
	Content string
	Ext     string
	Len     int
	Id      int
}

type BroadcastData struct {
	Content string
	Ext     string
}

var TeacherMessage = &BroadcastData{}
var StudentMessages = make([]*SubmissionData, 0)
var TeacherMessageMutex sync.Mutex
var StudentMessagesMutex sync.Mutex
var Config *Configuration
var SubmissionCounter = 0
var Usage = `
Usage:
	go_program  config.json

config.json is a json-formated file with 2 fields, IP and Port.

Example of config.json:
{
	"IP": "127.0.0.1",
	"Port": 8282
}
`

//-----------------------------------------------------------------
func showHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Teacher Message:\n")
	if TeacherMessage != nil {
		fmt.Println("Ext:", TeacherMessage.Ext)
		fmt.Println(TeacherMessage.Content, "\n")
	}
	fmt.Println("Student Messages:")
	for i := 0; i < len(StudentMessages); i++ {
		fmt.Println(StudentMessages[i].Id, StudentMessages[i].Len, StudentMessages[i].Ext)
		fmt.Println(StudentMessages[i].Content, "\n")
	}
}

//-----------------------------------------------------------------
func teacher_peeksHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, fmt.Sprintf("%d", len(StudentMessages)))
}

//-----------------------------------------------------------------
func teacher_receivesHandler(w http.ResponseWriter, r *http.Request) {
	StudentMessagesMutex.Lock()
	defer StudentMessagesMutex.Unlock()
	val := &SubmissionData{}
	if len(StudentMessages) != 0 {
		val = StudentMessages[0]
		val.Len = len(StudentMessages)
		StudentMessages = StudentMessages[1:]
	}
	js, err := json.Marshal(val)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		w.Header().Set("Content-Type", "application/json")
		w.Write(js)
	}
}

//-----------------------------------------------------------------
func teacher_sharesHandler(w http.ResponseWriter, r *http.Request) {
	TeacherMessageMutex.Lock()
	defer TeacherMessageMutex.Unlock()
	if r.FormValue("clear") == "yes" {
		TeacherMessage = &BroadcastData{}
		fmt.Fprintf(w, "Broadcast message is cleared.")
	} else if len(r.FormValue("content")) > 0 {
		TeacherMessage = &BroadcastData{
			Content: r.FormValue("content"),
			Ext:     r.FormValue("ext"),
		}
		fmt.Fprintf(w, "Content is shared.")
	} else {
		fmt.Fprintf(w, "Content is empty.  Select text to share.")
	}
}

//-----------------------------------------------------------------
func student_receivesHandler(w http.ResponseWriter, r *http.Request) {
	TeacherMessageMutex.Lock()
	defer TeacherMessageMutex.Unlock()
	js, err := json.Marshal(TeacherMessage)
	if err != nil {
		fmt.Println(err.Error())
	} else {
		w.Header().Set("Content-Type", "application/json")
		w.Write(js)
	}
}

//-----------------------------------------------------------------
func student_sharesHandler(w http.ResponseWriter, r *http.Request) {
	StudentMessagesMutex.Lock()
	defer StudentMessagesMutex.Unlock()
	if len(r.FormValue("content")) > 0 {
		SubmissionCounter++
		StudentMessages = append(StudentMessages, &SubmissionData{
			Content: r.FormValue("content"),
			Ext:     r.FormValue("ext"),
			Id:      SubmissionCounter,
		})
		fmt.Fprintf(w, "Content is shared.")
	} else {
		fmt.Fprintf(w, "Content is empty.  Select text to share.")
	}
}

//-----------------------------------------------------------------
func init_config(filename string) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	decoder := json.NewDecoder(file)
	Config = &Configuration{}
	err = decoder.Decode(&Config)
	if err != nil {
		log.Fatal(err)
	}
	Config.Address = fmt.Sprintf("%s:%d", Config.IP, Config.Port)
}

//-----------------------------------------------------------------
func main() {
	http.HandleFunc("/show", showHandler)
	http.HandleFunc("/teacher_peeks", teacher_peeksHandler)
	http.HandleFunc("/teacher_shares", teacher_sharesHandler)
	http.HandleFunc("/teacher_receives", teacher_receivesHandler)
	http.HandleFunc("/student_shares", student_sharesHandler)
	http.HandleFunc("/student_receives", student_receivesHandler)
	if len(os.Args) != 2 {
		fmt.Println(Usage)
		os.Exit(1)
	}
	init_config(os.Args[1])
	fmt.Println("**************************************************")
	fmt.Println("* VBoard running on", Config.Address)
	fmt.Println("**************************************************")
	err := http.ListenAndServe(Config.Address, nil)
	if err != nil {
		log.Fatal("Unable to serve gem server at " + Config.Address)
	}
}
