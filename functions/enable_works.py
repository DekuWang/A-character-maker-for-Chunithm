"""
Module for testing
"""
# Built-in Module
import xml.etree.ElementTree as ET

# Project Module
from config import WORK_SORT_TEMPLATE

def edit_work_sort(file_path: str, work_id: int):
    """
    function for editing work_sort xml file, 
    """
    # Ensure the file path
    work_name_sort_path         = rf"{file_path}\data\A000\charaWorks\WorksNameSort.xml"
    work_sort_path              = rf"{file_path}\data\A000\charaWorks\WorksSort.xml"

    # parse the xml tree for two files
    work_name_sort_tree         = ET.parse(source = work_name_sort_path)
    work_name_sort_root         = work_name_sort_tree.getroot()

    work_sort_tree              = ET.parse(source = work_sort_path)
    work_sort_root              = work_sort_tree.getroot()

    # Allocate existed ids exist in the file
    existed_work_ids            = []

    for i in work_name_sort_root.find("SortList").findall("StringID"):
        existed_work_ids.append(i.find("id").text)

    if work_id not in existed_work_ids:
        work_id_block = ET.fromstring(WORK_SORT_TEMPLATE)
        work_id_block.find("id").text = str(work_id)

        work_name_sort_root.find("SortList").append(work_id_block)
        work_sort_root.find("SortList").append(work_id_block)


    # Write to xml files 
    ET.indent(tree = work_name_sort_tree, space = "\t")
    work_name_sort_tree.write(work_name_sort_path, encoding = "utf-8", xml_declaration = True)

    ET.indent(tree = work_sort_tree, space = "\t")
    work_sort_tree.write(work_sort_path, encoding = "UTF-8", xml_declaration = True)

# For testing
# edit_work_sort(file_path = r"D:\Strange Projects\A-character-maker-for-Chunithm\test", work_id = 514115)