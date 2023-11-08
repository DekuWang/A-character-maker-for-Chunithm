from functions.mkDir import mkDir
from functions.classChara import *
from time import sleep

CharaList = []

userInput = str(input("Drop your image here, or press q to continue: "))
while(userInput != "q"):
    imagePath = userInput[3:len(userInput)-1]
    nameStr = input("Character Name: ")
    ID = int(input("Character ID(ID should be exact 4 numbers): "))
    while(len(str(ID)) != 4):
        ID = input("Please enter a correct character ID(ID should be exact 4 numbers): ")
    pngName = imagePath
    pngCount = 1
    name = str(nameStr)
    nameStr = Chara(name, ID, pngName)

    transFromInput = input("Would you plan to add transform to your character? (y/n): ")
    while(transFromInput != "n" and pngCount < 9):
        pngInput = str(input("Drop your image here, or press q to exit: "))[3:len(userInput)-1]
        if pngInput == "q":
            break
        nameStr.addPng(pngInput)
        transformName = input("Transform Name, leave it blank if you don't need to change name:")
        if transformName != "":
            nameStr.addNameStr(transformName)
        else:
            nameStr.addNameStr(name)
        pngCount += 1
        if pngInput == 9:
            break
        transFromInput = input("Would you plan to add more transform to your character? (y/n): ")


    CharaList.append(nameStr)
    userInput = str(input("Drop your image here to create a new character, or press q to continue: "))

mkDir()

for i in CharaList:
    i.xmlEdit()
    i.ToDDS()

print("Done.")

sleep(5)

