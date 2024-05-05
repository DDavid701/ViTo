try:
    import datetime
    import time
    import speech_recognition as sr
    import pyttsx3
    import platform
    from dotenv import load_dotenv
    from threading import Thread
    import wikipedia as wp
    import pyjokes as pj
    import random
    import requests
    import os
    from colorama import *
    init(autoreset=True)
except Exception:
    print("Installing Required Packages...")
    try:
        import os
        print("Installing SpeechRecognition...")
        os.system("pip3 install SpeechRecognition --break-system-packages")
        print("Installing PyTTSX3...")
        os.system("pip3 install pyttsx3 --break-system-packages")
        print("Installing DotENV...")
        os.system("pip3 install python-dotenv --break-system-packages")
        print("Installing Wikipedia...")
        os.system("pip3 install wikipedia --break-system-packages")
        print("Installing PyJokes...")
        os.system("pip3 install pyjokes --break-system-packages")
        print("Installing Requests...")
        os.system("pip3 install requests --break-system-packages")
        print("Installing Colorama...")
        os.system("pip3 install colorama --break-system-packages")
        import datetime
        import time
        import speech_recognition as sr
        import pyttsx3
        import platform
        from dotenv import load_dotenv
        from threading import Thread
        import wikipedia as wp
        import pyjokes as pj
        import random
        import requests
        import os
        from colorama import *
    except Exception as e:
        print("Couldn't install the requirements!")
        print(e)
        raise SystemExit

def msg(TYPE,CONTENT):
    if TYPE=="log":
        print(Fore.GREEN + "ViTo" + Fore.LIGHTBLACK_EX + " × " + Fore.LIGHTWHITE_EX + CONTENT)
    elif TYPE=="error":
        print(Fore.GREEN+"ViTo"+Fore.LIGHTBLACK_EX+" × "+Fore.LIGHTRED_EX+CONTENT)
    elif TYPE=="warning":
        print(Fore.GREEN + "ViTo" + Fore.LIGHTBLACK_EX + " × " + Fore.LIGHTYELLOW_EX + CONTENT)
    else:
        print(Fore.GREEN + "ViTo" + Fore.LIGHTBLACK_EX + " × " + Fore.RED + "Couldn't recognise message type! " + Fore.WHITE + "(" + Fore.LIGHTRED_EX+TYPE+Fore.WHITE+")")

print(Fore.LIGHTBLACK_EX+"["+Fore.YELLOW+"*"+Fore.LIGHTBLACK_EX+"] "+Fore.LIGHTWHITE_EX+"ViTo 1.0 by DDavid701")
print(Fore.LIGHTBLACK_EX+"["+Fore.YELLOW+"*"+Fore.LIGHTBLACK_EX+"] "+Fore.LIGHTBLUE_EX+"https://github.com/DDavid701/ViTo")
PLATFORM=platform.system()
msg("log", f"Operating System Detected: '{PLATFORM}'")

def ErrorCode(error):
    if error == 0:
        msg("error", "Error 0: Can't define General Language!")
    elif error == 1:
        msg("error", "Error 1: The Program has an unknown issue! Please Report this!")
    elif error == 2:
        msg("error", "Error 2: 'playsound' Library ran into an Error!")
    elif error == 3:
        msg("error", "Error 3: Text to Speech Library ran into an Error!")
    elif error == 4:
        msg("error","Error 4: SpeechRecognition ran into an Error!")
    elif error == 5:
        msg("error", "Error 5: This Language is still in development!")
    elif error == 6:
        msg("error", "Error 6: Can't Connect with the Internet!")
    else:
        msg("error", "Error -1: An Fatal Error occurred! (Please Report this Issue.)")

def warning(VALUE):
    if VALUE=="sound":
        msg("warning", "Sounds are disabled!")

def ringtone():
    COUNT = 0
    while (COUNT < 5):
        COUNT = COUNT + 1
        try:
            warning("sound")
            #playsound("assets/ringtone.mp3")
        except Exception:
            ErrorCode(2)
            break
if PLATFORM=="Windows":
    msg("log", "Running cls...")
    os.system("cls")
msg("log", "Loading Settings...")
load_dotenv("conf/settings.env") #SettingsFile path
USERNAME=os.getenv("Name")
WAKEWORD=os.getenv("WakeWord")
LANGUAGE=os.getenv("Language")
if LANGUAGE=="de-DE":
    LANGUAGE_SHORT="Deutsch"
