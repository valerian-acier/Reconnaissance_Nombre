import random
import copy
import math

def isIn(ltabou, v):
    for l in ltabou:
        found = True
        if l == []:
            continue
        for i, x in enumerate(l):
            if x != v[i]:
                found = False
                break
        if found:
            return True
    return False

def tabouCalcul(variablesCount, evaluate):

    # Hyperparameters
    ltabouSize = 10

    ltabou = [[] for i in range(ltabouSize)]

    current = [1 for i in range(variablesCount)]

    notProgressing = 0
    a = 0
    minBorne = -3
    maxBorne = 200

    currentBest = current
    currentBestValue = -9999999999

    while(notProgressing < 100000):

        newCurrent = []
        best = -99999999999

        cmp = 0

        while cmp < 20:
            r = random.randint(0, len(current)-1)
            was = current[r]
            if (r%1):
                current[r] = random.uniform(0,1)
            else:
                current[r] = random.randint(minBorne, maxBorne)
            if isIn(ltabou, current) == False:
                cmp += 1
                tmp = evaluate(current)
                # print(tmp, current)
                if tmp > best:
                    best = tmp
                    newCurrent = copy.deepcopy(current)
            current[r] = was

        current = newCurrent
        print(best, current)

        ltabou[a] = copy.deepcopy(current)
        a += 1
        a = a % ltabouSize

        if best > currentBestValue:
            print("best:", best, current)
            notProgressing = 0
            currentBestValue = best
            currentBest = newCurrent
        if notProgressing > 100 and notProgressing%100 == 0:
            if random.randint(0, 1) == 1:
                current = [1 for _ in range(len(current))]
            else:
                current = currentBest
            print("Reset !")
        notProgressing += 1
    print("Current best :", currentBest, "with", currentBestValue)
    return