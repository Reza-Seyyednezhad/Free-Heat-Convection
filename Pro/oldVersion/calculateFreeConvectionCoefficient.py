import os
import colorama
from colorama import Fore, Back
from pyfiglet import print_figlet
from _Data import *

os.system("cls")
colorama.init(True)


class CalculateFreeConvection:
    def __init__(self, SurfaceTemp, SurroundTemp, SurfaceLength=1, cylinderDiameter=1):
        self.SurfaceTemp = float(SurfaceTemp)
        self.SurroundTemp = float(SurroundTemp)
        self.SurfaceLength = float(SurfaceLength)
        self.cylinderDiameter = float(cylinderDiameter)
        self.yourTemp = float((self.SurfaceTemp + self.SurroundTemp) / 2)
        self.myList = AirDataList
        self.myList.append(self.yourTemp)
        self.myList.sort()
        temp1 = self.myList[self.myList.index(self.yourTemp) - 1]
        temp2 = self.myList[self.myList.index(self.yourTemp) + 1]
        # Finding near numbers
        self.temp1Data = float(AirDataTemp[temp1])
        self.temp2Data = float(AirDataTemp[temp2])
        # Ro:
        ro1 = float(self.temp1Data["Ro"])
        ro2 = float(self.temp2Data["Ro"])
        self.roRes = ro1 + ((self.yourTemp - temp1) * ((ro2 - ro1) / (temp2 - temp1)))
        # Cp
        cp1 = float(self.temp1Data["Cp"])
        cp2 = float(self.temp2Data["Cp"])
        self.cpRes = cp1 + ((self.yourTemp - temp1) * ((cp2 - cp1) / (temp2 - temp1)))
        # Dynamic Viscosity
        dv1 = float(self.temp1Data["Dynamic Viscosity"])
        dv2 = float(self.temp2Data["Dynamic Viscosity"])
        self.dvRes = dv1 + ((self.yourTemp - temp1) * ((dv2 - dv1) / (temp2 - temp1)))
        # Cinematic Viscosity
        cv1 = float(self.temp1Data["Cinematic Viscosity"])
        cv2 = float(self.temp2Data["Cinematic Viscosity"])
        self.cvRes = cv1 + ((self.yourTemp - temp1) * ((cv2 - cv1) / (temp2 - temp1)))
        # Thermal conductivity(k)
        tc1 = float(self.temp1Data["Thermal conductivity(k)"])
        tc2 = float(self.temp2Data["Thermal conductivity(k)"])
        self.tcRes = tc1 + ((self.yourTemp - temp1) * ((tc2 - tc1) / (temp2 - temp1)))
        # Thermal diffusivity(Alpha)
        td1 = float(self.temp1Data["Thermal diffusivity(Alpha)"])
        td2 = float(self.temp2Data["Thermal diffusivity(Alpha)"])
        self.tdRes = td1 + ((self.yourTemp - temp1) * ((td2 - td1) / (temp2 - temp1)))
        # Pr
        pr1 = float(self.temp1Data["Pr"])
        pr2 = float(self.temp2Data["Pr"])
        self.prRes = pr1 + ((self.yourTemp - temp1) * ((pr2 - pr1) / (temp2 - temp1)))
        # Beta
        bt1 = float(1 / temp1)
        bt2 = float(1 / temp2)
        self.btRes = bt1 + ((self.yourTemp - temp1) * ((bt2 - bt1) / (temp2 - temp1)))

        def ForVerticalPlate():
            print(Fore.LIGHTBLUE_EX + "Calculation Section for Vertical Plate: \n")
            print(
                Fore.GREEN + Back.BLACK + "***************************************\n\n"
            )
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
                print(Fore.RED + key + " :\n     " + Fore.CYAN + value)
                print(
                    Fore.GREEN
                    + Back.BLACK
                    + "***************************************\n"
                )

        def ForHorizontalPlate():

            print(Fore.LIGHTBLUE_EX + "Calculation Section for Horizontal Plate: \n")
            RaRes = float(
                (
                    9.81
                    * self.btRes
                    * abs(SurfaceTemp - SurroundTemp)
                    * SurfaceLength ** 3
                )
                / (self.cvRes * self.tdRes)
            )
            print(
                Fore.GREEN + Back.BLACK + "***************************************\n\n"
            )
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

        def LongHorizontalCylinder():
            print(
                Fore.LIGHTBLUE_EX
                + "Calculation Section for Long Horizontal Cylinder: \n"
            )
            print(
                Fore.GREEN + Back.BLACK + "***************************************\n\n"
            )
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
                print(Fore.RED + key + " :\n     " + Fore.CYAN + value)
                print(
                    Fore.GREEN
                    + Back.BLACK
                    + "***************************************\n"
                )
