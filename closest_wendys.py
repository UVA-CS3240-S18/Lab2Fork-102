# Mark Sherriff (mss2x)

import math
import webbrowser

google_maps_url = "https://www.google.com/maps/@35.372742,-81.954957,15z?hl=en"

def distance_between(lat_1, lon_1, lat_2, lon_2):
    theta = lon_1 - lon_2
    dist = math.sin(lat_1 * math.pi / 180.0) * math.sin(lat_2 * math.pi / 180.0) + math.cos(lat_1 * math.pi / 180.0) * math.cos(lat_2 * math.pi / 180.0) * math.cos(theta * math.pi / 180.0)
    dist = math.acos(dist)
    dist = dist * 180.0 / math.pi
    dist = dist * 60 * 1.1515

    return dist

#lat = float(input("Current latitude: "))
#lon = float(input("Current longitude: "))

lat = 38.0322727
lon = -78.50997339999999
datafile = open("wendys.csv", "r")

closest_dist = 200
closest_wendys = ""


for line in datafile:
    entry = line.split(";")
    dist_to_wendys = distance_between(lat, lon, float(entry[0]), float(entry[1]))
    if dist_to_wendys < closest_dist:
        splitaddress = str(entry[4]).split()
        fulladdress = ""
        for i in range(len(splitaddress)):
            if i == 0:
                fulladdress += splitaddress[i]
            else:
                fulladdress += "+" + splitaddress[i]
        splitcity = str(entry[5]).split()
        fullcity = ""
        if len(splitcity) <= 1:
            fullcity = splitcity[0]
        else:
            for i in range(len(splitcity)):
                if i == 0:
                    fullcity += splitcity[i]
                else:
                    fullcity += "+" + splitcity[i]
        closeststate=str(entry[6])
        closest_dist = dist_to_wendys
        closest_wendys = entry[2]
google_maps_url = "https://www.google.com/maps?q=" + fulladdress + "+" + fullcity + "+" + closeststate
print(google_maps_url)

datafile.close()

print("The closest Wendy's (", closest_wendys, ") is", closest_dist, "miles away.")
google_maps_url = google_maps_url.replace(' ', '+')
webbrowser.open(google_maps_url)

