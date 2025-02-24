import requests
from bs4 import BeautifulSoup
import json
import requests
import datetime
from bs4 import BeautifulSoup
import re

def getVersion() -> str:
    vers = ""
    for ver in soup.findAll('small', href=False):
        x = ver.text
        if ('iOS' in x):
            versione = re.findall(pattern=r"\((\d+\.\d+\.\d+)\)",string=x)
            return str(versione[0])

def getlink() -> json:
    mylink = ""
    date = str(datetime.date.today())
    for link in soup.findAll('a', href=True):
        if('.ipa' in link['href']):
            mylink = link['href']
            myjson= {}
            myjson['version'] = getVersion()
            myjson['date'] = date
            myjson['size'] = 146000000
            myjson['downloadURL'] = mylink
            myjson['minOSVersion'] = "15.0"
            return (myjson)

def json_upd(jsonfile):
    f = open('alt.json','w')
    json_object = json.dumps(jsonfile, indent=4)
    f.write(json_object)
    f.close()

def get_Json() -> json:
    with open('alt.json', 'r') as myjson:
        data = json.load(myjson)
        myjson.close()
        return data

x = requests.get('https://ipogo.app')
soup = BeautifulSoup(x.text,"html.parser")

json_file = get_Json()
if getVersion() != json_file['apps'][0]['versions'][0]['version']:
    jadd = getlink()
    json_file['apps'][0]['versions'].insert(0, jadd)
    json_upd(json_file)
    print("Update Detected")
else:
    print("No Update Detected")
