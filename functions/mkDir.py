"""
Making directories for all elements
"""
# Build-in Modules
import os

def mk_dir(opt_name = "A514"):
    """ function for making directories
    param: 
        opt_name: something looks like AXXX
    """
    if not os.path.exists("outPut/" + opt_name):
        os.makedirs("outPut/" + opt_name)
        os.makedirs("outPut/" + opt_name + '/chara')
        #os.makedirs("outPut/" + opt_name + '/charaWorks')
        os.makedirs("outPut/" + opt_name + '/ddsImage')
    else:
        print('The direction exists.')
