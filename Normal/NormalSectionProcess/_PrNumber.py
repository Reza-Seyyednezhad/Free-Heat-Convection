import colorama
colorama.init(True)
from colorama import Fore, Back

def PrNumber():
    try:
        print(Fore.RED+ Back.CYAN + "Pr Number INTERPOLATION (For Ts):\n")
        print(Fore.RED+ Back.YELLOW + "Temperature:\n")
        B = float(input("Your Temp.: "))
        A = float(input("Temp 1: "))
        C = float(input("Temp 2: "))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pr(liquid):\n")
        PrL1 = float(input("Pr(liquid) 1: "))
        PrL2 = float(input("Pr(liquid) 2: "))
        res1 = PrL1 + ((B-A) * ((PrL2-PrL1)/(C-A)))
        print(f"Pr(Liquid): {res1}")
        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pr(vapor):\n")
        PrV1 = float(input("Pr(vapor) 1: "))
        PrV2 = float(input("Pr(vapor) 2: "))
        res2 = PrV1 + ((B-A) * ((PrV2-PrV1)/(C-A)))
        print(f"Pr(vapor): {res2}")
        print(Fore.GREEN+ Back.BLACK + "***************************************")
    except:
        print(Fore.RED + "Something went Wrong!!!!")
    