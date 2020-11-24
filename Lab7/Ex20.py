'''
Write a program that converts a time from one time zone to another. 
The user enters the timein the usual American way, such as 3:48pm or 
11:26am. The first time zone the user enters is that of the original
time and the second is the desired time zone. The possible time zones 
are Eastern, Central, Mountain, or Pacific.
'''
# Time zone differences:
# pacific = 0
# mountain = 100
# central = 200
# eastern = 300

timeZones = ["pacific", "mountain", "central", "eastern"]

inp = input("Enter time: ")
zone = input("Enter source timezone: ")
target = input("Enter target timezone: ")

splTime = inp.split(":")
time = int(splTime[0] + splTime[1][0:2])
am = True if splTime[1][2] == "a" else False
time += 0 if am else 1200
time -= 1200 if time > 1200 and am else 0

sindex = timeZones.index(zone.lower())
dindex = timeZones.index(target.lower())
if (sindex != -1 and dindex != -1):
    time += (dindex - sindex) * 100
    time %= 2400
    am = True if time < 1200 else False
    time %= 1200
    strTime = str(time) if time >= 1000 else "0" + str(time)
    print(f"{strTime[0:2]}:{strTime[2:4]}{'am' if am else 'pm'}")
