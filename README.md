# PING Digital Assistant

A Virtual Desktop Assistant Written in Python.
<br> It's generally a basic virtual assistant<br>
The basic purpose of this is to make work easier as it re-directs you to various main sites and performs various important functions for your PC as well just install it for your system and run it in your code editor or IDE.<br>

# Installing :

- Clone the repo to make it available on your local system by using ```git clone <FORKED_REPO_URL>```
- cd into the project directory i.e  - ```cd DesktopAssitant```


# Requirements for windows
Steps to run the Assistant on your pc (use python 3.9)

Installing all the necessary python module using
```
pip install -r requirements.txt
pip install playsound
pip install beautifulsoup4
pip install wikipedia
pip install pyttsx3
pip install lxml

```             

# Creating a Shortcut
First run in the cloned Repository folder
```
python batchcreator.py
```             
Next it will ask for a file path, The path to the you want to give it is the file path of PING.bat <br>
Then it will ask for the location of your desktop folder in order to install a shortcut, Provide it with a path (i.e. "C:\Users\[Your User Abbrev.]\Desktop") <br>

# Personalizing The assistant
In an editor open the file config.ini, the two top most items<br>
```
master = User
voice = Female
```
Replace User with your name<br>
Then change the voice to your preference Female or Male<br>

# Run
For windows user run
```
python main.py
```
