# -*- coding: utf-8 -*-
import requests
import re
import random
import json

global anime_xml
anime_xml = ""

def getXML():
    global anime_xml
    url = 'http://www.animenewsnetwork.com/encyclopedia/reports.xml?id=172&nlist=100&nskip=0'
    request = requests.get(url)
    if request.status_code == 200:
        #print "Successfully downloaded XML"
        #print request.text
        anime_xml = request.text
        return request.text

def pick_random():
    getXML()
    match = re.findall('>([^"<"]+)</anime>', anime_xml)
    match = [s.encode('ascii','ignore') for s in match]
    match = [s.replace('&amp;', '&') for s in match]
    return random.choice(match)
    
def get_summary(anime_title):
    global anime_xml
    if "(" in anime_title:
        anime_title = anime_title[:anime_title.index("(")]
    if "-" in anime_title:
        anime_title = anime_title[:anime_title.index("-")]
    reg_expression = '<anime href="([^"]+)">'+ anime_title
    match = re.findall(reg_expression, anime_xml)
    if not match:
        return get_summary(pick_random())
    request = requests.get("http://www.animenewsnetwork.com"+match[0])
    anime_info = request.text
    reg_expression = "<strong>Plot Summary:</strong> \n\t<span>([^<]+)</span>"
    match = re.findall(reg_expression, anime_info)
    match = [s.encode('ascii', 'ignore') for s in match]
    if not match:
        return "No summary at this time"
    return match[0]

