import colorama
colorama.init(True)
from colorama import Fore, Back
def CinematicViscosity():
    try:
        print(Fore.RED+ Back.CYAN + "Cinematic Viscosity INTERPOLATION (for T(inf)):\n")
        print(Fore.RED+ Back.YELLOW + "Temperature:\n")
        B = float(input("Your Temp.: "))
        A = float(input("Temp 1: "))
        C = float(input("Temp 2: "))
        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Viscosity(mu)(liquid):\n")
        VL1 = float(eval(input("Viscosity(mu)(liquid) 1: ")))
        VL2 = float(eval(input("Viscosity(mu)(liquid) 2: ")))
        res1 = VL1 + ((B-A) * ((VL2-VL1)/(C-A)))
        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Special Volume (Liquid):\n")
        SVL1 = float(eval(input("Special Volume (Liquid) 1: ")))
        SVL2 = float(eval(input("Special Volume (Liquid) 2: ")))
        res2 = SVL1 + ((B-A) * ((SVL2-SVL1)/(C-A)))
        result = res1 * res2
        print(f"Cinematic Viscosity(nu) * 10^6 = {result}")
    except:
        print(Fore.RED + "Something went Wrong!!!!")
    