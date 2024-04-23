import colorama
from dotenv import load_dotenv
import os
colorama.init(autoreset=True)
load_dotenv("conf/pylog.env")
PREFIX=os.getenv("PREFIX")
CREDITS=os.getenv("skip_credits")
if CREDITS == "y" or CREDITS == "yes" or CREDITS == "true" or CREDITS == "True":
    pass
else:
     print(colorama.Fore.WHITE+"Thanks for using PyLog")
     print(colorama.Fore.WHITE+"by DDavid701 for Saphire")

def msg(type,content):
    if type=="log":
        print(colorama.Fore.GREEN + PREFIX + colorama.Fore.LIGHTBLACK_EX + " × " + colorama.Fore.LIGHTWHITE_EX + content)
    elif type=="error":
        print(colorama.Fore.GREEN+PREFIX+colorama.Fore.LIGHTBLACK_EX+" × "+colorama.Fore.LIGHTRED_EX+content)
    elif type=="warning":
        print(colorama.Fore.GREEN + PREFIX + colorama.Fore.LIGHTBLACK_EX + " × " + colorama.Fore.LIGHTYELLOW_EX + content)
    else:
        print(colorama.Fore.GREEN + PREFIX + colorama.Fore.LIGHTBLACK_EX + " × " + colorama.Fore.RED + "Couldn't recognise message type! " + colorama.Fore.WHITE + "(" + colorama.Fore.LIGHTRED_EX+type+colorama.Fore.WHITE+")")