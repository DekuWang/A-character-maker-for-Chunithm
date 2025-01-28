"""
Module used for creating nameplates
"""

# Build In Modules
import os
import xml.etree.ElementTree as ET

# Third party Modules
from wand.image import Image
from wand.drawing import Drawing

# Project Modules
from config import NAMEPLATE_OUTPUT_PATH, NAMEPLATE_BACKGROUND, NAMEPLATE_TEMPATE

class Nameplate:
    """
    A class for creating nameplate
    """
    def __init__(self, plate_id: int, name: str, image_png: str,
                 explain_text: str, default_have: bool):
        # tell user to put an plate_id larger than 10000
        self.plate_id = plate_id
        self.plate_id_str = str(plate_id).rjust(8,"0")
        self.name = name
        self.image_png = image_png
        self.default_have = "true" if default_have else "false"
        self.explain_text = explain_text
        # image filename processed by the program
        self.output_image = f"CHU_UI_NamePlate_{self.plate_id_str}.png"
        self.dataname = f"namePlate{self.plate_id_str}"
        self.plate_folder = f"{NAMEPLATE_OUTPUT_PATH}/{self.dataname}"

    def xml_edit(self):
        """
        Filling the needed data into the xml template
        """
        # Make Path Folder
        if not os.path.exists(self.plate_folder):
            os.makedirs(self.plate_folder)
        tree = ET.parse(NAMEPLATE_TEMPATE)
        root = tree.getroot()
        root.find("dataName").text = self.dataname
        root.find("name").find("id").text = str(self.plate_id)
        root.find("name").find("str").text = self.name
        root.find("image").find("path").text = self.output_image
        root.find("defaultHave").text = str(self.default_have)
        root.find("explainText").text = self.explain_text

        tree = ET.ElementTree(root)
        if not os.path.exists(self.plate_folder):
            os.makedirs(self.plate_folder)
        tree.write(self.plate_folder + "/NamePlate.xml", encoding="UTF_8", xml_declaration=True)

    # def print_all(self):
    #     print(f"id:             {self.id}")
    #     print(f"name:           {self.name}")
    #     print(f"image:          {self.image_png}")
    #     print(f"default_have:   {self.default_have}")
    #     print(f"dataname:       {self.dataname}")

    def to_dds(self):
        """
        Transfer users' image to dds image
        """
        # nameplate image size = 228 * 576 (h * w)
        # nameplate size = 185 * 565 (h * w)
        # filename format: CHU_UI_NamePlate_00010149.dds

        background = Image(filename=NAMEPLATE_BACKGROUND)
        background.colorspace = "transparent"
        foreground = Image(filename = self.image_png)
        foreground.resize(width = 565, height = 185)

        with Drawing() as draw:
            print(background.height)
            draw.composite(
                operator='copy',
                  top = 0, left = 0,
                  height = foreground.height,
                  width = foreground.width,
                  image = foreground)
            draw(background)
            if not os.path.exists(self.plate_folder):
                os.makedirs(self.plate_folder)
            background.save(filename = f"{self.plate_folder}/{self.output_image}")

# For testing use
# test_plate = Nameplate(plate_id=1234, name = "test", image_png=r"D:\StrangeThings\Chunithm related\Character\图片\梅贝尔\CHU_UI_Character_9999_00_00.png",
#                        explain_text="test", default_have=1)
# test_plate.to_dds()
# test_plate.xml_edit()
