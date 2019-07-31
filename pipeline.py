import requests
import json
import sys
#import datetime

""" 
script that scans and shows the avg and max build times of jenkins jobs and projects
I have no access to manage plugins so i cant install nice plugins that already do this
therefore i made my own script. you need to add the urls of the apps to a file.
mine was named seleniumURLS.txt on the line with open file
"""

version = "7.1.4"
try:
    if sys.argv[1]:
        print("Your version input: ", sys.argv[1])
        version = sys.argv[1]
except:
    pass

url1 = sys.argv[2]

#http://jenkins.birst... 

def parseBuild(url):
    r = requests.get(url)
    temp = r.json()
    stringy = json.dumps(temp)
    stringy = json.loads(stringy)
    timeArray = []
    maxx = 0
    avg = 0

    for each in stringy['builds']:
        convert = round(each['duration'] / 3600000, 4)
        convert *= 60
        timeArray.append(round(convert, 2))

    for each in timeArray:
        if each > maxx:
            maxx = each
        avg += each

    try:
        avg /= len(timeArray)

    except:
        avg = 0

    print(str.format("MAX: {0:.3f}" , maxx), "minutes")
    print(str.format("AVG: {0:.3f}", avg), "minutes")
    print("BUILD TIME (mins): ", timeArray)

    return [maxx, avg]


def parseURL(url):
    r = requests.get(url)
    temp = r.json()
    stringy = json.dumps(temp)
    stringy = json.loads(stringy)

    #print (stringy)

    import collections

    def Tree():
        return collections.defaultdict(Tree)
    
    pipeline = Tree()

    print("PIPELINE: ", pipeline)
    print("Commands: ", dir(pipeline))

    for each in stringy['downstreamProjects']:
        print(each)
        pipeline[each['name']] = [each['url']]
        stringyTime = each['url'] + "api/json?tree=builds[id,duration]"
        print(stringyTime)
        temp = parseBuild(stringyTime)
        pipeline[each['name']].append(temp)

    # AVERAGE THEN MAXX
    print("PIPELINEafter: ", pipeline)
    
parseURL(url1)

