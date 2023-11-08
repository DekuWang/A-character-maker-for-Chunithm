import xml.etree.ElementTree as ET
from wand import image
import os

class Chara:
    def __init__(self, nameStr, ID, png1, png2 = None, png3 = None, png4 = None, png5 = None, png6 = None, png7 = None, png8 = None, png9 = None, optNum = "A514", worksID = "514", worksStr = "自製"):
        
        self.optNum = optNum
        self.optFolder = "outPut/" + self.optNum

        #For XML
        #self.ID looks like 0007
        self.ID = ID
        #dataName looks like chara000070
        self.dataName = "chara0"+ str(self.ID) +"0"
        #nameID looks like 7
        self.nameID = str(int(self.ID))
        self.nameStr = nameStr
        self.sortName = self.nameStr
        self.worksID = worksID
        self.worksStr = worksStr
        #defaultImagesID looks like 7
        self.defaultImagesID = str(int(self.nameID))
        #defaultImagesStr looks like chara0007_0
        self.defaultImagesStr = "chara"+ str(self.ID) +"_0"

        #For toDDS
        self.png = list(filter(None,[png1, png2, png3, png4, png5, png6, png7, png8, png9]))

    def xmlEdit(self, file_xml = r'template/Chara.xml', works_xml = r'template/CharaWorks.xml', dds_xml = r'template/DDSImage.xml'):
        tree = ET.parse(file_xml)
        root = tree.getroot()

        root.find("dataName").text = self.dataName
        root.find("name").find("id").text = self.nameID + "0"
        root.find("name").find("str").text = self.nameStr
        root.find("sortName").text = self.sortName
        root.find("works").find("id").text = self.worksID
        root.find("works").find("str").text = self.worksStr
        root.find("defaultImages").find("id").text = self.defaultImagesID + "0"
        root.find("defaultImages").find("str").text = self.defaultImagesStr + "0"

        if len(self.png) > 1:
            for i in range(1,len(self.png)):
                root.find("addImages" + str(i)).find("changeImg").text = "true"
                root.find("addImages" + str(i)).find("charaName").find("id").text = str(self.nameID) + str(i)
                root.find("addImages" + str(i)).find("charaName").find("str").text = self.nameStr
                root.find("addImages" + str(i)).find("image").find("id").text = self.defaultImagesID + str(i)
                root.find("addImages" + str(i)).find("image").find("str").text = self.defaultImagesStr + str(i)
                root.find("addImages" + str(i)).find("rank").text = str(5 * (i + 2))

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

        for i in range(len(self.png)):
            tree3 = ET.parse(dds_xml)
            root3 = tree3.getroot()
            root3.find("dataName").text = self.dataName
            root3.find("name").find("id").text = self.nameID
            root3.find("name").find("str").text = self.nameStr
            root3.find("ddsFile0").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_0" + str(i) + "_00.dds"
            root3.find("ddsFile1").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_0" + str(i) + "_01.dds"
            root3.find("ddsFile2").find("path").text = "CHU_UI_Character_" + str(self.ID) + "_0" + str(i) + "_02.dds"
            ddsFolder = self.optFolder + "/ddsImage/ddsImage0" + str(self.ID) + str(i) +"/"
            if not os.path.exists(ddsFolder):
                os.makedirs(ddsFolder)
            tree3.write(ddsFolder + "/DDSImage.xml")
        

    def ToDDS(self):
        for i in range(len(self.png)):
            ddsName = self.makeddsName(str(i))
            ddsFolder = self.optFolder + "/ddsImage/ddsImage0" + str(self.ID) + str(i) +"/"

            if not os.path.exists(ddsFolder):
                os.makedirs(ddsFolder)

            with image.Image(filename = self.png[i]) as img:
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

    def makeddsName(self, digit):
        return ["CHU_UI_Character_" + str(self.ID) + "_0" + digit + "_00.dds", "CHU_UI_Character_" + str(self.ID) + "_0" + digit + "_01.dds", "CHU_UI_Character_" + str(self.ID) + "_0" + digit + "_02.dds"]



png1 = "testImage/1.png"
png2 = "testImage/2.png"
png3 = "testImage/3.png"

Kokoro = Chara("Kokoro", "0001", png1, png2, png3)

Kokoro.xmlEdit()
Kokoro.ToDDS()