import configparser, random, smtplib, sys, datetime, getpass, os, webbrowser
import time, playsound, urllib.parse, urllib.error
import calendar
import bs4 as bs
import urllib.request, sys, stdiomask, subprocess, webbrowser, pyperclip
import wikipedia
from pygame import mixer
from actions import open_url, search, speak, wish_me_bye
from collections import Counter

config = configparser.ConfigParser()  # if exists loads library.
config.read('config.ini')


def command_wikipedia(debug, query):
    speak("Searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    if debug == "True":
        print(results)
    else:
        pass
    speak(results)


def command_whatsup():
    st_msgs = [
        "I am just doing my thing",
        "Nothing Much",
    ]
    speak(random.choice(st_msgs))


def command_open(query, popular_websites, debug, search_engine, take_command):
    website = query.replace("open", "").strip().lower()
    try:
        open_url(popular_websites[website])
    except KeyError:
        if debug == "True":
            print(f"Unknown website: {website}")
        else:
            pass
        speak(f"Sorry, i don't know the website {website}")
        speak(f"¿Do you want me to search {website} in the web?")
        if take_command() == "yes":
            search(website, search_engine)
        else:
            pass


def command_search(query, search_engine):
    search_query = query.split("for")[-1]
    search(search_query, search_engine)

def command_nothing():
    master = config['DEFAULT']['master']
    wish_me_bye(master)
    sys.exit()

def command_echo():
    while True:
        try:
            num1 = input("What would you like to say?: ")
            speak(num1)
        except KeyboardInterrupt:
            print(' ')
            break

def command_hello():
    master = config['DEFAULT']['master']
    speak("Hello "+master)

def command_weather():
    weatherurl = config['DEFAULT']['weatherurl']
    source = urllib.request.urlopen(weatherurl).read()
    soup = bs.BeautifulSoup(source,'lxml')
    for paragraph in soup.find_all('span', class_='high-temp-text'):
        hightemp = paragraph.text
    for paragraph in soup.find_all('span', class_='low-temp-text'):
        lowtemp = paragraph.text
    for paragraph in soup.find_all('span', class_='summary swap'):
        current = paragraph.text
    speak('It is currently '+current+' with a high of '+hightemp+' and a low temp of '+lowtemp)

def command_news(take_command):
    i = 0
    result = 'No Stories Found'
    result1 = 'No Stories Found'
    v = 0
    c = 0
    speak('What would you like to search for')
    search = take_command()
    if "today's stories" in search or "top stories"in search:
        source = urllib.request.urlopen('https://news.google.com/topics/').read()
        soup = bs.BeautifulSoup(source,'lxml')

        for para in soup.find_all('a', class_='DY5T1d RZIKme'):
            v = para.text
            if c > 6:
                break
            c= c+1
            speak(v)
            # print(v)
            result = 1
    else:
        try:
            source = urllib.request.urlopen('https://news.google.com/topics/').read()
            soup = bs.BeautifulSoup(source,'lxml')
            for para in soup.find_all('a', class_='DY5T1d RZIKme'):
                v = para.text
                if search in v:
                    result1 = v
                    para = str(para)
                    parag = para[para.index('href=".')+7:para.index('">')]
                    url = 'https://news.google.com/'+parag
                    speak(result1)
        except urllib.error.URLError:
            speak("Check your internet connection, oh wait you don't have one.")
    if result == result1:
        speak("I haven't found any stories with that headline")
