import datetime
import time
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from playsound import playsound
import wikipedia as wp
import pyjokes as pj
import random
import requests
import os
playsound("assistant_programstart.mp3")
os.system("cls")
load_dotenv("settings.env") #SettingsFile path
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
    print(TerminalPrefix + " <|> Error 0: Can't define General Language!")
    raise SystemExit

if GeneralLanguage=='de-DE':
    speekvoice=-2
elif GeneralLanguage=='en-GB':
    speekvoice=-1
else:
    print(TerminalPrefix + " <|> Error 0: Can't define General Language!")
    raise SystemExit

if GeneralLanguage=='de-DE':
    wp.set_lang("de")
elif GeneralLanguage=='en-GB':
    wp.set_lang("en")
else:
    print(TerminalPrefix + " <|> Error 0: Can't define General Language!")
    raise SystemExit



#VersionChecker
version='beta-0.6-pre2' #Dont Edit this!
url = 'https://pastebin.com/raw/RmfvMed7'
request_latest = requests.get(url)
latest_version = request_latest.text
if version==latest_version:
    print(TerminalPrefix + " <|> This is a Pre-Release (Unstable)")
else:
    print(TerminalPrefix + " <|> This is a Pre-Release (Unstable)")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[speekvoice].id)
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
    load_dotenv("messages.env")
    joke=os.getenv("Joke_" + GeneralLanguage)
    clock=os.getenv("Clock_" + GeneralLanguage)
    date=os.getenv("Date_" + GeneralLanguage)
    random_int_trigger=os.getenv("RanNum_" + GeneralLanguage)
    random_int_min=os.getenv("RanNum_Min_" + GeneralLanguage)
    random_int_max=os.getenv("RanNum_Max_" + GeneralLanguage)
    random_int_gen=os.getenv("RanNum_Gen_" + GeneralLanguage)
    random_int_is=os.getenv("RanNum_Is_" + GeneralLanguage)
    random_int_err=os.getenv("RanNum_Err_" + GeneralLanguage)
    math_plus_trigger=os.getenv("MathPlus_" + GeneralLanguage)
    math_plus_main=os.getenv("MathPlus_main_" + GeneralLanguage)
    math_plus_seco=os.getenv("MathPlus_seco_" + GeneralLanguage)
    math_plus_answ=os.getenv("MathPlus_answ_" + GeneralLanguage)
    math_plus_err=os.getenv("MathPlus_err_" + GeneralLanguage)
    math_minus_trigger = os.getenv("MathMinus_" + GeneralLanguage)
    math_minus_main = os.getenv("MathMinus_main_" + GeneralLanguage)
    math_minus_seco = os.getenv("MathMinus_seco_" + GeneralLanguage)
    math_minus_answ = os.getenv("MathMinus_answ_" + GeneralLanguage)
    math_minus_err = os.getenv("MathMinus_err_" + GeneralLanguage)
    wikipedia_trigger=os.getenv("Wikipedia_" + GeneralLanguage)
    wikipedia_message=os.getenv("Wikipedia_message_" + GeneralLanguage)
    shutdown=os.getenv("Shutdown_" + GeneralLanguage)

    while True:

        listened = listen()

        if AssistantName in listened:
            first_run = True
            playsound("assistant_activate.mp3")

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

                if random_int_trigger in listened:
                    speek(random_int_min)
                    minimum = listen()
                    speek(random_int_max)
                    maximum = listen()
                    print(TerminalPrefix + " <|> " + minimum, maximum)
                    speek(random_int_gen)
                    try:
                        generated_number = random.randint(int(minimum), int(maximum))
                        speek(random_int_is + str(generated_number))
                        break
                    except Exception:
                        speek(random_int_err)
                        break

                if math_plus_trigger in listened:
                    speek(math_plus_main)
                    math_plus_first = listen()
                    speek(math_plus_seco)
                    math_plus_second = listen()
                    try:
                        math_plus_answer = int(math_plus_first) + int(math_plus_second)
                        speek(math_plus_answ + str(math_plus_answer))
                        break
                    except Exception:
                        speek(f"{math_plus_err}")
                        break

                if math_minus_trigger in listened:
                    speek(math_plus_main)
                    math_minus_first = listen()
                    speek(math_plus_seco)
                    math_minus_second = listen()
                    try:
                        math_minus_answer = int(math_minus_first) - int(math_minus_second)
                        speek(math_minus_answ + str(math_minus_answer))
                        break
                    except Exception:
                        speek(f"{math_minus_err}")
                        break

                if wikipedia_trigger in listened:
                    speek(wikipedia_message)
                    wp_query=listen()
                    wp_search = wp.summary(wp_query)
                    speek(wp_search)
                    break

                if "note add" in listened:
                    speek("What do you want to add?")
                    listened_item=listen()
                    print(listened_item)
                    with open("notes.txt", "a") as addfile:
                        addfile.write(str(listened_item) + "\n")
                        break

                if "note read" in listened:
                    notes = []
                    with open("notes.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            notes.append(str(line.strip()))
                    if not notes:
                        speek("You don't have any notes yet!")
                    else:
                        speek("Your notes are: ")
                        speek(line)
                        speek("if you want to add notes say 'vito add a note!'")

                if shutdown in listened:
                    print(TerminalPrefix + " <|> " + shutdown)
                    speek(shutdown)
                    time.sleep(0.3)
                    raise SystemExit

                else:
                    playsound("assistant_deactivate.mp3")
                    break

                first_run = False
                listened = listen()
