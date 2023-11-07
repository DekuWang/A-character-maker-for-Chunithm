import xml.etree.ElementTree as ET
from wand import image
import os

class Chara:
    def __init__(self, nameStr, ID, pngName, optNum = "A514", worksID = "514", worksStr = "自製"):
        self.ID = ID
        self.worksID = worksID
        self.optNum = optNum
        self.optFolder = "outPut/" + self.optNum

        #For XML
        self.dataName = "chara0"+ str(self.ID) +"0" 
        self.nameID = str(self.ID) + "0"
        self.nameStr = nameStr
        self.sortName = self.nameStr
        self.worksID = self.worksID
        self.worksStr = worksStr
        self.defaultImagesID = self.nameID
        self.defaultImagesStr = "chara"+ str(self.ID) +"_00"

        #For toDDS
        self.pngName = pngName

    def xmlEdit(self, file_xml = r'template/Chara.xml', works_xml = r'template/CharaWorks.xml', dds_xml = r'template/DDSImage.xml'):
        tree = ET.parse(file_xml)
        root = tree.getroot()

        root.find("dataName").text = self.dataName
        root.find("name").find("id").text = self.nameID
        root.find("name").find("str").text = self.nameStr
        root.find("sortName").text = self.sortName
        root.find("works").find("id").text = self.worksID
        root.find("works").find("str").text = self.worksStr
        root.find("defaultImages").find("id").text = self.defaultImagesID
        root.find("defaultImages").find("str").text = self.defaultImagesStr

        tree = ET.ElementTree(root)
        charaFolder = self.optFolder + "/chara/chara0"+ str(self.ID) +"0"
        if not os.path.exists(charaFolder):
            os.makedirs(charaFolder)
        tree.write(charaFolder + "/Chara.xml")

        tree2 = ET.parse(works_xml)
        root2 = tree2.getroot()
        workFolder = self.optFolder + "/charaWorks/charaWorks000"+ str(self.worksID)
        if not os.path.exists(workFolder):
            os.makedirs(workFolder)
        if not os.path.exists(workFolder + "/CharaWorks.xml"):
            tree2.write(workFolder + "/CharaWorks.xml")

        tree3 = ET.parse(dds_xml)
        root3 = tree3.getroot()
        root3.find("dataName").text = self.dataName
        root3.find("name").find("id").text = self.nameID
        root3.find("name").find("str").text = self.nameStr
        root3.find("ddsFile0").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_00_00.dds"
        root3.find("ddsFile1").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_00_01.dds"
        root3.find("ddsFile2").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_00_02.dds"
        ddsFolder = self.optFolder + "/ddsImage/ddsImage0"+ str(self.ID) +"0"
        if not os.path.exists(ddsFolder):
            os.makedirs(ddsFolder)
        tree3.write(ddsFolder + "/DDSImage.xml")
        

    def ToDDS(self):
        ddsName = self.makeddsName()
        ddsFolder = self.optFolder + "/ddsImage/ddsImage0"+ str(self.ID) +"0/"
        if not os.path.exists(ddsFolder):
            os.makedirs(ddsFolder)
        with image.Image(filename = self.pngName) as img:
            if img.width > img.height:
                img.crop(width= img.height, height= img.height, gravity= "north")
            else:
                img.crop(width= img.width, height= img.width, gravity= "north") 

            img.resize(1080, 1080)
            img.compression = 'dxt5'
            img.save(filename = ddsFolder + ddsName[0])

            img.resize(512, 512)
            img.compression = 'dxt5'
            img.save(filename = ddsFolder + ddsName[1])

            img.crop(width= img.width - 200, height= img.width - 200, gravity= "north") 
            img.resize(128, 128)
            img.compression = 'dxt5'
            img.save(filename = ddsFolder + ddsName[2])

    def makeddsName(self):
        return ["CHU_UI_Character_" + str(self.ID) + "_00_00.dds", "CHU_UI_Character_" + str(self.ID) + "_00_01.dds", "CHU_UI_Character_" + str(self.ID) + "_00_02.dds"]

