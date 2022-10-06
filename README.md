# AVA Digital Assistant

A Virtual Desktop Assistant Written in Python.
<br> It's generally a basic virtual assistant<br>
The basic purpose of this is to make work easier as it re-directs you to various main sites and performs various important functions for your PC as well just install it for your system and run it in your code editor or IDE.<br>
<br>Github Desktop and Git are mandatory - https://desktop.github.com/ - https://git-scm.com/downloads<br>

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

# Installing PyAudio
<br>Make sure that you have python 3.9 installed for this step<br>
<br>Check your python version using<br>
```
Python
exit()

```
<br>Pull your bit size<br>
```
Python 3.9.12 (tags/v3.9.12:b28265d, Mar 23 2022, 23:52:46) [MSC v.1929 64 bit (AMD64 <----- )] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```           
<br>In this case the bit size is AMD64<br>
<br>Installing the right package. So in that case they would run<br>
```
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

```
<br>If AMD64 isn't what shows up then run<br>
```
pip install PyAudio‑0.2.11‑cp39‑cp39‑win32.whl
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
