import colorama
colorama.init(True)
from colorama import Fore, Back
import os
from pyfiglet import print_figlet
os.system('cls')


def avarageHeatTransfer():
    try:
        os.system('cls')
        print_figlet("Avarage Heat Transfer Coefficient")
        print(Fore.CYAN + "Attention: Mathematical power is: { ** }")
        surfaceTemp = float(input("Surface Temp.(K): ")) 
        fluidTemp = float(input("Fluid Temp.(K): ")) 
        Beta = float(eval(input("Beta(1/K): ")))
        surfaceLength = float(input("Surface Length(m) or Diameter(m): "))
        CinematicViscosity = float(eval(input("Cinematic Viscosity(nu): ")))
        alpha = float(eval(input("Alpha: ")))
        Pr = float(input("Pr: "))
        k = float(eval(input("k: "))) 
        ra = float((9.81 * Beta * (surfaceTemp - fluidTemp) *(surfaceLength**3))/(CinematicViscosity * alpha))
        nu = float((0.825 + ((0.387 * ra**(1/6))/((1 + (0.492/Pr)**(9/16))**(8/27))))**2)
        res = float(nu * k / surfaceLength)
        print(Fore.BLUE + "********************************")
        print(Fore.BLACK + Back.YELLOW + f"Avarage Heat Transfer Coefficient is: {res}")
        print(Fore.BLUE + "********************************")
    except :
        print(Fore.RED + "Something went Wrong!!!!")