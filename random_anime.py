import requests
import re
import random
import json

def getXML():
    url = 'http://www.animenewsnetwork.com/encyclopedia/reports.xml?id=172&nlist=100&nskip=0'
    request = requests.get(url)
    if request.status_code == 200:
        #print "Successfully downloaded XML"
        #print request.text
        return request.text

def pick_random():
    anime_xml = getXML()
    match = re.findall('>([^"<"]+)</anime>', anime_xml)
    match = [s.encode('ascii','ignore') for s in match]
    match = [s.replace('&amp;', '&') for s in match]
    return random.choice(match)
    

