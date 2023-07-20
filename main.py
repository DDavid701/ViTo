import datetime
import time
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from playsound import playsound
import pyjokes as pj
import random
import requests
import os
os.system("cls")
load_dotenv("assets/settings.env") #SettingsFile path
#Settings
Username=os.getenv("Username")
AssistantName=os.getenv("AssistantName")
GeneralLanguage=os.getenv("GeneralLanguage")
TerminalPrefix=os.getenv("TerminalPrefix")
#Settings

if GeneralLanguage=='de-DE':
    jokelanguage='de'
elif GeneralLanguage=='en-GB':
    jokelanguage='en'
else:
    print(TerminalPrefix + " <|> Error 1: Can't define General Language!")
    raise SystemExit

#VersionChecker
version='beta-0.4-pre2' #Dont Edit this!
url = 'https://pastebin.com/raw/RmfvMed7'
request_latest = requests.get(url)
latest_version = request_latest.text
if version==latest_version:
    print(TerminalPrefix + " <|> This is a Pre-Release Version!")
else:
    print(TerminalPrefix + " <|> This is a Pre-Release Version!")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[-2].id)
def speek(line):
    engine.say(line)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

    try:
        listened = recognizer.recognize_google(audio, language=GeneralLanguage)
        print(f"{TerminalPrefix} <|> {listened}")
    except Exception:
        return "None"


    return listened.lower()

if __name__ == "__main__":
    load_dotenv("assets/messages.env")
    joke=os.getenv("Joke_" + GeneralLanguage)
    clock=os.getenv("Clock_" + GeneralLanguage)
    date=os.getenv("Date_" + GeneralLanguage)
    random_int=os.getenv("RanNum_" + GeneralLanguage)
    shutdown=os.getenv("Shutdown_" + GeneralLanguage)

    while True:

        listened = listen()

        if AssistantName in listened:
            first_run = True
            playsound("assets/assistant_activate.mp3")

            while True:

                if joke in listened:
                    speek(pj.get_joke(language=jokelanguage))
                    break

                if clock in listened:
                    clocktime=time.strftime("%H:%M")
                    speek(clocktime)
                    break

                if date in listened:
                    speek(datetime.datetime.today())
                    break

                if random_int in listened:
                    speek("Please say the minimum of the number?")
                    minimum = listen()
                    speek("Please say the maximum of the number?")
                    maximum = listen()
                    print(TerminalPrefix + " <|> " + minimum, maximum)
                    speek("Random Number is generating...")
                    try:
                        generated_number = random.randint(int(minimum), int(maximum))
                        speek("Your Number is " + str(generated_number))
                        break
                    except Exception:
                        speek("Can't Generate the Number!")
                        break


                if shutdown in listened:
                    print(TerminalPrefix + " <|> " + shutdown)
                    speek(shutdown)
                    time.sleep(0.3)
                    raise SystemExit

                else:
                    playsound("assets/assistant_deactivate.mp3")
                    break

                first_run = False
                listened = listen()
