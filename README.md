# MANGOBACK
Back It Up from Instance to Instance


## Introduction
---------------
- Purpose of this mongoback library is to make it easy for user to take backup from
  one instace and restore it on another instance by just configuring one config
  file.

  ```
  NOTICE:don't use this library, If remote instace database have possibility of 
  modification by app server beetween backups. Because basically, What  library 
  does is making clone of local instace to remote instance.so it'll drop db  on 
  your remote instance.
  ```

## Installation
- To install, You need to clone this directory to your local machine or instance that 
you want take backup from.
- Then, `cd` to that directory and fire following command in Terminal.

```bash
 $ sudo python setup.py install
```

## Usage

- First you need to define config variable as following in script:


```python
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
    }}

MG = MangoBack(CONFIG)
MG.run()

```
- Before running script, First make directory in remote instance where you'll store your
 backup.

- To initialise, pass `CONFIG` variable in `MangoBack` class, Use `run()` function to start
 process.

  ```bash
  $sudo python mbconfig.py 
  ```

- Remember that if your mongod process is not running on remote server and you only
  want copy backup files then, You must Disable `remote` variable in `restore_config`.
  
- Authentication in place then, You must Enable `auth` system and provide `uname`
 and `pwd` while configuring.

- Always add absolute `PATH` in configure file. Because rsync can not understand relative path.

