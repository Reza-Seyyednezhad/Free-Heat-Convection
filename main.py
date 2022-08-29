import os
import colorama
colorama.init(True)
from colorama import Fore, Back
from  Normal.NormalSectionProcess._intro import *
from Normal.NormalSectionProcess._SATURATED import *
from Normal.NormalSectionProcess._NORMAL import *
from Normal.NormalSectionProcess._CinematicViscosity import *
from Normal.NormalSectionProcess._PrNumber import *
from Normal.NormalSectionProcess._Coefficients import *
from Normal.NormalSectionProcess._AvarageHeatTransfer import *
from pyfiglet import print_figlet

os.system('cls')
print_figlet("Interpolation")
print(Fore.GREEN+ Back.BLACK + "***************************************")
# Introduction

try:
    Intro()
    select = int(input("    Which => "))
    if select == 1:
        SaturatedINTERPOLATION()
    elif select == 2:
        NormalINTERPOLATION()
    elif select == 3:
        PrNumber()
    elif select == 4:
        CinematicViscosity()
    elif select == 5:
        FreeHeatTransfer()
        text = int(input('    Which => '))
        if text == 1:
            Gr()
        elif text == 2:
            Ra()
        elif text == 3:
            Nu()
        elif text == 4:
            avarageHeatTransfer()
        else:
            print(Fore.RED + "Something went Wrong!!!!")
    else:
        print(Fore.RED + "Something went Wrong!!!!")
except :
    print(Fore.RED + "Something went Wrong!!!!")
