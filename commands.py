import configparser
import random
import smtplib
import sys

import wikipedia
from pygame import mixer

from actions import open_url, search, speak, wish_me_bye

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
    except KeyError:  # If the website is unknown
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
            break

def command_hello():
    speak("Hello")
