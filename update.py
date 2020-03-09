import os, sys, subprocess
import requests
from time import sleep


print("started new script")

scriptname = os.path.basename(__file__)

url = "https://raw.githubusercontent.com/hibryid/Testupdate/master/update.py"
r = requests.get(url)
with open(scriptname, 'wb') as f:
    f.write(r.content)
    print("Done downloading")


while True:
    print("sleeping enough")
    sleep(15)
    print(os.path.basename(__file__))
    os.execl(sys.executable, sys.executable, * sys.argv)
