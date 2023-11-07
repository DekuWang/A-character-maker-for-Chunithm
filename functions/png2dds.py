from wand import image

def png2dds(pngName, ddsName):
    with image.Image(filename = pngName) as img:
        if img.width > img.height:
            img.crop(width= img.height, height= img.height, gravity= "north")
        else:
            img.crop(width= img.width, height= img.width, gravity= "north") 

        img.resize(1080, 1080)
        img.compression = 'dxt5'
        img.save(filename = "image/" + ddsName[0])

        img.resize(512, 512)
        img.compression = 'dxt5'
        img.save(filename = "image/" + ddsName[1])

        img.crop(width= img.width - 200, height= img.width - 200, gravity= "north") 
        img.resize(128, 128)
        img.compression = 'dxt5'
        img.save(filename = "image/" + ddsName[2])
        

def makeddsName(userDdsName):
    return ["CHU_UI_Character_" + str(userDdsName) + "_00_00.dds", "CHU_UI_Character_" + str(userDdsName) + "_00_01.dds", "CHU_UI_Character_" + str(userDdsName) + "_00_02.dds"]


pngName = " & 'f:\Strange things\Chunithm related\Character\Program\inProcess\image\image.jpg'"
ddsName = "9998"
png2dds(pngName[4:len(pngName)-1], makeddsName(ddsName))
