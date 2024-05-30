import xml.etree.ElementTree as ET
from wand.image import Image, COMPOSITE_OPERATORS
from wand.color import Color
from wand.drawing import Drawing
from wand.display import display
import os

class nameplate:
    def __init__(self, id: int, name: str, image_png: str, explainText: str, default_have: bool, optNum = "A514"):
        
        self.optNum = optNum
        self.optFolder = "outPut/" + self.optNum

        self.id = id # tell user to put an id larger than 10000
        self.name = name
        self.image_png = image_png
        self.default_have = ["false", "true"][default_have]
        self.explain_text = explainText
        self.output_image = f"CHU_UI_NamePlate_000{self.id}.png" # image filename processed by the program
        self.dataname = f"namePlate000{self.id}"
        self.plate_folder = self.optFolder + "/namePlate/" + self.dataname
        
        # Make Path Folder
        if not os.path.exists(self.plate_folder):
            os.mkdir(self.plate_folder)


    def xmlEdit(self, file_xml = r'template/NamePlate.xml'):
        tree = ET.parse(file_xml)
        root = tree.getroot()
        root.find("dataName").text = self.dataname
        root.find("name").find("id").text = str(self.id)
        root.find("name").find("str").text = self.name
        root.find("image").find("path").text = self.output_image
        root.find("defaultHave").text = str(self.default_have)
        root.find("explainText").text = self.explain_text

        tree = ET.ElementTree(root)
        if not os.path.exists(self.plate_folder):
            os.makedirs(self.plate_folder)
        tree.write(self.plate_folder + "/NamePlate.xml")
    
    # def print_all(self):
    #     print(f"id:             {self.id}")
    #     print(f"name:           {self.name}")
    #     print(f"image:          {self.image_png}")
    #     print(f"default_have:   {self.default_have}")
    #     print(f"dataname:       {self.dataname}")

    def to_dds(self):
        # nameplate image size = 228 * 576 (h * w)
        # nameplate size = 185 * 565 (h * w)
        # filename format: CHU_UI_NamePlate_00010149.dds

        background = Image(filename = f"template/nameplateBG.png")
        background.colorspace = "transparent"
        foreground = Image(filename = self.image_png)
        foreground.resize(width = 565, height = 185)

        with Drawing() as draw:
            print(background.height)
            draw.composite(operator='copy', top = 0, left = 0, height = foreground.height, width = foreground.width, image = foreground)
            draw(background)
            # background.save(filename = self.plate_folder + "/output.png")
            background.save(filename = f"{self.plate_folder}/{self.output_image}")

# test_path = r"F:\Chunithm\Luminous\0322LUMINOU\CHUNITHM LUMINOU (SDHD 2.20.00)\data\A000\namePlate\namePlate00010149\CHU_UI_NamePlate_00010149.dds"
# print(test_path)
# test_plate = nameplate(id = 123, name = "name", image_png=test_path, explainText= "explainText", default_have=1)
# test_plate.to_dds()
