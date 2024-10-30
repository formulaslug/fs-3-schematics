# import numpy as np
import math

rValues = [1,1.2,1.5,1.8,2.2,2.7,3.3,3.9,4.7,5.6,6.8,8.2,10,12,15,18,22,27,33,39,47,56,68,82,100]

def rTor (resistor1, resistor2):
    return resistor2/(resistor1+resistor2)

def error (ratio, rVals):
    return abs((ratio) - rTor(rVals[0],rVals[1]))/ratio

def roundRatio (value, top = 0):
    # print(f"top: {top}")
    if value < 0.01:
        roundedValue = roundRatio(value*10, top + 1)
        if top == 0:
            decimals = math.log(round(roundedValue/value),10)
            number = roundedValue
            return(decimals, number)
        else:
            return roundedValue
    else:
        if top == 0:
            decimals = 0.0
            number = value
            return(decimals, number)
        else:
            return value
    
def find (input, output):
    ratio = output/input
    decimals, ratio = roundRatio(ratio)
    print(f"decimals: {decimals}, ratio: {ratio}")
    storage = (1,1)
    errorVar = error(ratio, storage)
    for vA in rValues:
        for vB in rValues:
            # print(f"checking vA: {vA} and vB: {vB} with ratio {rTor(vA,vB)}")
            # print(f"diff: {error(ratio, (vA, vB))}, storage: {error(ratio, storage)}")
            if error(ratio, (vA, vB)) < error(ratio, storage):
                errorVar = error(ratio, (vA, vB))
                storage = (vA,vB)
            # print(vA,vB)
    storageOut = (storage[0] * 100**decimals, storage[1])
    print(f"R1: {storageOut[0]}, R2: {storageOut[1]}, Error%: {round(errorVar,3)}")
    return storageOut, errorVar


Vin = float(input("Vin?     "))
Vout = float(input("Vout?     "))
find(Vin, Vout)

