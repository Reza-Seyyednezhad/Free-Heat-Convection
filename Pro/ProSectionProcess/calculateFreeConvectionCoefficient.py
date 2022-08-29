import os
import colorama
from colorama import Fore, Back
from pyfiglet import print_figlet
from ...Normal.NormalSectionProcess._Data import *

os.system("cls")
colorama.init(True)


class CalculateFreeConvection:
    def __init__(self, SurfaceTemp, SurroundTemp, SurfaceLength=1, cylinderDiameter=1):
        self.SurfaceTemp = float(SurfaceTemp)
        self.SurroundTemp = float(SurroundTemp)
        self.SurfaceLength = float(SurfaceLength)
        self.cylinderDiameter = float(cylinderDiameter)
        self.yourTemp = float((self.SurfaceTemp + self.SurroundTemp) / 2)
        myList = AirDataList
        myDict = AirDataTemp
        myList.append(self.yourTemp)
        myList.sort()
        # Finding near numbers
        temp1 = myList[myList.index(self.yourTemp) - 1]
        temp2 = myList[myList.index(self.yourTemp) + 1]
        # Finding near numbers info
        temp1Data = myDict[temp1]
        temp2Data = myDict[temp2]
        # Ro:
        ro1 = float(temp1Data["Ro"])
        ro2 = float(temp2Data["Ro"])
        self.roRes = ro1 + ((self.yourTemp - temp1) * ((ro2 - ro1) / (temp2 - temp1)))
        # Cp
        cp1 = float(temp1Data["Cp"])
        cp2 = float(temp2Data["Cp"])
        self.cpRes = cp1 + ((self.yourTemp - temp1) * ((cp2 - cp1) / (temp2 - temp1)))
        # Dynamic Viscosity
        dv1 = float(temp1Data["Dynamic Viscosity"])
        dv2 = float(temp2Data["Dynamic Viscosity"])
        self.dvRes = dv1 + ((self.yourTemp - temp1) * ((dv2 - dv1) / (temp2 - temp1)))
        # Cinematic Viscosity
        cv1 = float(temp1Data["Cinematic Viscosity"])
        cv2 = float(temp2Data["Cinematic Viscosity"])
        self.cvRes = cv1 + ((self.yourTemp - temp1) * ((cv2 - cv1) / (temp2 - temp1)))
        # Thermal conductivity(k)
        tc1 = float(temp1Data["Thermal conductivity(k)"])
        tc2 = float(temp2Data["Thermal conductivity(k)"])
        self.tcRes = tc1 + ((self.yourTemp - temp1) * ((tc2 - tc1) / (temp2 - temp1)))
        # Thermal diffusivity(Alpha)
        td1 = float(temp1Data["Thermal diffusivity(Alpha)"])
        td2 = float(temp2Data["Thermal diffusivity(Alpha)"])
        self.tdRes = td1 + ((self.yourTemp - temp1) * ((td2 - td1) / (temp2 - temp1)))
        # Pr
        pr1 = float(temp1Data["Pr"])
        pr2 = float(temp2Data["Pr"])
        self.prRes = pr1 + ((self.yourTemp - temp1) * ((pr2 - pr1) / (temp2 - temp1)))
        # Beta
        bt1 = float(1 / temp1)
        bt2 = float(1 / temp2)
        self.btRes = bt1 + ((self.yourTemp - temp1) * ((bt2 - bt1) / (temp2 - temp1)))



    def getInfo(self):
        os.system("cls")
        try:
            res = {
                "Ro": self.roRes,
                "Cp": self.cpRes,
                "mu": self.dvRes,
                "nu(Cinematic Viscosity)": self.cvRes,
                "K": self.tcRes,
                "ALPHA": self.tdRes,
                "Pr": self.prRes,
                "BETA": self.btRes,
            }
            for key, value in res.items():
                print(Fore.RED + f"{key}:\n")
                print(Fore.CYAN + f"    {value}")
                print(Fore.GREEN + Back.BLACK + "***************************************\n")
        except:
            print(Fore.RED + "Something went wrong.")


    def ForVerticalPlate(self):
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Calculation Section for Vertical Plate: \n")
        print(Fore.GREEN + Back.BLACK + "***************************************\n\n")
        try:
            GrRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(self.SurfaceTemp - self.SurroundTemp)
                    * self.SurfaceLength ** 3
                )
                / (self.cvRes ** 2)
            )
            RaRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(self.SurfaceTemp - self.SurroundTemp)
                    * self.SurfaceLength ** 3
                )
                / (self.cvRes * self.tdRes)
            )
            NuRes = float(
                (
                    0.825
                    + (
                        (0.387 * RaRes ** (1 / 6))
                        / ((1 + (0.492 / self.prRes) ** (9 / 16)) ** (8 / 27))
                    )
                )
                ** 2
            )
            # h
            HRes = float(NuRes * self.tcRes / self.SurfaceLength)
            Result = {"Gr": GrRes, "Ra": RaRes, "Nu": NuRes, "h(W/K.m**2)": HRes}

            for key, value in Result.items():
                print(Fore.RED + f"{key}:\n")
                print(Fore.CYAN + f"    {value}")
                print(Fore.GREEN + Back.BLACK + "***************************************\n")
        except :
            print(Fore.RED + "Something went wrong.")
        

    def ForHorizontalPlate(self):
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Calculation Section for Horizontal Plate: \n")
        try:
            RaRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(self.SurfaceTemp - self.SurroundTemp)
                    * self.SurfaceLength ** 3
                )
                / (self.cvRes * self.tdRes)
            )
            print(Fore.GREEN + Back.BLACK + "***************************************\n\n")
            print("Bottom Plate is:\n   1) Cold(c)\n    2) Hot(h)")
            ColdOrHot = str(input("         Which: "))
            if ColdOrHot.lower() == "c" or int(ColdOrHot) == 1:
                if RaRes in range(10 ** 4, 10 ** 7):
                    NuHPC = float(0.54 * (RaRes ** 0.25))
                elif RaRes in range(10 ** 7, 10 ** 11):
                    NuHPC = float(0.15 * (RaRes ** (1 / 3)))
                else:
                    print("Ra out of ranged :(")

                print(Fore.LIGHTBLUE_EX + "Nu:\n")
                print(Fore.YELLOW + Back.BLACK + f"     {NuHPC}\n")

                # h for Horizontal Plate when bottom surface is COLD.
                print(
                    Fore.LIGHTBLUE_EX
                    + "h(W/K.m**2) for Horizontal Plate when bottom surface is COLD:\n"
                )
                HResC = float(NuHPC * self.tcRes / self.SurfaceLength)
                print(Fore.YELLOW + Back.BLACK + f"     {HResC}\n")

            elif ColdOrHot.lower == "h" or int(ColdOrHot) == 2:
                if RaRes in range(10 ** 5, 10 ** 10):
                    NuHPH = float(0.27 * (RaRes ** 0.25))
                else:
                    print("Ra out of ranged :(")

                print(Fore.LIGHTBLUE_EX + "Nu:\n")
                print(Fore.YELLOW + Back.BLACK + f"     {NuHPH}\n")

                # h for Horizontal Plate when bottom surface is COLD.
                print(
                    Fore.LIGHTBLUE_EX
                    + "     h(W/K.m**2) for Horizontal Plate when bottom surface is HOT:\n"
                )
                HResH = float(NuHPH * self.tcRes / self.SurfaceLength)
                print(Fore.YELLOW + Back.BLACK + f"     {HResH}\n")

            else:
                print(Fore.RED + "Something went Wrong!!!!")
        except:
            print(Fore.RED + "Something went wrong.")
        


    def LongHorizontalCylinder(self):
        os.system("cls")
        print(
            Fore.LIGHTBLUE_EX + "Calculation Section for Long Horizontal Cylinder: \n"
        )
        print(Fore.GREEN + Back.BLACK + "***************************************\n\n")
        try:
            GrRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(self.SurfaceTemp - self.SurroundTemp)
                    * self.cylinderDiameter ** 3
                )
                / (self.cvRes ** 2)
            )
            RaRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(self.SurfaceTemp - self.SurroundTemp)
                    * self.cylinderDiameter ** 3
                )
                / (self.cvRes * self.tdRes)
            )
            NuRes = float(
                (
                    0.6
                    + (
                        (0.387 * RaRes ** (1 / 6))
                        / ((1 + (0.559 / self.prRes) ** (9 / 16)) ** (8 / 27))
                    )
                )
                ** 2
            )
            # h
            HRes = float(NuRes * self.tcRes / self.cylinderDiameter)
            Result = {"Gr": GrRes, "Ra": RaRes, "Nu": NuRes, "h(W/K.m**2)": HRes}

            for key, value in Result.items():
                print(Fore.RED + f"{key}:\n")
                print(Fore.CYAN + f"    {value}")
                print(Fore.GREEN + Back.BLACK + "***************************************\n")
        except:
            print(Fore.RED + "Something went wrong.")
        

