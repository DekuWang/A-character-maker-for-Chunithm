"""
Module for making Characters, including editing needed xml file and transfer image to dds format
"""
# Built-in Modules
import os
import xml.etree.ElementTree as ET

# Third-party modules
from wand import image

SKILL_DICT = {
    'Invalid': -1,
    '限界突破の証': 6100010,
    '真・限界突破の証': 6100011,
    '絆・限界突破の証': 6100012,
    'オールガード【LMN】': 6102000,
    'ゲージブースト【LMN】': 6102001,
    'コンボエクステンド【LMN】': 6102002,
    'アタックギルティ【LMN】': 6102003,
    'ジャッジメント【LMN】': 6102004,
    'オーバージャッジ【LMN】': 6102005,
    '嘆きのしるし【LMN】': 6102006,
    '勇気のしるし【LMN】': 6102007,
    '道化師の狂気【LMN】': 6102008
    }

class Chara:
    """
    Class for making characters, 
    param:
        rank_reward will be a dictionary looks like {level: skill}
        Maximum length of rank_reward will be 7

        transfer_rank will be a list looks like [level1, level2, ...]
        Length of transfer_rank will be the amount of transfer(maxumum 9)
    """
    def __init__(self, name_str:str, chara_id:str, png1:str, rank_reward:dict, transfer_rank:list,
                 works_id:str = "514", opt_num:str = "A514", work_str:str = "自製"):
        self.opt_num = opt_num
        self.opt_folder = "outPut/" + self.opt_num

        #For XML
        #self.chara_id looks like 0007
        self.chara_id = chara_id
        #dataName looks like chara000070
        self.dataname = "chara0"+ str(self.chara_id) +"0"
        #name_id looks like 7
        self.name_id = str(int(self.chara_id))
        self.name_str = [name_str]
        self.sort_name = self.name_str[0]
        self.works_id = works_id
        self.work_str = work_str
        #default_image_id looks like 7
        self.default_image_id = str(int(self.name_id))
        #default_image_str looks like chara0007_0
        self.default_image_str = "chara"+ str(self.chara_id) +"_0"

        self.rank_reward = rank_reward
        self.transfer_rank = transfer_rank

        #For toDDS
        self.png = [png1]

    def xml_edit(self, file_xml:str = r'template/Chara.xml',
                # works_xml:str = r'template/CharaWorks.xml',
                dds_xml:str = r'template/DDSImage.xml'):
        """
        Function for editing xml file, filling needed blanks
        """
        tree = ET.parse(file_xml)
        root = tree.getroot()

        root.find("dataName").text = self.dataname
        root.find("name").find("id").text = self.name_id + "0"
        root.find("name").find("str").text = self.name_str[0]
        root.find("sortName").text = self.sort_name
        root.find("works").find("id").text = self.works_id
        root.find("works").find("str").text = self.work_str
        root.find("defaultImages").find("id").text = self.default_image_id + "0"
        root.find("defaultImages").find("str").text = self.default_image_str + "0"

        if len(self.png) > 1:
            for i in range(1,len(self.png)):
                root.find("addImages" + str(i)).find("changeImg").text = "true"
                root.find("addImages" + str(i)).find("charaName").find("id").text = str(self.name_id) + str(i)
                root.find("addImages" + str(i)).find("charaName").find("str").text = self.name_str[i]
                root.find("addImages" + str(i)).find("image").find("id").text = self.default_image_id + str(i)
                root.find("addImages" + str(i)).find("image").find("str").text = self.default_image_str + str(i)
                root.find("addImages" + str(i)).find("rank").text = self.transfer_rank[i-1]

        for i in enumerate(self.rank_reward):
            current_index = i[0]    # Index
            current_key = i[1]      # Rank
            current_reward = self.rank_reward[current_key]
            current_block = root.find("ranks").findall("CharaRankData")[current_index]
            # Set Reward ID
            current_block.find("rewardSkillSeed").find("rewardSkillSeed").find("id").text = SKILL_DICT[current_reward]
            # Set Reward String
            current_block.find("rewardSkillSeed").find("rewardSkillSeed").find("str").text = current_reward
            # Set Reward Rank
            root.find("ranks").findall("CharaRankData")[i[0]].find("index").text = current_key

        tree = ET.ElementTree(root)
        chara_folder = self.opt_folder + "/chara/chara0"+ str(self.chara_id) +"0"
        if not os.path.exists(chara_folder):
            os.makedirs(chara_folder)
        tree.write(chara_folder + "/Chara.xml")

        # Current unused due to don't know how to make works work
        # tree2 = ET.parse(works_xml)
        # root2 = tree2.getroot()
        # workFolder = self.opt_folder + "/charaWorks/charaWorks000"+ str(self.works_id)
        # if not os.path.exists(workFolder):
        #     os.makedirs(workFolder)
        # if not os.path.exists(workFolder + "/CharaWorks.xml"):
        #     tree2.write(workFolder + "/CharaWorks.xml")

        for i in range(len(self.png)):
            tree3 = ET.parse(dds_xml)
            root3 = tree3.getroot()
            root3.find("dataName").text = "ddsImage0" + str(self.chara_id) + str(i)
            root3.find("name").find("id").text = self.default_image_id + str(i)
            root3.find("name").find("str").text = "chara"+ str(self.chara_id) +"_0" + str(i)
            root3.find("ddsFile0").find("path").text = f"CHU_UI_Character_{str(self.chara_id)}_0{str(i)}_00.dds"
            root3.find("ddsFile1").find("path").text = f"CHU_UI_Character_{str(self.chara_id)}_0{str(i)}_01.dds"
            root3.find("ddsFile2").find("path").text = f"CHU_UI_Character_{str(self.chara_id)}_0{str(i)}_02.dds"

            dds_folder = self.opt_folder + "/ddsImage/ddsImage0" + str(self.chara_id) + str(i) +"/"
            if not os.path.exists(dds_folder):
                os.makedirs(dds_folder)
            tree3.write(dds_folder + "/DDSImage.xml")

    def to_dds(self):
        """
        Function for transfer user's image to dds format
        """
        for i in enumerate(self.png):
            current_index = i[0]
            dds_name = self.make_ddsname(current_index)
            dds_folder = f"{self.opt_folder}/ddsImage/ddsImage0{str(self.chara_id)}{str(current_index)}/"

            if not os.path.exists(dds_folder):
                os.makedirs(dds_folder)

            # Croping image to square, and resize them to needed size
            with image.Image(filename = self.png[current_index]) as img:
                if img.width > img.height:
                    img.crop(width= img.height, height= img.height, gravity= "north")
                else:
                    img.crop(width= img.width, height= img.width, gravity= "north")

                img.resize(1080, 1080)
                img.compression = 'dxt5'
                img.save(filename = dds_folder + dds_name[0])

                img.resize(512, 512)
                img.compression = 'dxt5'
                img.save(filename = dds_folder + dds_name[1])

                img.crop(width= img.width - 200, height= img.width - 200, gravity= "north")
                img.resize(128, 128)
                img.compression = 'dxt5'
                img.save(filename = dds_folder + dds_name[2])

    def make_ddsname(self, digit):
        """
        Function for generating DDS names
        """
        return [f"CHU_UI_Character_{self.chara_id}_0{digit}_00.dds",
                f"CHU_UI_Character_{self.chara_id}_0{digit}_01.dds",
                f"CHU_UI_Character_{self.chara_id}_0{digit}_02.dds"]

    def add_image(self, image_):
        """
        Function for appending new image to current Character
        """
        self.png.append(image_)

    def addname_str(self, name_str):
        """
        Function for appending new name string to current Character
        """
        self.name_str.append(name_str)

    def getname_str(self):
        """
        Function for getting name from current Character
        """
        return self.name_str

    def get_image(self):
        """
        Function for getting image from current Character
        """
        return self.png

test_png = r"D:\StrangeThings\Chunithm related\Character\图片\梅贝尔\CHU_UI_Character_9999_00_00.png"
test_chara = Chara(name_str="test", chara_id=1234, png1=test_png, rank_reward={}, transfer_rank=[])

test_chara.to_dds()
test_chara.xml_edit()
