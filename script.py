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
        print("You inputted version : ", sys.argv[1])
        version = sys.argv[1]
except:
    pass

def parseURL(url):
    r = requests.get(url)
    temp = r.json()
    stringy = json.dumps(temp)
    stringy = json.loads(stringy)
    maxx = 0
    avg = 0
    timeArray = []

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

def scanBirstJenkins():
    biggestMax = 0
    totalAvg = 0
    counter = 0

    maxArray = []
    avgArray = []

    with open('seleniumURLS2.txt') as fp:
        for eachURL in fp:
            suffix = "api/json?tree=builds[id,duration]"
            eachURL = eachURL + suffix
            eachURL = eachURL.replace("\n", "")

            eachURL = eachURL.replace("7.1.4", version)

            print("\n", eachURL)
            try:
                parseURLValues = parseURL(eachURL)

                maxArray.append(parseURLValues[0])
                avgArray.append(round(parseURLValues[1], 4))

                if biggestMax < parseURLValues[0]:
                    biggestMax = parseURLValues[0]
                totalAvg += parseURLValues[1]
                counter += 1

            except:
                continue
    try:
        print("TotalAVG: ", totalAvg)
        print("COUNTER: ", counter)
        totalAvg /= counter
    except:
        totalAvg = 0

    print("\n\n~~DONE SCANNING ALL BUILDS~~ ~~DONE SCANNING ALL BUILDS~~ ~~DONE SCANNING ALL BUILDS~~")
    print("PLEASE FOLLOW ME ON SOCIAL MEDIA\n@BynLeung and uhhh other stuff.\n\n")
    print("LONGEST BUILD (mins): ", round(biggestMax, 3))
    print("TOTAL AVG RUNTIME (mins): ", round(totalAvg, 3))
    print("SORTED ARRAY OF MAXXXES: ", sorted(maxArray))
    print("SORTED ARRAY OF AVERAGES: ", sorted(avgArray))
    

scanBirstJenkins()


