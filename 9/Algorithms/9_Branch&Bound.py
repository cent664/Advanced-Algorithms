import math
import time

files = ["xqf131.tsp", "xqg237.tsp", "pma343.tsp", "pka379.tsp", "bcl380.tsp", "pbl395.tsp", "pbk411.tsp","pbn423.tsp", "pbm436.tsp", "xql662.tsp"]
bestsol=[564,1019,1368,1332,1621,1281,1343,1365,1443,2513]

fpw=open("BranchandBound.txt","w")

def dis(c1, c2):
    xdistance = abs(c1[0] - c2[0])
    ydistance = abs(c1[1] - c2[1])
    distance = math.sqrt((pow(xdistance,2) + (pow(ydistance,2))))
    return distance

def Salesman(currentlocation, remaininglocations, cost):
    end = time.time()
    global costmin, start
    while 1:
        if end >= start + 300:
            return costmin
        if len(remaininglocations) == 0:
            leastcost = cost + dis(currentlocation, locationList[0])
            if costmin >= leastcost:
                costmin = leastcost
            return leastcost

        best = 99999999
        if (cost>best):
            return best

        for i in range(0, len(remaininglocations)):
            value = Salesman(remaininglocations[i], remaininglocations[0:i] + remaininglocations[i + 1:len(remaininglocations)],cost + dis(currentlocation, remaininglocations[i]))
            best = min(best, value)
        return best

if __name__ == '__main__':
    for i in range(0, len(files)):
        costmin = 99999999
        fp = open(files[i], "r")
        locationList = []
        for j in range(0, 8):
            fp.readline()
        for line in fp:
            point = line.split(" ")
            if (len(point) == 3):
                locationList.append([int(point[1]), int(point[2])])

        start = time.time()

        fpw.write(str((bestsol[i]/Salesman(locationList[0], locationList[1:len(locationList)], 0))))
        fpw.write("\n")