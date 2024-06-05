"""Python libs"""
from time import sleep
"""Project libs"""
from functions.mkDir import mkDir
from functions.classChara import *
from functions.checkID import checkID

CharaList = []

userInput = str(input("Drop your image here, or press q to continue: "))
while(userInput != "q" and userInput != ""):
    #create character
    #imagePath = userInput[3:len(userInput)-1]
    imagePath = userInput
    nameStr = input("Character Name: ")

    ID = input("Please enter a character ID(ID should be exact 4 numbers): ")
    while not checkID(ID):
        ID = input("Please enter a correct character ID(ID should be exact 4 NUMBER): ")
    pngCount = 1
    name = str(nameStr)
    nameStr = Chara(name, ID, imagePath)

    #create transform (within character)
    transFromInput = input("Would you plan to add transform to your character? (y/n): ")
    while(transFromInput != "n" and pngCount < 9 and transFromInput != ""):
        pngInput = str(input("Drop your image here to add a transform, or press q to exit: "))
        if pngInput == "q" or pngInput == "":
            break

        #pngPath = pngInput[3:len(userInput)-1]
        pngPath = pngInput
        nameStr.addPng(pngPath)
        transformName = input("Transform Name, leave it empty if you want to use default name:")
        if transformName != "":
            nameStr.addNameStr(transformName)
        else:
            nameStr.addNameStr(name)
        pngCount += 1
        if pngCount == 9:
            print("Meet the maximum transform number.")
            break
        #transFromInput = input("Would you plan to add more transform to your character? (y/n): ")

    CharaList.append(nameStr)
    print()
    userInput = str(input("Drop your image here to create a new character, or press q to continue: "))

mkDir()

for i in CharaList:
    i.xmlEdit()
    i.ToDDS()

print("Done.")

sleep(5)