def IntroSection():
    print_figlet('Calculate Free Convection')
    # SurfaceTemp, SurroundTemp, SurfaceLength=1, cylinderDiameter=1
    try:
        SurfaceTempInput = float(input("Enter Surface Temprature: "))
        SurroundTempInput = float(input("Enter Surround Temprature: "))
        SurfaceLengthInput = float(input("Enter Surface Length (default: 1): "))
        cylinderDiameterInput = float(input("Enter Cylinder Length (default: 1): "))
        myObj = CalculateFreeConvection(SurfaceTempInput, SurroundTempInput, SurfaceLengthInput, cylinderDiameterInput)
        txt = """
        Which One:\n
            1. Get Info\n
            2. Vertical Plate\n
            3. Horizontal Plate\n
            4. Long Horizontal Cylinder\n
            5. All...\n
        """
        userInput = int(input(txt + "   (1 or 2 or 3 or 4 or 5): "))
        if userInput == 1:
            myObj.getInfo()
        elif userInput == 2:
            myObj.ForVerticalPlate()
        elif userInput == 3:
            myObj.ForHorizontalPlate()
        elif userInput == 4:
            myObj.LongHorizontalCylinder()
        elif userInput == 5:
            print(Fore.CYAN + "Info:\n  ")
            print(myObj.getInfo())
            print("*    *   *   *   *")
            print(Fore.CYAN + "Vertical Plate:\n  ")
            print(myObj.ForVerticalPlate())
            print("*    *   *   *   *")
            print(Fore.CYAN + "Horizontal Plate:\n  ")
            print(myObj.ForHorizontalPlate())
            print("*    *   *   *   *")
            print(Fore.CYAN + "Long Horizontal Cylinder:\n  ")
            print(myObj.LongHorizontalCylinder())
            print("*    *   *   *   *")
            

    except:
        print('Something went wrong.')

