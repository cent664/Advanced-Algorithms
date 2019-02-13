import random

if __name__ == '__main__':

    rand = []
    state = 1
    p = 0.5
    for i in range(0,10000000):
        temp = random.uniform(0,1)
        if (temp > p):
            if not state:
                state = 1
            else:
                state = 0
            rand.append(state)
        if (temp < p):
            rand.append(state)

    randstr = ''.join(str(e) for e in rand)

    fs = open("state.txt", "w")

    fs.write(randstr)
    fs.write("\n")

    fs.close()

