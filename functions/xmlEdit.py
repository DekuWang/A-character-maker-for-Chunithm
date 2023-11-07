# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import os

#Edit Chara.xml
def editChara(nameStr, ID, optName, file_xml = 'template/Chara.xml', worksID = 5140, worksStr = "自製"):
    tree = ET.parse(file_xml)
    root = tree.getroot()

    root.find("dataName").text = "chara0"+ str(ID) +"0"
    root.find("name").find("id").text = str(ID) + "0"
    root.find("name").find("str").text = nameStr
    root.find("sortName").text = nameStr
    root.find("works").find("id").text = str(worksID)
    root.find("works").find("str").text = worksStr
    root.find("defaultImages").find("id").text = str(ID) + "0"
    root.find("defaultImages").find("str").text = "chara"+ str(ID) +"_00"

    tree = ET.ElementTree(root)
    charaFolder = "outPut/" + optName + "/chara/chara0"+ str(ID) +"0"
    if not os.path.exists(charaFolder):
        os.makedirs(charaFolder)
    tree.write(charaFolder + "/Chara.xml")

#optName = "A124"
editChara("メイベル", 9999, "A124")
#print(os.path.exists("output/" + optName + "/chara/"))