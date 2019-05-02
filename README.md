To use this software to share code in class, you will need to (1) install [Sublime Text 3](https://www.sublimetext.com/3) and (2) install a specific plug in for Sublime Text.

To install Sublime Text 3, [go here.](https://www.sublimetext.com/3)

### Student's installation

(1) Open Sublime Text.  Select **New File** in the File menu.

(2) Select **Show Console** in the View menu.

[Note: The console appears at the bottom of the Sublime window. Python code can be executed in the console.]

(3) Copy, paste the following code to Console and hit Enter:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardS"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardS.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardS.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Student", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```

(4) Set the server address

### Teacher's installation

(1) Open Sublime Text.  Select **New File** in the File menu.

(2) Select **Show Console** in the View menu.

[Note: The console appears at the bottom of the Sublime window. Python code can be executed in the console.]

(3) Copy, paste the following code to Console and hit Enter:
```
import os; package_path = os.path.join(sublime.packages_path(), "VBoardT"); os.mkdir(package_path) if not os.path.isdir(package_path) else print("dir exists"); module_file = os.path.join(package_path, "VBoardT.py") ; menu_file = os.path.join(package_path, "Main.sublime-menu"); version_file = os.path.join(package_path, "version.go"); import urllib.request; urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/VBoardT.py", module_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/Main.sublime-menu-Teacher", menu_file); urllib.request.urlretrieve("https://raw.githubusercontent.com/vtphan/VBoard/master/version.go", version_file)
```
(4) Set the server address

(5) Download the latest server ([Windows](http://umdrive.memphis.edu/vphan/public/VBoard/vboard.exe), [MacOS](http://umdrive.memphis.edu/vphan/public/VBoard/vboard)) and make them *executable* on teacher's computer.  This command-line server needs to be run on the teacher's computer every time VBoard is used in class.

Run the server
```
    ./vboard config.json
```

