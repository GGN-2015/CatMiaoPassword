import json
import os
import DirUtils

configFileName = os.path.join(DirUtils.getConfigDir(), "config.json")
MEM_CONFIG = json.load(open(configFileName))

def get(name):
    assert type(name) == str
    assert MEM_CONFIG.get(name) is not None
    return MEM_CONFIG[name]