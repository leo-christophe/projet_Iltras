import keyboard
from colorama import Fore, Style
def wait_spacebar():
    print(Style.BRIGHT)
    print(Fore.RED + "Appuyez sur la touche espace pour continuer...")
    print(Style.RESET_ALL)
    print(">...")
    keyboard.wait('spacebar')

