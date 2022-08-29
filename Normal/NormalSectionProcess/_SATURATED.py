import colorama
colorama.init(True)
from colorama import Fore, Back
def SaturatedINTERPOLATION():
    try:
        print(Fore.RED+ Back.CYAN + "SATURATED INTERPOLATION:\n")
        print(Fore.RED+ Back.YELLOW + "Temperature:\n")
        B = float(input("Your Temp.: "))
        A = float(input("Temp 1: "))
        C = float(input("Temp 2: "))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pressure:\n")
        P1 = float(input("Pressure 1: "))
        P2 = float(input("Pressure 2: "))
        res1 = P1 + ((B-A) * ((P2-P1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Ro:\n")
        ro1 = float(input("Ro 1: "))
        ro2 = float(input("Ro 2: "))
        res2 = ro1 + ((B-A) * ((ro2-ro1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Special Volume (Liquid):\n")
        SVL1 = float(eval(input("Special Volume (Liquid) 1: ")))
        SVL2 = float(eval(input("Special Volume (Liquid) 2: ")))
        res3 = SVL1 + ((B-A) * ((SVL2-SVL1)/(C-A)))

        
        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Special Volume (Vapor):\n")
        SVV1 = float(input("Special Volume (Vapor) 1: "))
        SVV2 = float(input("Special Volume (Vapor) 2: "))
        res4 = SVV1 + ((B-A) * ((SVV2-SVV1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "h(fg):\n")
        HF1 = float(input("h(fg) 1: "))
        HF2 = float(input("h(fg) 2: "))
        res5 = HF1 + ((B-A) * ((HF2-HF1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "k(liquid):\n")
        KL1 = float(eval(input("k(liquid) 1: ")))
        KL2 = float(eval(input("k(liquid) 2: ")))
        res6 = KL1 + ((B-A) * ((KL2-KL1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "k(vapor):\n")
        KV1 = float(eval(input("k(vapor) 1: ")))
        KV2 = float(eval(input("k(vapor) 2: ")))
        res7 = KV1 + ((B-A) * ((KV2-KV1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pr(liquid):\n")
        PrL1 = float(input("Pr(liquid) 1: "))
        PrL2 = float(input("Pr(liquid) 2: "))
        res8 = PrL1 + ((B-A) * ((PrL2-PrL1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Pr(vapor):\n")
        PrV1 = float(input("Pr(vapor) 1: "))
        PrV2 = float(input("Pr(vapor) 2: "))
        res9 = PrV1 + ((B-A) * ((PrV2-PrV1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "sigma:\n")
        Sigma1 = float(eval(input("sigma 1: ")))
        Sigma2 = float(eval(input("sigma 2: ")))
        res10 = Sigma1 + ((B-A) * ((Sigma2-Sigma1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        print(Fore.RED+ Back.YELLOW + "Beta:\n")
        Beta1 = float(eval(input("Beta1 (1/K): ")))
        Beta2 = float(eval(input("Beta 2(1/K): ")))
        res11 = Beta1 + ((B-A) * ((Beta2-Beta1)/(C-A)))

        print(Fore.GREEN+ Back.BLACK + "***************************************")
        msg = str(input("Do you want to see [Cp and Viscosity]: "))
        if msg in ['yes', 'y', '1']:
            print(Fore.RED+ Back.YELLOW + "C(p)(liquid):\n")
            CPL1 = float(input("C(p)(liquid) 1: "))
            CPL2 = float(input("C(p)(liquid) 2: "))
            res12 = CPL1 + ((B-A) * ((CPL2-CPL1)/(C-A)))

            print(Fore.GREEN+ Back.BLACK + "***************************************")
            print(Fore.RED+ Back.YELLOW + "C(p)(Vapor):\n")
            CPV1 = float(input("C(p)(Vapor) 1: "))
            CPV2 = float(input("C(p)(Vapor) 2: "))
            res13 = CPV1 + ((B-A) * ((CPV2-CPV1)/(C-A)))

            print(Fore.GREEN+ Back.BLACK + "***************************************")
            print(Fore.RED+ Back.YELLOW + "Viscosity(mu)(liquid):\n")
            VL1 = float(eval(input("Viscosity(mu)(liquid) 1: ")))
            VL2 = float(eval(input("Viscosity(mu)(liquid) 2: ")))
            res14 = VL1 + ((B-A) * ((VL2-VL1)/(C-A)))

            print(Fore.GREEN+ Back.BLACK + "***************************************")
            print(Fore.RED+ Back.YELLOW + "Viscosity(mu)(vapor):\n")
            VV1 = float(eval(input("Viscosity(mu)(vapor) 1: ")))
            VV2 = float(eval(input("Viscosity(mu)(vapor) 2: ")))
            res15 = VV1 + ((B-A) * ((VV2-VV1)/(C-A)))

            print(Fore.GREEN+ Back.BLACK + "***************************************")
            print(Fore.GREEN+ Back.BLACK + "***************************************")
            print(Fore.GREEN+ Back.BLACK + "***************************************")

            Results = {
                "temp.": B,
                "pressure": res1,
                "Ro": res2,
                "Special Volume (Liquid)": res3,
                "Special Volume (Vapor)": res4,
                "h(fg)": res5,
                "k(liquid)": res6,
                "k(Vapor)": res7,
                "Pr(liquid)": res8,
                "Pr(Vapor)": res9,
                "sigma": res10,
                "Beta": res11,
                "C(p)(liquid)": res12,
                "C(p)(Vapor)": res13,
                "Viscosity(mu)(liquid)": res14,
                "Viscosity(mu)(vapor)": res15
            }
        else:
            Results = {
                "temp.": B,
                "pressure": res1,
                "Ro": res2,
                "Special Volume (Liquid)": res3,
                "Special Volume (Vapor)": res4,
                "h(fg)": res5,
                "k(liquid)": res6,
                "k(Vapor)": res7,
                "Pr(liquid)": res8,
                "Pr(Vapor)": res9,
                "sigma": res10,
                "Beta": res11
            }

        for key, value in Results.items():
            print(f"{key}:{value} \n")
            print(Fore.YELLOW+ Back.BLACK + "------------------ \n")
    except :
        print(Fore.RED + "Something went Wrong!!!!")

