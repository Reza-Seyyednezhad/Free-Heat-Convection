import colorama
from ._Data import *
import os
from colorama import init, Fore, Back
init(True)
def FunctionName(yourTemp):
    os.system('cls')
    myList = AirDataList
    myDict = AirDataTemp
    myList.append(yourTemp)
    myList.sort()
    # Finding near numbers
    temp1 = myList[myList.index(yourTemp) - 1]
    temp2 = myList[myList.index(yourTemp) + 1]
    # Finding near numbers info
    temp1Data = myDict[temp1]
    temp2Data = myDict[temp2]
    # Ro:
    ro1 = float(temp1Data["Ro"])
    ro2 = float(temp2Data["Ro"])
    roRes = ro1 + ((yourTemp - temp1) * ((ro2 - ro1) / (temp2 - temp1)))
    # Cp
    cp1 = float(temp1Data["Cp"])
    cp2 = float(temp2Data["Cp"])
    cpRes = cp1 + ((yourTemp - temp1) * ((cp2 - cp1) / (temp2 - temp1)))
    # Dynamic Viscosity
    dv1 = float(temp1Data["Dynamic Viscosity"])
    dv2 = float(temp2Data["Dynamic Viscosity"])
    dvRes = dv1 + ((yourTemp - temp1) * ((dv2 - dv1) / (temp2 - temp1)))
    # Cinematic Viscosity
    cv1 = float(temp1Data["Cinematic Viscosity"])
    cv2 = float(temp2Data["Cinematic Viscosity"])
    cvRes = cv1 + ((yourTemp - temp1) * ((cv2 - cv1) / (temp2 - temp1)))
    # Thermal conductivity(k)
    tc1 = float(temp1Data["Thermal conductivity(k)"])
    tc2 = float(temp2Data["Thermal conductivity(k)"])
    tcRes = tc1 + ((yourTemp - temp1) * ((tc2 - tc1) / (temp2 - temp1)))
    # Thermal diffusivity(Alpha)
    td1 = float(temp1Data["Thermal diffusivity(Alpha)"])
    td2 = float(temp2Data["Thermal diffusivity(Alpha)"])
    tdRes = td1 + ((yourTemp - temp1) * ((td2 - td1) / (temp2 - temp1)))
    # Pr
    pr1 = float(temp1Data["Pr"])
    pr2 = float(temp2Data["Pr"])
    prRes = pr1 + ((yourTemp - temp1) * ((pr2 - pr1) / (temp2 - temp1)))
    # Beta
    bt1 = float(1 / temp1)
    bt2 = float(1 / temp2)
    btRes = bt1 + ((yourTemp - temp1) * ((bt2 - bt1) / (temp2 - temp1)))

    res = {
        "roRes": roRes,
        "cpRes": cpRes,
        "MU": dvRes,
        "NU": cvRes,
        "K": tcRes,
        "ALPHA": tdRes,
        "prRes": prRes,
        "BETA": btRes
    }
    for key, value in res.items():
        print(Fore.RED + f"{key}:\n")
        print(Fore.CYAN + f"    {value}")
        print(Fore.GREEN + Back.BLACK + "***************************************\n")

FunctionName(288.15)