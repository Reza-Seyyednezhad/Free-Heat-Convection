import colorama
colorama.init(True)
from colorama import Fore, Back

def NormalINTERPOLATION():
    try:
        print(Fore.RED+ Back.CYAN + "NORMAL INTERPOLATION:\n")
        print(Fore.RED+ Back.YELLOW + "Temperature:\n")
        B = float(input("Your Temp.: "))
        A = float(input("Temp 1: "))
        C = float(input("Temp 2: "))

        print(Fore.GREEN+ Back.BLACK + "***************************************")

        print(Fore.RED+ Back.YELLOW + "Ro:\n")
        ro1 = float(input("Ro 1: "))
        ro2 = float(input("Ro 2: "))
        res1 = ro1 + ((B-A) * ((ro2-ro1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "C(p):\n")
        CP1 = float(input("C(p) 1: "))
        CP2 = float(input("C(p) 2: "))
        res2 = CP1 + ((B-A) * ((CP2-CP1)/(C-A)))

        res3 = float(1/res2)

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Dynamic Viscosity(mu):\n")
        DV1 = float(eval(input("Dynamic Viscosity(mu) 1: ")))
        DV2 = float(eval(input("Dynamic Viscosity(mu) 2: ")))
        res4 = DV1 + ((B-A) * ((DV2-DV1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Cinematic Viscosity(nu):\n")
        CV1 = float(eval(input("Cinematic Viscosity(nu) 1: ")))
        CV2 = float(eval(input("Cinematic Viscosity(nu) 2: ")))
        res5 = CV1 + ((B-A) * ((CV2-CV1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "k:\n")
        K1 = float(eval(input("k 1: ")))
        K2 = float(eval(input("k 2: ")))
        res6 = K1 + ((B-A) * ((K2-K1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Alpha:\n")
        alpha1 = float(eval(input("Alpha 1: ")))
        alpha2 = float(eval(input("Alpha 2: ")))
        res7 = alpha1 + ((B-A) * ((alpha2-alpha1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pr:\n")
        Pr1 = float(input("Pr 1: "))
        Pr2 = float(input("Pr 2: "))
        res8 = Pr1 + ((B-A) * ((Pr2-Pr1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Beta:\n")
        res9 = float(1/B)
        print(Fore.GREEN+ Back.BLACK + "***************************************")


        Results = {
            "temp.": B,
            "Ro": res1,
            "C(p)": res2,
            "Special Volume (1/Ro) ": res3,
            "Dynamic Viscosity(mu)": res4,
            "Cinematic Viscosity(nu)": res5,
            "k": res6,
            "Alpha": res7,
            "Pr": res8,
            "Beta": res9
        }

        for key, value in Results.items():
            print(f"{key}: {value} \n")
            print(Fore.YELLOW+ Back.BLACK + "------------------ \n")
    except:
        print(Fore.RED + "Something went Wrong!!!!")
    