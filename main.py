import datetime
import time
import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
from playsound import playsound
from threading import Thread
import wikipedia as wp
import pyjokes as pj
import random
import requests
import os
from colorama import *
init(autoreset=True)
print(Fore.GREEN + """
__      ___ _______    
\ \    / (_)__   __|   
 \ \  / / _   | | ___  
  \ \/ / | |  | |/ _ \ 
   \  /  | |  | | (_) |
    \/   |_|  |_|\___/                
""" + Fore.LIGHTGREEN_EX + "[ViTo beta-0.7.0] made by DZYT002")
print("Github: " + Fore.LIGHTBLUE_EX + "https://github.com/DZYT002/ViTo")
def ErrorCode(error):
    if error == 0:
        print(Fore.LIGHTRED_EX + "[!] Error 0: Can't define General Language!")
    elif error == 1:
        print(Fore.LIGHTRED_EX + "[!] Error 1: The Program has an unknown issue! Please Report this!")
    elif error == 2:
        print(Fore.LIGHTRED_EX + "[!] Error 2: 'playsound' Library ran into an Error!")
    elif error == 3:
        print(Fore.LIGHTRED_EX + "[!] Error 3: Text to Speech Library ran into an Error!")
    elif error == 4:
        print(Fore.LIGHTRED_EX + "[!] Error 4: SpeechRecognition ran into an Error!")
    elif error == 5:
        print(Fore.LIGHTRED_EX + "[!] Error 5: This Language is still in development!")
    elif error == 6:
        print(Fore.LIGHTRED_EX + "[!] Error 6: Can't Connect with the Internet!")
    else:
        print(Fore.RED + "[!] Error -1: An Fatal Error occurred! (Please Report this Issue.)")
def ringtone():
    count = 0
    while (count < 5):
        count = count + 1
        try:
            playsound("assets/assistant_timer_ringtone.mp3")
        except Exception:
            ErrorCode(2)
            break
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
elif GeneralLanguage=='en-US':
    ErrorCode(5)
    raise SystemExit
else:
    ErrorCode(0)
    raise SystemExit

if GeneralLanguage=='de-DE':
    speekvoice=-2
elif GeneralLanguage=='en-GB':
    speekvoice=-1
elif GeneralLanguage=='en-US':
    ErrorCode(5)
    raise SystemExit
else:
    ErrorCode(0)
    raise SystemExit

if GeneralLanguage=='de-DE':
    wp.set_lang("de")
elif GeneralLanguage=='en-GB':
    wp.set_lang("en")
elif GeneralLanguage=='en-US':
    ErrorCode(5)
    raise SystemExit
else:
    ErrorCode(0)
    raise SystemExit

#Testing
url = 'https://google.com/'
request_internet = requests.get(url)
if request_internet.status_code == 200:
    print(f"{TerminalPrefix} <|>"+Fore.GREEN+" Connected with the Internet!")
else:
    print(f"[!] The Status Code is {request_internet.status_code}")
    ErrorCode(6)
    raise SystemExit


#VersionChecker
version='beta-0.7' #don't edit this!
url = 'https://pastebin.com/raw/RmfvMed7' #don't edit this unless you're using a fork version!
request_latest = requests.get(url)
latest_version = request_latest.text
if version==latest_version:
    print(Fore.LIGHTGREEN_EX + TerminalPrefix + " <|> There's no new Version available!")
else:
    print(Fore.LIGHTRED_EX + TerminalPrefix + f" <|> There's a new Version available! [{latest_version}]")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[speekvoice].id)
def speek(line):
    try:
        engine.say(line)
        engine.runAndWait()
    except Exception:
        ErrorCode(3)
        raise SystemExit
def listen():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
        try:
            listened = recognizer.recognize_google(audio, language=GeneralLanguage)
            print(f"{TerminalPrefix} <|> {listened}")
        except Exception:
            return ""
    except Exception:
        raise SystemExit


    return listened.lower()

