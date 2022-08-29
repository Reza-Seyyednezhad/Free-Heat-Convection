import os
os.system('python -m pip install colorama  pyfiglet')
import colorama
from colorama import Fore, Back
from pyfiglet import print_figlet
from calculateFreeConvectionCoefficient import IntroSection
os.system("cls")
colorama.init(True)

print_figlet("Pro")
print(Fore.GREEN + Back.BLACK + "***************************************")
IntroSection()