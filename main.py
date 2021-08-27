import os
import time
import json
import schedule

isJob = True
config = {}
with open('./config.json', "r") as configFile:
    config = json.load(configFile)

def mysqldump():
    global config


    q = "mysqldump -u " + config["db"]["login"] + " --password=" + config["db"]["password"] + " " + config["db"]["name"] + " > " + config["path"] + config["fileName"]
    os.system(q)
    global isJob
    isJob = False

schedule.every().day.at(config["time"]).do(mysqldump)

while isJob:
    schedule.run_pending()
    time.sleep(1)