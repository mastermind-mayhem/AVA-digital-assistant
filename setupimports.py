import configparser, random, smtplib, sys, datetime, getpass, os, webbrowser
import time, playsound, urllib.parse, urllib.error
import calendar
import bs4 as bs
import urllib.request, sys, stdiomask, subprocess, webbrowser, pyperclip
import wikipedia
from pygame import mixer
# import getpass, os
# # USER_NAME = getpass.getuser()
# filepath = input("file path?: ")
# locationpath = input("locationpath?: ")
# batchname = 'PING'
# def add_to_startup(file_path=filepath):
#     if file_path == filepath:
#         file_path = os.path.dirname(os.path.realpath(__file__))
#     bat_path = locationpath
#     # bat_path = r'C:\Users\maste\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
#     with open(bat_path + '\\ ' +batchname+".bat", "w+") as bat_file:
#         bat_file.write(r'start "" '+filepath)
# add_to_startup()
# print('Shortcut has been created')
# # start "" C:\Users\maste\OneDrive\Documents\Atom\AVA7.beta\startup.py
subprocess.run("pip install -r requirements.txt", shell=True)
subprocess.run("pip install playsound", shell=True)
subprocess.run("pip install BeautifulSoup4", shell=True)
subprocess.run("pip install wikipedia", shell=True)
subprocess.run("pip install pyttsx3", shell=True)
subprocess.run("pip install lxml", shell=True)