elif LANGUAGE=="en-GB":
    LANGUAGE_SHORT="English"
else:
    LANGUAGE_SHORT = "unknown"
msg("log", "Loaded Settings!")

if LANGUAGE=='de-DE':
    msg("log", "Setting language to 'Deutsch'")
    JOKE_LANG='de'
elif LANGUAGE=='en-GB':
    msg("log", "Setting language to 'English'")
    JOKE_LANG='en'
else:
    ErrorCode(0)
    raise SystemExit
msg("log", f"Language set to '{LANGUAGE_SHORT}'")

if LANGUAGE=='de-DE':
    msg("log", f"Setting voice to '{LANGUAGE_SHORT}'")
    VOICE=-2
elif LANGUAGE=='en-GB':
    msg("log", f"Setting voice to '{LANGUAGE_SHORT}'")
    VOICE=-1
else:
    ErrorCode(0)
    raise SystemExit
msg("log", f"Voice set to '{LANGUAGE_SHORT}'")

if LANGUAGE=='de-DE':
    wp.set_lang("de")
elif LANGUAGE=='en-GB':
    wp.set_lang("en")
else:
    ErrorCode(0)
    raise SystemExit

# Internet Connection Test
URL = 'https://github.com/DDavid701/ViTo'
msg("log", f"Set url to '{URL}'")
REQUEST_CONNECTION = requests.get(URL)
if REQUEST_CONNECTION.status_code == 200:
    msg("log", f"Connected with the Internet! ({REQUEST_CONNECTION.status_code})")
else:
    msg("warning", f"Couldn't connect to {URL}! ({REQUEST_CONNECTION.status_code})")
    raise SystemExit


# Update Check
VERSION='1.0_pre3' #don't edit this!
msg("log", f"Detected version: '{VERSION}'")
URL = 'https://pastebin.com/raw/RmfvMed7'
REQUEST_VERSION = requests.get(URL)
LATEST_VERSION = REQUEST_VERSION.text
if VERSION==LATEST_VERSION:
    if "_pre" in VERSION:
        msg("warning", f"This is a Pre Release Version!")
    else:
        msg("log", "There's no new Version available!")
else:
    if "_pre" in VERSION:
        msg("warning", f"This is a Pre Release Version!")
    else:
        msg("warning", f"There's a new Version available! [{LATEST_VERSION}]")

if PLATFORM=="Windows":
    ENGINE=pyttsx3.init("sapi5")
elif PLATFORM=="MacOS":
    msg("error", "MacOS isnt supported yet!")
    raise SystemExit
elif PLATFORM=="Linux":
    ENGINE=pyttsx3.init("espeak")
else:
    ENGINE=pyttsx3.init("espeak")
VOICES=ENGINE.getProperty("voices")
ENGINE.setProperty("voice", VOICES[VOICE].id)
def speek(VALUE):
    try:
        ENGINE.say(VALUE)
        ENGINE.runAndWait()
    except Exception:
        ErrorCode(3)
        raise SystemExit
def listen():
    try:
        RECOGNIZER=sr.Recognizer()
        with sr.Microphone() as MICROPHONE:
            RECOGNIZER.adjust_for_ambient_noise(MICROPHONE, duration=0.2)
            AUDIO=RECOGNIZER.listen(MICROPHONE)
        try:
            RESULT=RECOGNIZER.recognize_google(AUDIO, language=LANGUAGE)
            msg("log", f"{RESULT}")
        except Exception:
            return "An Error occurred!"
    except Exception as e:
        msg("log", f"{e}")
        time.sleep(5)
        raise SystemExit


    return RESULT

