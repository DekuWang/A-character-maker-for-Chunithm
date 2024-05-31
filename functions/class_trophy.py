"""
Module for storing trophy class
"""
# First party modules
import os
import xml.etree.ElementTree as ET

class Trophy:
    """
    Class for creaeting Trophy
    """
    def __init__(self, trophy_id:int, name:str, default_have:bool,
                 rare_type:int, opt_num:str = "A514", explain_text:str = "-"):
        self.trophy_id = trophy_id
        self.name = name
        self.explain_text = explain_text
        self.default_have = "true" if default_have else "false"
        self.rare_type = rare_type

        self.dataname = f"trophy00{trophy_id}"
        self.trophy_folder = f"outPut/{opt_num}/trophy/{self.dataname}"

    def edit_xml(self):
        """
        For generate trophy xml file
        """
        if not os.path.exists(self.trophy_folder):
            os.makedirs(self.trophy_folder)

        tree = ET.parse("template/Trophy.xml")
        root = tree.getroot()

        root.find("dataName").text = self.dataname
        root.find("name").find("id").text = str(self.trophy_id)
        root.find("name").find("str").text = self.name
        root.find("explainText").text = self.explain_text
        root.find("defaultHave").text = self.default_have
        root.find("rareType").text = str(self.rare_type)

        tree = ET.ElementTree(root)
        tree.write(self.trophy_folder+"/Trophy.xml")
