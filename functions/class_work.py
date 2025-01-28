"""
The class for generating chara work files
"""
# First Party modules
import xml.etree.ElementTree as ET
from os.path import exists
from os import makedirs

# Project Modules
from config import CHARAWORK_OUTPUT_PATH, CHARAWORK_TEMPLATE

class Work():
    """
    The class for generating charawork files, basically XML files
    """
    def __init__(self, work_id, work_name):
        self.work_id = str(work_id)
        self.work_name = work_name
        self.dataname = f"charaWorks{self.work_id.rjust(6, '0')}"

    def edit_xml(self):
        """
        The function for editing work xml template
        """
        work_xml = ET.parse(source=CHARAWORK_TEMPLATE)
        work_root = work_xml.getroot()

        work_root.find("name").find("str").text = self.work_name
        work_root.find("name").find("id").text = self.work_id
        work_root.find("dataName").text = self.dataname

        output_path = f"{CHARAWORK_OUTPUT_PATH}/{self.dataname}/"
        if not exists(output_path):
            makedirs(output_path)

        ET.indent(tree=work_xml, space = " ")
        work_xml.write(output_path + "CharaWorks.xml", encoding="UTF_8", xml_declaration=True)
 
# For testing use
# test_work = Work(1234, "test")
# test_work.edit_xml()
