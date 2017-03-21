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
        "backup_dir": os.getcwd() + "/backup/"
    },
    "restore_config": {
        "auth":False,
        "uname":None,
        "pwd":None,
        "remote": True,
        "instance_url": "ubuntu@ec2-435-134-234-225.us-west-2.compute.amazonaws.com",
        "remote_dir": "/home/ubuntu/backup",
        "pem_file": "/home/aniket/Desktop/projects/keys/example.pem"
    }
}

MG = MangoBack(CONFIG)
MG.run()
