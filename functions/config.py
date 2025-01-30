"""
For Stroing some global variables
"""

OPT_NAME = "A514" # Default OPT_Name
OUTPUT_PATH = f"output/{OPT_NAME}"

# For dds map
DDSMAP_OUTPUT_PATH = f"{OUTPUT_PATH}/ddsMap"
DDSMAP_TEMPLATE = r"template/MapXML/DDSMap.xml"

# For map.xml
MAP_OUTPUT_PATH = f"{OUTPUT_PATH}/map"
MAP_TEMPLATE = r"template/MapXML/Map.xml"

# For mapArea.xml
MAPAREA_OUTPUT_PATH = f"{OUTPUT_PATH}/mapArea"
MAPAREA_TEMPLATE = r"template/MapXML/MapArea.xml"

# For character
CHARA_OUTPUT_PATH = f"{OUTPUT_PATH}/chara"
CHARA_TEMPLATE = r"template/Chara.xml"
CHARA_DDS_OUTPUT_PATH = f"{OUTPUT_PATH}/ddsImage"
CHARA_DDS_IMAGE_TEMPLATE = r"template/DDSImage.xml"
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

RANK_REWARD_XML_TEXT = """
<CharaRankData>
  <index></index>
  <type>1</type>
  <rewardSkillSeed>
    <rewardSkillSeed>
      <id></id>
      <str></str>
      <data />
    </rewardSkillSeed>
  </rewardSkillSeed>
  <text>
    <flavorTxtFile>
      <path />
    </flavorTxtFile>
  </text>
</CharaRankData>
"""

# For nameplate
NAMEPLATE_OUTPUT_PATH = f"{OUTPUT_PATH}/namePlate"
NAMEPLATE_TEMPATE = r"template/NamePlate.xml"
NAMEPLATE_BACKGROUND = r"template/nameplateBG.png"

# For Trophy
TROPHY_OUTPUT_PATH = f"{OUTPUT_PATH}/trophy"
TROPHY_TEMPLATE = r"template/Trophy.xml"

# For charaWork
CHARAWORK_OUTPUT_PATH = f"{OUTPUT_PATH}/charaWorks"
CHARAWORK_TEMPLATE = r"template/CharaWorks.xml"