if __name__ == "__main__":
    load_dotenv("assets/messages.env")
    joke=os.getenv("Joke_" + GeneralLanguage)
    clock=os.getenv("Clock_" + GeneralLanguage)
    clock_message=os.getenv("Clock_msg_" + GeneralLanguage)
    date=os.getenv("Date_" + GeneralLanguage)
    date_message=os.getenv("Date_msg_" + GeneralLanguage)
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
    wikipedia_message2=os.getenv("Wikipedia_message2_" + GeneralLanguage)
    note_add_trigger=os.getenv("Notes_Add_" + GeneralLanguage)
    note_add_msg1=os.getenv("Notes_Add_msg1_" + GeneralLanguage)
    note_add_msg2=os.getenv("Notes_Add_msg2_" + GeneralLanguage)
    note_rem_trigger=os.getenv("Notes_Rem_" + GeneralLanguage)
    note_rem_msg1 = os.getenv("Notes_Rem_msg1_" + GeneralLanguage)
    note_rem_msg2 = os.getenv("Notes_Rem_msg2_" + GeneralLanguage)
    note_rem_msg3 = os.getenv("Notes_Rem_msg3_" + GeneralLanguage)
    note_read_trigger=os.getenv("Notes_Read_" + GeneralLanguage)
    note_read_msg1 = os.getenv("Notes_Read_msg1_" + GeneralLanguage)
    note_read_msg2 = os.getenv("Notes_Read_msg2_" + GeneralLanguage)
    note_read_msg3 = os.getenv("Notes_Read_msg3_" + GeneralLanguage)
    timer_trigger = os.getenv("Timer_Trigger_" + GeneralLanguage)
    timer_msg1 = os.getenv("Timer_msg1_" + GeneralLanguage)
    timer_msg2 = os.getenv("Timer_msg2_" + GeneralLanguage)
    timer_msg3 = os.getenv("Timer_msg3_" + GeneralLanguage)
    timer_set_min = os.getenv("Timer_set_min_" + GeneralLanguage)
    timer_set_sec = os.getenv("Timer_set_sec_" + GeneralLanguage)
    shutdown=os.getenv("Shutdown_" + GeneralLanguage)

    while True:

        listened = listen()

        if AssistantName in listened:
            first_run = True
            try:
                playsound("assets/assistant_activate.mp3")
            except Exception:
                ErrorCode(2)
                break


            while True:

                if joke in listened:
                    speek(pj.get_joke(language=jokelanguage))
                    break

                if clock in listened:
                    clocktime=time.strftime("%H:%M")
                    speek(clock_message + clocktime)
                    break

                if date in listened:
                    date_today = datetime.datetime.today()
                    speek(date_message + date_today)
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
                    def wp_search_func():
                        speek(wp_search)
                    speek(wikipedia_message)
                    wp_query=listen()
                    try:
                        wp_search = wp.summary(wp_query)
                        thread_wp_1 = Thread(target=wp_search_func)
                        thread_wp_1.start()
                        break
                    except wikipedia.exceptions.PageError:
                        print("Error!")
                        speek(f"{wp_query}" + wikipedia_message2)
                        break


                def note_read():
                    notes = []
                    with open("notes.txt", "r") as file:
                        lines = file.readlines()
                        for line in lines:
                            notes.append(str(line.strip()))
                    if not notes:
                        speek(note_read_msg1)
                        speek(note_read_msg2)
                    else:
                        speek(note_read_msg3)
                        speek(line)

                if note_add_trigger in listened:
                    speek(note_add_msg1)
                    listened_item=listen()
                    with open("notes.txt", "a") as addfile:
                        addfile.write(str(listened_item) + "\n")
                        speek(note_add_msg2)
                        break

                if note_rem_trigger in listened:
                    note_read()
                    speek(note_rem_msg1)
                    note_to_remove = listen()
                    with open("notes.txt", "r") as file:
                        lines = file.readlines()

                    with open("notes.txt", "w") as remfile:
                        removed = False
                        for line in lines:
                            note = line.strip()
                            if note == note_to_remove:
                                removed = True
                            else:
                                remfile.write(line)
                    if removed:
                        speek(note_rem_msg2)
                    else:
                        speek(note_rem_msg3)

                if note_read_trigger in listened:
                    notes = []
                    with open("notes.txt", "r") as readfile:
                        lines = readfile.readlines()
                        for line in lines:
                            notes.append(str(line.strip()))
                    if not notes:
                        speek(note_read_msg1)
                        speek(note_read_msg2)
                    else:
                        speek(note_read_msg3)
                        speek(line)

                def atimer(amount, sec_or_min):
                    if sec_or_min == 'min':
                        speek(f'{timer_set_min}')
                        time.sleep(int(amount) * 60)
                        ringtone()
                    elif sec_or_min == 'sec':
                        speek(f'{timer_set_sec}')
                        time.sleep(int(amount))
                        ringtone()
                    else:
                        print("Error 1: The Program has an unknown issue! Please Report this!")

                if timer_trigger in listened:
                    speek(timer_msg1)
                    atimer_listen = listen()
                    if "min" in atimer_listen:
                        speek(timer_msg2)
                        atimer_listen2 = listen()
                        testthr = Thread(target=atimer, args=(atimer_listen2, "min"))
                        testthr.start()
                        break
                    elif "sek" in atimer_listen:
                        speek(timer_msg2)
                        atimer_listen2 = listen()
                        testthr = Thread(target=atimer, args=(atimer_listen2, "sec"))
                        testthr.start()
                    else:
                        speek(timer_msg3)
                        break

                if shutdown in listened:
                    print(Fore.RED + TerminalPrefix + " <|> " + shutdown)
                    speek(shutdown)
                    time.sleep(0.3)
                    raise SystemExit

                else:
                    try:
                        playsound("assets/assistant_deactivate.mp3")
                        break
                    except Exception:
                        ErrorCode(2)
                        break

                first_run = False
                listened = listen()
