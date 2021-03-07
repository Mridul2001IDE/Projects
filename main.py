import speech_recognition as sr
import pyttsx3  # python text-to-speech
import pywhatkit
import datetime
# import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            print("Listening....")

            voice = listener.listen(source)

            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


# def name_input():
#     with sr.Microphone() as source:
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[1].id)
#
#         # print("Hi! Can i know to whom am i Talking?")
#         # talk("Hi! Can i know to whom am i Talking?")
#         print("Listening....")
#         talk("Listening");
#         voice = listener.listen(source)
#         name = listener.recognize_google(voice)
#         name = name.lower()
#         # name = take_command()
#     return name


def run_alexa():
    # name = name_input()
    command = take_command()

    if 'alexa' in command:
        print("Hi" + name + "What can i do for you")
        talk("Hi" + name + "What can i do for you")

    elif 'play' and 'song' in command:
        song = command.replace('play', '')
        print('Playing ' + song)
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'current time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    # elif 'Who the heck is ' in command:
    #     person = command.replace('Who the heck is', '')
    #     print(wikipedia.summary(person, 1))
    #     # print(info)
    #     talk(wikipedia.summary(person, 1))
    elif 'joke' in command:
        jj = pyjokes.get_joke()
        print(jj)
        talk(jj)

    elif 'stop' or 'end' in command:
        exit()

    else:
        exit()


while True:
    run_alexa()