if __name__ == "__main__":
    load_dotenv("conf/messages.env")
    msg("log", "Loading Language...")
    joke=os.getenv("Joke_"+LANGUAGE)
    clock=os.getenv("Clock_"+LANGUAGE)
    clock_message=os.getenv("Clock_msg_" + LANGUAGE)
    date=os.getenv("Date_" + LANGUAGE)
    date_message=os.getenv("Date_msg_" + LANGUAGE)
    random_int_trigger=os.getenv("RanNum_" + LANGUAGE)
    random_int_min=os.getenv("RanNum_Min_" + LANGUAGE)
    random_int_max=os.getenv("RanNum_Max_" + LANGUAGE)
    random_int_gen=os.getenv("RanNum_Gen_" + LANGUAGE)
    random_int_is=os.getenv("RanNum_Is_" + LANGUAGE)
    random_int_err=os.getenv("RanNum_Err_" + LANGUAGE)
    math_plus_trigger=os.getenv("MathPlus_" + LANGUAGE)
    math_plus_main=os.getenv("MathPlus_main_" + LANGUAGE)
    math_plus_seco=os.getenv("MathPlus_seco_" + LANGUAGE)
    math_plus_answ=os.getenv("MathPlus_answ_" + LANGUAGE)
    math_plus_err=os.getenv("MathPlus_err_" + LANGUAGE)
    math_minus_trigger = os.getenv("MathMinus_" + LANGUAGE)
    math_minus_main = os.getenv("MathMinus_main_" + LANGUAGE)
    math_minus_seco = os.getenv("MathMinus_seco_" + LANGUAGE)
    math_minus_answ = os.getenv("MathMinus_answ_" + LANGUAGE)
    math_minus_err = os.getenv("MathMinus_err_" + LANGUAGE)
    wikipedia_trigger=os.getenv("Wikipedia_" + LANGUAGE)
    wikipedia_message=os.getenv("Wikipedia_message_" + LANGUAGE)
    wikipedia_message2=os.getenv("Wikipedia_message2_" + LANGUAGE)
    note_add_trigger=os.getenv("Notes_Add_" + LANGUAGE)
    note_add_msg1=os.getenv("Notes_Add_msg1_" + LANGUAGE)
    note_add_msg2=os.getenv("Notes_Add_msg2_" + LANGUAGE)
    note_rem_trigger=os.getenv("Notes_Rem_" + LANGUAGE)
    note_rem_msg1 = os.getenv("Notes_Rem_msg1_" + LANGUAGE)
    note_rem_msg2 = os.getenv("Notes_Rem_msg2_" + LANGUAGE)
    note_rem_msg3 = os.getenv("Notes_Rem_msg3_" + LANGUAGE)
    note_read_trigger=os.getenv("Notes_Read_" + LANGUAGE)
    note_read_msg1 = os.getenv("Notes_Read_msg1_" + LANGUAGE)
    note_read_msg2 = os.getenv("Notes_Read_msg2_" + LANGUAGE)
    note_read_msg3 = os.getenv("Notes_Read_msg3_" + LANGUAGE)
    timer_trigger = os.getenv("Timer_Trigger_" + LANGUAGE)
    timer_msg1 = os.getenv("Timer_msg1_" + LANGUAGE)
    timer_msg2 = os.getenv("Timer_msg2_" + LANGUAGE)
    timer_msg3 = os.getenv("Timer_msg3_" + LANGUAGE)
    timer_set_min = os.getenv("Timer_set_min_" + LANGUAGE)
    timer_set_sec = os.getenv("Timer_set_sec_" + LANGUAGE)
    shutdown=os.getenv("Shutdown_" + LANGUAGE)
    msg("log", f"Loaded Language {LANGUAGE}")
    msg("log", "Starting...")

    while True:
        RESULT=listen()
        if WAKEWORD in RESULT:
            FIRST_RUN = True
            try:
                warning("sound")
                #playsound("assets/activate.mp3")
            except Exception:
                ErrorCode(2)
                break
            while True:

                if joke in RESULT:
                    speek(pj.get_joke(language=JOKE_LANG))
                    break

                if clock in RESULT:
                    CLOCK=time.strftime("%H:%M")
                    speek(clock_message + CLOCK)
                    break

                if date in RESULT:
                    DATE=datetime.datetime.today()
                    speek(date_message+f"{datetime.datetime.today()}")
                    break

                if random_int_trigger in RESULT:
                    speek(random_int_min)
                    MIN=listen()
                    speek(random_int_max)
                    MAX=listen()
                    msg("log", f"{MIN}|{MAX}")
                    speek(random_int_gen)
                    try:
                        GENERATED_NUMBER=random.randint(int(MIN),int(MAX))
                        speek(random_int_is+str(GENERATED_NUMBER))
                        break
                    except Exception:
                        speek(random_int_err)
                        break

                if math_plus_trigger in RESULT:
                    speek(math_plus_main)
                    FIRST_NUMBER=listen()
                    speek(math_plus_seco)
                    SECOND_NUMBER = listen()
                    try:
                        EQUAL=(int(FIRST_NUMBER)+int(SECOND_NUMBER))
                        speek(math_plus_answ+str(EQUAL))
                        break
                    except Exception:
                        speek(f"{math_plus_err}")
                        break

                if math_minus_trigger in RESULT:
                    speek(math_plus_main)
                    FIRST_NUMBER=listen()
                    speek(math_plus_seco)
                    SECOND_NUMBER=listen()
                    try:
                        EQUAL=int(FIRST_NUMBER)-int(SECOND_NUMBER)
                        speek(math_minus_answ+str(EQUAL))
                        break
                    except Exception:
                        speek(f"{math_minus_err}")
                        break

                if wikipedia_trigger in RESULT:
                    def wp_search_func():
                        speek(SEARCH)
                    speek(wikipedia_message)
                    QUERY=listen()
                    try:
                        SEARCH=wp.summary(QUERY)
                        WP_THREAD=Thread(target=wp_search_func)
                        WP_THREAD.start()
                        break
                    except wikipedia.exceptions.PageError:
                        msg("warning", "PAGE ERROR: Couldn't load page!")
                        speek(f"{QUERY}"+wikipedia_message2)
                        break


                def note_read():
                    NOTES=[]
                    with open("notes.txt", "r") as FILE:
                        LINES=FILE.readlines()
                        for LINE in LINES:
                            NOTES.append(str(LINE.strip()))
                    if not NOTES:
                        speek(note_read_msg1)
                        speek(note_read_msg2)
                    else:
                        speek(note_read_msg3)
                        speek(LINE)

                if note_add_trigger in RESULT:
                    speek(note_add_msg1)
                    ITEM=listen()
                    with open("notes.txt", "a") as FILE:
                        FILE.write(str(ITEM) + "\n")
                        speek(note_add_msg2)
                        break

                if note_rem_trigger in RESULT:
                    note_read()
                    speek(note_rem_msg1)
                    ITEM=listen()
                    with open("notes.txt", "r") as FILE:
                        LINES=FILE.readlines()
                    with open("notes.txt", "w") as FILE:
                        REMOVED=False
                        for LINE in LINES:
                            NOTE=LINE.strip()
                            if NOTE==ITEM:
                                REMOVED=True
                            else:
                                FILE.write(line)
                    if REMOVED:
                        speek(note_rem_msg2)
                    else:
                        speek(note_rem_msg3)

                if note_read_trigger in RESULT:
                    NOTES=[]
                    with open("notes.txt", "r") as FILE:
                        LINES=FILE.readlines()
                        for LINE in LINES:
                            NOTES.append(str(LINE.strip()))
                    if not NOTES:
                        speek(note_read_msg1)
                        speek(note_read_msg2)
                    else:
                        speek(note_read_msg3)
                        speek(LINE)

                def atimer(AMOUNT,TYPE):
                    if TYPE == 'min':
                        speek(f'{timer_set_min}')
                        time.sleep(int(AMOUNT)*60)
                        ringtone()
                    elif TYPE == 'sec':
                        speek(f'{timer_set_sec}')
                        time.sleep(int(AMOUNT))
                        ringtone()
                    else:
                        ErrorCode(-1)

                if timer_trigger in RESULT:
                    speek(timer_msg1)
                    TYPE=listen()
                    if "min" in TYPE:
                        speek(timer_msg2)
                        AMOUNT=listen()
                        TIMER_THREAD=Thread(target=atimer, args=(AMOUNT, "min"))
                        TIMER_THREAD.start()
                        break
                    elif "sek" in TYPE:
                        speek(timer_msg2)
                        AMOUNT=listen()
                        TIMER_THREAD=Thread(target=atimer, args=(AMOUNT, "sec"))
                        TIMER_THREAD.start()
                    else:
                        speek(timer_msg3)
                        break

                if shutdown in RESULT:
                    msg("log", f"{shutdown}")
                    speek(shutdown)
                    time.sleep(0.3)
                    raise SystemExit

                else:
                    try:
                        warning("sound")
                        #playsound("assets/deactivate.mp3")
                        break
                    except Exception:
                        ErrorCode(2)
                        break

                FIRST_RUN = False
                RESULT=listen()
