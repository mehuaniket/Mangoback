
import sys
import os
import subprocess
import time
import colorama


class MangoBack:

    """Purpose of this mongoback library is to make it easy for user to take backup from
  one instace and restore it on another instance by just configuring one config
  file.
        """

    def __init__(self, config):
        """initilise configuration from config directory"""
        # mangoback always take backup from only local URLs
        self.host = "127.0.0.1"
        # ps is to holding variable for subprocess in every function.
        self.ps = None
        self.spinner = None
        # username and password is loded from config if auth is True
        # otherwise it'll load as None
        if config["backup_config"]["auth"] is True:
            self.buname = config["backup_config"]["uname"]
            self.bpwd = config["backup_config"]["pwd"]
        else:
            self.buname = None
            self.bpwd = None
        # mangoback will only run process for single database.
        # if databse name is specified.
        if "dbname" in config:
            self.dbname = config["dbname"]
        else:
            self.dbname = None
        # you must specify backup directory
        self.backup_dir = config["backup_config"]["backup_dir"]
        self.port = config["backup_config"]["port"]
        self.remote = config["restore_config"]["remote"]
        if config["restore_config"]["remote"] is True:
            if config["restore_config"]["auth"] is True:
                self.runame = config["restore_config"]["uname"]
                self.rpwd = config["restore_config"]["pwd"]
            else:
                self.runame = None
                self.rpwd = None
            self.instance_url = config["restore_config"]["instance_url"]
            self.rport = config["restore_config"]["port"]
            self.remote_dir = config["restore_config"]["remote_dir"]
            self.pem_file = config["restore_config"]["pem_file"]
            self.remote_install = config["restore_config"]["remote_install"]

    def spinning_cursor(self):
        """this is spinner function to spin cursor,print continuously when subprocess is running"""
        while True:
            for cursor in '|/-\\':
                yield cursor

    def spinit(self):
        """this function will print and backspace everytime spinner genrate change value"""
        # Create spinner variable to run it in every function as needed.
        self.spinner = self.spinning_cursor()
        # Check if process is still running
        while self.ps.poll() is None:
            sys.stdout.write(self.spinner.next())
            sys.stdout.flush()
            sys.stdout.write('\b')

    def backup_db(self):
        """this method will take backup on local machine """
        if self.buname is not None and self.bpwd is not None:
            cmd = "mongodump  --host {host} --port {port} --username {uname} --password {pwd}".format(
                host=self.host,port=self.port, uname=self.buname, pwd=self.bpwd)
        else:
            cmd = "mongodump  --host {host} --port {port}".format(host=self.host,port=self.port)
        if self.dbname is not None:
            cmd = cmd + " --db {dbname}".format(dbname=self.dbname)
        cmd = cmd + " --out={db_dir}".format(db_dir=self.backup_dir)
        print cmd
        print colorama.Fore.GREEN
        print "Backuping at...", self.backup_dir
        self.ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # Check if process is still running
        self.spinit()
        # Grab output
        self.ps.communicate()
        print colorama.Style.RESET_ALL
        print "Backup process is finished"
        print "Backup files at", self.backup_dir

    def remote_upload(self):
        """it will upload all file to server"""
        cmd = 'rsync --update -rave "ssh -i {pempath}" {backup_db_dir} {instance_url}:{remote_dir}'.format(
            pempath=self.pem_file, backup_db_dir=self.backup_dir,
            instance_url=self.instance_url, remote_dir=self.remote_dir)
        print "uploading...at remote dir:", self.remote_dir
        self.ps = subprocess.Popen(cmd, shell=True)
        self.ps.communicate()
        print "restore process is finished"


    def restore_db(self):
        """ it will restore uploaded dir"""

        if self.runame is not None and self.rpwd is not None:
            cmd = "mongorestore --drop   --host {host} --username {uname} --password {pwd}".format(
                host=self.host, uname=self.runame, pwd=self.rpwd)
        else:
            cmd = "mongorestore --drop   --host {host}".format(
                host=self.host)
        cmd = cmd + " {db_dir}".format(db_dir=self.remote_dir)
        print cmd
        print colorama.Fore.GREEN
        print "running restore at remote dir:"
        print "restoring...", self.remote_dir
        logincmd = 'ssh -i "{pempath}" {instance_url} "{cmd}"'.format(
            pempath=self.pem_file, instance_url=self.instance_url, cmd=cmd)
        print logincmd
        self.ps = subprocess.Popen(
            logincmd, shell=True, stdout=subprocess.PIPE)
        self.spinit()
        # Grab output
        self.ps.communicate()
        print colorama.Style.RESET_ALL
        print "restore process is finished"

    def run(self):
        """it's ultimate method to run all process in single method call"""
        self.backup_db()
        if self.remote is True:
            self.remote_upload()
            if self.remote_install is True:
                self.restore_db()
        
