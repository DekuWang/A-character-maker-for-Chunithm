import os

def mkDir(optName = "A514"):
    if not os.path.exists("outPut/" + optName):
        os.makedirs("outPut/" + optName)
        os.makedirs("outPut/" + optName + '/chara')
        os.makedirs("outPut/" + optName + '/charaWorks')
        os.makedirs("outPut/" + optName + '/ddsImage')
    else:
        print('The direction exists.')