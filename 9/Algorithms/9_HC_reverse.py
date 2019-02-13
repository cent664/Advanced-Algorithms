import math
import random
import time

files = ["xqf131.tsp", "xqg237.tsp", "pma343.tsp", "pka379.tsp", "bcl380.tsp", "pbl395.tsp", "pbk411.tsp", "pbn423.tsp", "pbm436.tsp", "xql662.tsp"]
bestsol = [564, 1019, 1368, 1332, 1621, 1281, 1343, 1365, 1443, 2513]

fpw = open("Reverse.txt", "w")

def dis(c1, c2):
    xdistance = abs(c1[0] - c2[0])
    ydistance = abs(c1[1] - c2[1])
    distance = math.sqrt((pow(xdistance, 2) + (pow(ydistance, 2))))
    return distance

def Salesman(CityList):
    end = time.time()
    newbest = 99999999
    currentbest = 99999999
    global costmin, start
    while 1:
        if end >= start + 300:
            return costmin

        random.shuffle(CityList)

        for i in range(0, len(CityList)-1):
            distanceHC = dis(CityList[i], CityList[i+1])
            currentbest = currentbest + distanceHC

        index1 = random.randint(0, len(CityList) - 1)
        index2 = random.randint(0, len(CityList) - 1)

        if index1 > index2:
            front = CityList[0:index2]
            back = CityList[index1:]
            middle = CityList[index2:index1]

        else:
            front = CityList[0:index1]
            back = CityList[index2:]
            middle = CityList[index1:index2]
        middle.reverse()
        new_city = front + middle + back

        for i in range(0, len(CityList)-1):
            distanceHC = dis(CityList[i], CityList[i+1])
            newbest = newbest + distanceHC
        if newbest < currentbest:
            CityList = new_city
            currentbest = newbest
        else:
            middle.reverse()
            new_city = front + middle + back

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

        fpw.write(str((bestsol[i] / Salesman(locationList))))
        fpw.write("\n")