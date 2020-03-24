import sys
import requests as rq
from bs4 import BeautifulSoup

# Get the data from the command line argument URL
def getData(url):
    r = rq.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    spans = soup.find_all('div', {'class' : 'timestamp'})
    time = [span.get_text() for span in spans]

    name = soup.find('title').get_text()

    return time, name

def properFormat(h, m, s):
    q  = 0
    mi = 0

    totalHours   = sum(h)
    totalMinutes = sum(m)
    totalSeconds = sum(s)

    q = int(totalSeconds / 60)
    mi = totalSeconds % 60
    totalMinutes += q
    totalSeconds = mi

    q = int(totalMinutes / 60)
    mi = totalMinutes % 60
    totalHours += q
    totalMinutes = mi

    return [totalHours, totalMinutes, totalSeconds]

# extract the hours from the time list
def getHours(time):
    hours = []

    for t in time:
        if len(t) == 8:
            hours.append(int(t[0:2]))
        elif len(t) == 7:
            hours.append(int(t[0]))

    return hours

# extract the minutes from the time list
def getMinutes(time):
    minutes = []

    for t in time:
        if len(t) == 8:
            minutes.append(int(t[3:5]))
        elif len(t) == 7:
            minutes.append(int(t[2:4]))
        elif len(t) == 4:
            minutes.append(int(t[0]))
        elif len(t) == 5:
            minutes.append(int(t[0:2]))

    return minutes

# extract the seconds from the time list
def getSeconds(time):
    seconds = []

    for t in time:
        if len(t) == 8:
            seconds.append(int(t[6:]))
        elif len(t) == 7:
            seconds.append(int(t[5:]))
        elif len(t) == 5:
            seconds.append(int(t[3:]))
        elif len(t) == 4:
            seconds.append(int(t[2:]))

    return seconds

def Printer(name, length):
    print()
    print("Playlist Name: {}".format(name[0:len(name) - 10]))
    print("Playlist Length: {} Hours, {} Minutes, {} Seconds".format(length[0], length[1], length[2]))

# MAIN
URL = str(sys.argv[1])

if URL[0:32] == 'https://www.youtube.com/playlist':
    data, name = getData(URL)
    length = properFormat(getHours(data), getMinutes(data), getSeconds(data))
    Printer(name, length)
else:
    print('Not A Valid Link')

#TODO:
# Number of videos
# Visualizer?
