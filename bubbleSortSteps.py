

def bubbleSort(aList):
    steps = 0
    for passNumber in range (len(aList)-1,0,-1):
        steps += 1
        for i in range(passNumber):
            steps += 1
            if aList[i] > aList [i + 1]:
                steps += 1
                temp = aList[i]
                steps += 1
                aList[i] = aList[i +1]
                steps += 1
                aList[i +1] = temp
                steps += 1
        steps += 1
    return steps

randonNumbers = [86,25, 24, 52, 10, 99, 68, 44, 67, 5]
print(bubbleSort(randonNumbers))

randonNumbersSorted = [5, 10, 24, 25, 44, 52, 67, 68, 86, 99]
print(bubbleSort(randonNumbersSorted))

randonNumbersSortedReverse = [99, 86, 68, 67, 52, 44, 25, 24, 10, 5]
print(bubbleSort(randonNumbersSortedReverse))


