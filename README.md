# PING Digital Assistant

A Virtual Desktop Assistant Written in Python.
<br> It's generally a basic virtual assistant<br>
The basic purpose of this is to make work easier as it re-directs you to various main sites and performs various important functions for your PC as well just install it for your system and run it in your code editor or IDE.
Github Desktop is mandatory - https://desktop.github.com/
Highly recommended that git is installed - https://git-scm.com/downloads<br>

# Installing 

- Clone the repo to make it available on your local system by using ```git clone <FORKED_REPO_URL>```
- cd into the project directory i.e  - ```cd DesktopAssitant```


# Requirements for Windows
Steps to run the Assistant on your pc (use python 3.9) - https://www.python.org/downloads/windows/

Installing all the necessary python module using
```
pip install subprocess
python setupimports.py

```             

# Personalizing The Assistant
In an editor open the file config.ini, the two top most items<br>
```
master = User
voice = Female
```
Replace User With Your Name<br>
Then change the voice to your preference Female or Male<br>

# Run
For windows user run
```
python main.py
```

# Optional - Creating a Shortcut
1. open File Explorer and go to the cloned folder
2. find and open the file PING.bat
3. Replace the brackets with the file path to main.py (no quotes)

