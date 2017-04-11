"""
configuration for mangoback
"""
import os
from mangoback import MangoBack


CONFIG = {
    "dbname":None,
    "backup_config": {
        "auth":False,
        "uname":None,
        "pwd":None,
        "port":"27017",
        "backup_dir": os.getcwd() + "/backup/"
    },
    "restore_config": {
        "auth":False,
        "uname":None,
        "pwd":None,
        "remote": False,
        "remote_install":True,
        "instance_url": "ubuntu@35.164.228.234",
        "port":"27017",
        "remote_dir": "/home/ubuntu/backup",
        "pem_file": "/Users/Aniket/Documents/keys/iot-com.pem"
    }
}

MG = MangoBack(CONFIG)
MG.run()
