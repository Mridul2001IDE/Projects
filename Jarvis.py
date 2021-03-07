import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

MASTER = "Mridul"


# Speak function will pronounce the string which is passed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()


print("Initializing Jarvis...")


# This function will wish the author as per the time
def wishme():
    hour = datetime.datetime.now().hour
    # print(hour)
    if 0 <= hour < 12:
        print("Good morning sir!!")
        speak("Good morning sir")
    elif 12 < hour < 24:
        print("Good evening Sir")
        speak("Good evening sir")
    speak("I am Jarvis, How may i help you?")


# This function will take command from Microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
        # print("user said: "+query)
    except:
        print("Say that again")
        query = None
    return query


# Main program starts here

wishme()
# takecommand()
query = takecommand()
query = query.lower()

# Logics

if 'wikipedia' in query:
    speak("Searching wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)

