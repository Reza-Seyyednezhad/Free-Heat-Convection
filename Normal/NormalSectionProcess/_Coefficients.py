import colorama
colorama.init(True)
from colorama import Fore, Back
import os
from pyfiglet import print_figlet
os.system('cls')

# Grashof Number
def Gr():
    try:
        os.system('cls')
        print_figlet("Grashof Number")
        print(Fore.CYAN + "Attention: Mathematical power is: { ** }")
        surfaceTemp = float(input("Surface Temp.(K): "))
        fluidTemp = float(input("Fluid Temp.(K): "))
        Beta = float(eval(input("Beta(1/K): ")))
        surfaceLength = float(input("Surface Length(m) or Diameter(m): "))
        CinematicViscosity = float(eval(input("Cinematic Viscosity(nu): ")))
        res = float((9.81 * Beta * abs(surfaceTemp - fluidTemp) *(surfaceLength**3))/(CinematicViscosity**2))
        print(Fore.BLACK + Back.YELLOW + f"Grashof Number is: {res}")
    except :
        print(Fore.RED + "Something went Wrong!!!!")

# Rayleigh Number

def Ra():
    try:
        os.system('cls')
        print_figlet("Rayleigh Number")
        print(Fore.CYAN + "Attention: Mathematical power is: { ** }")
        surfaceTemp = float(input("Surface Temp.(K): ")) 
        fluidTemp = float(input("Fluid Temp.(K): ")) 
        Beta = float(eval(input("Beta(1/K): ")))
        surfaceLength = float(input("Surface Length(m) or Diameter(m): "))
        CinematicViscosity = float(eval(input("Cinematic Viscosity(nu): ")))
        alpha = float(eval(input("Alpha: "))) 
        res = float((9.81 * Beta * abs(surfaceTemp - fluidTemp) *(surfaceLength**3))/(CinematicViscosity * alpha))
        print(Fore.BLACK + Back.YELLOW + f"Rayleigh Number is: {res}")
    except :
        print(Fore.RED + "Something went Wrong!!!!")


#  Nusselt number for Vertical surface
def Nu():
    try:
        os.system('cls')
        print_figlet("Nusselt Number")
        print(Fore.CYAN + "Attention: Mathematical power is: { ** }")
        surfaceTemp = float(input("Surface Temp.(K): ")) 
        fluidTemp = float(input("Fluid Temp.(K): ")) 
        Beta = float(eval(input("Beta(1/K): ")))
        surfaceLength = float(input("Surface Length(m) or Diameter(m): "))
        CinematicViscosity = float(eval(input("Cinematic Viscosity(nu): ")))
        alpha = float(eval(input("Alpha: ")))
        Pr = float(input("Pr : ")) 
        ra = float((9.81 * Beta * abs(surfaceTemp - fluidTemp) *(surfaceLength**3))/(CinematicViscosity * alpha))
        res = float((0.825 + ((0.387 * ra**(1/6))/((1 + (0.492/Pr)**(9/16))**(8/27))))**2)
        print(Fore.BLACK + Back.YELLOW + f"Nusselt Number is: {res}")
    except :
        print(Fore.RED + "Something went Wrong!!!!")

