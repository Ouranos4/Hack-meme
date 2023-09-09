from colorama import Fore, Back, Style, init
from playsound import playsound
import threading
import time
password = int(input("Enter password: "))
first="██╗   ██╗  █████╗  ██╗   ██╗  ██╗  ██╗  █████╗   █████╗  ██╗  ██╗ ███████╗ ██████╗   ███╗  ██╗ █████╗  ██████╗ █████╗"
secon="╚██╗ ██╔╝ ██╔══██╗ ██║   ██║  ██║  ██║ ██╔══██╗ ██╔══██╗ ██║ ██╔╝ ██╔════╝ ██╔══██╗  ████╗ ██║██╔══██╗██╔════╝██╔══██╗"
thirt=" ╚████╔╝  ██║  ██║ ██║   ██║  ███████║ ███████║ ██║  ╚═╝ █████═╝  █████╗   ██║  ██║  ██╔██╗██║███████║╚█████╗ ███████║"
fourt="  ╚██╔╝   ██║  ██║ ██║   ██║  ██╔══██║ ██╔══██║ ██║  ██╗ ██╔═██╗  ██╔══╝   ██║  ██║  ██║╚████║██╔══██║ ╚═══██╗██╔══██║"
fifth="   ██║    ╚█████╔╝ ╚██████╔╝  ██║  ██║ ██║  ██ ║╚█████╔╝ ██║ ╚██╗ ███████╗ ██████╔╝  ██║ ╚███║██║  ██║██████╔╝██║  ██║"
sixth="   ╚═╝     ╚════╝   ╚═════╝   ╚═╝  ╚═╝ ╚═╝  ╚═╝  ╚════╝  ╚═╝  ╚═╝ ╚══════╝ ╚═════╝   ╚═╝  ╚══╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝"

def play_audio():
    playsound("Hyper Spoiler ! Cyberpunk 2077 ! BGM.mp3")
if password==12345678:
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()
    time.sleep(0.5)
    print(
    Fore.GREEN + first)
    print(
    Fore.GREEN + secon)
    print(
    Fore.GREEN + thirt)
    print(
    Fore.GREEN+ fourt)
    print(
    Fore.GREEN + fifth)
    print(
    Fore.GREEN + sixth)
else:
    print("Password is false")