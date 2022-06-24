def bubbleSort(aList):
    for passNumber in range (len(aList)-1,0,-1):
        for i in range(passNumber):
            if aList[i] > aList [i + 1]:
                temp = aList[i]
                aList[i] = aList[i +1]
                aList[i +1] = temp
    return aList

