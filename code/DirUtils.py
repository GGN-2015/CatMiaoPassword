import os

# get Project Root Dir
def getRootDir():
    dirNow = os.path.dirname(__file__)
    return os.path.dirname(dirNow)

# get Code Dir
def getCodeDir():
    return os.path.join(getRootDir(), "code")

# file encrypted will be saved in ${RootDir}/file
def getFileDir():
    return os.path.join(getRootDir(), "file")

# config.json
def getConfigDir():
    return os.path.join(getRootDir(), "config")