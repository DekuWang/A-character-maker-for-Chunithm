from functions.mkDir import mkDir
from functions.classChara import *
from time import sleep

CharaList = []

userInput = str(input("Drop your image here, or press q to continue: "))
while(userInput != "q"):
    imagePath = userInput[3:len(userInput)-1]

    nameStr = input("Character Name: ")
    ID = int(input("Character ID: "))
    pngName = imagePath

    nameStr = Chara(str(nameStr), ID, pngName)
    CharaList.append(nameStr)
    userInput = str(input("Drop your image here, or press q to continue: "))

mkDir()

for i in CharaList:
    i.xmlEdit()
    i.ToDDS()

print("Done.")

sleep(5)

