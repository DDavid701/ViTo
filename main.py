import pyjokes
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from playsound import playsound
import pyjokes as pj
import requests
import os
os.system("cls")
load_dotenv("settings.env") #SettingsFile path
#Settings
Username=os.getenv("Username")
AssistantName=os.getenv("AssistantName")
GeneralLanguage=os.getenv("GeneralLanguage")
#Settings

#VersionChecker
version='beta-0.3' #Dont Edit this!
url = 'https://pastebin.com/raw/RmfvMed7'
request_latest = requests.get(url)
latest_version = request_latest.text
if version==latest_version:
    print("AssistantV2 <|> No new versions available!")
else:
    print("AssistantV2 <|> New version is available, please update the program!")

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
        print(f"AssistantV2 <|> {listened}")
    except Exception:
        return "None"


    return listened.lower()

if __name__ == "__main__":
    while True:

        listened = listen()

        if AssistantName in listened:
            first_run = True
            playsound("assets/assistant_activate.mp3")

            while True:

                if "witz" in listened:
                    speek(pyjokes.get_joke(language="en"))
                    break

                if "stop vito" in listened:
                    raise SystemExit

                else:
                    playsound("assets/assistant_deactivate.mp3")

                    break

                first_run = False
                listened = listen()
