import colorama
colorama.init(True)
from colorama import Fore, Back
import os

def Intro():
    text = """
    INTERPOLATION:\n        
        1) SATURATED INTERPOLATION \n        
        2) NORMAL INTERPOLATION \n        
        3) Pr NUMBER INTERPOLATION\n        
        4) Cinematic Viscosity INTERPOLATION\n\n
    Free Displacement Heat Coefficient Calculations \n
        5) Coefficient to calculate \n
    """
    print(Fore.YELLOW + text)

def FreeHeatTransfer():
    os.system('cls')
    newText = """
        1) Gr \n
        2) Ra \n
        3) Nu \n
        4) Avarage Heat Transfer Coefficient
    """
    print(Fore.YELLOW + newText)