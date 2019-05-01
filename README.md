To use this software to share code in class, you will need to (1) install [Sublime Text 3](https://www.sublimetext.com/3) and (2) install a specific plug in for Sublime Text.

To install Sublime Text 3, [go here.](https://www.sublimetext.com/3)

### Student's installation

(1) Open Sublime Text

(2) Click **Show Console** in the View menu.

(3) Copy this code:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardS"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardS.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardS.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Student", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```

(4) Paste copied code to Console and hit enter.

(5) In Sublime Text: (i) specify a folder on their computers to store local files, (ii) set the server address, which is shown when the server is run, and (iii) complete the registration by simply entering your given username.


### Teacher's installation

(1) Open Sublime Text

(2) Click **Show Console** in the View menu.

(3) Copy this code:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardT"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardT.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardT.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Teacher", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```
(4) Paste copied code to Console and hit enter.

(5) Download the latest server ([Windows](http://umdrive.memphis.edu/vphan/public/VBoard/vboard.exe), [MacOS](http://umdrive.memphis.edu/vphan/public/VBoard/vboard)) and make them *executable* on teacher's computer.  This command-line server needs to be run on the teacher's computer every time VBoard is used in class.

Run the server
```
    ./vboard config.json
```

