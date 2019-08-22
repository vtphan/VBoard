To use this software to share code in class, you will need to (1) install [Sublime Text 3](https://www.sublimetext.com/3) and (2) install a specific plug in for Sublime Text.

To install Sublime Text 3, [go here.](https://www.sublimetext.com/3)

****

# For Students

## Installation

(1) Open Sublime Text.  Select **New File** in the File menu.

(2) Select **Show Console** in the View menu.

[Note: The console appears at the bottom of the Sublime window. Python code can be executed in the console.]

(3) Copy, paste the following code to Console and hit Enter:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardS"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardS.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardS.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Student", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```

(4) Set the server address: 

+ Click on "Set server address" in the VBoardS menu of Sublime Text.  
+ Then, in the console input in the bottom of Sublime Text, enter the server address.
+ Your teacher should be able to tell you what the server address is.

## Usage

To share code with your teacher, select the code in a Sublime Text window and click "Share" in the VBoardS menu.

To receive code that was shared by the teacher, click "Receive" in the VBoardS menu.


****

# For teachers

## Installation

(1) Open Sublime Text.  Select **New File** in the File menu.

(2) Select **Show Console** in the View menu.

[Note: The console appears at the bottom of the Sublime window. Python code can be executed in the console.]

(3) Copy, paste the following code to Console and hit Enter:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardT"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardT.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardT.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Teacher", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```
(4) Set the server address.

+ Click on "Set server address" in the VBoardS menu of Sublime Text.  
+ Then, in the console input in the bottom of Sublime Text, enter the server address.
+ The server address can be specified explitly in the config.js file.  
If not, the vboard server will guess the server address and explicitly says what it is.

A server address looks like this:
```
SOME_IP_ADDRESS:8282
```

(5) Download the latest server ([Windows](http://umdrive.memphis.edu/vphan/public/VBoard/vboard.exe), [MacOS](http://umdrive.memphis.edu/vphan/public/VBoard/vboard)) and make them *executable* on teacher's computer.  This command-line server needs to be run on the teacher's computer every time VBoard is used in class.

Run the server
```
    ./vboard config.json
```

## Usage

To share code with your students, select the code in a Sublime Text window and click "Share" in the VBoardT menu.

To receive code that was shared by students one by one, click "Receive" in the VBoardT menu.

