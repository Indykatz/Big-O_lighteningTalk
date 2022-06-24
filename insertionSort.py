def insertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position = index
        while position > 0 and aList[position] > currentValue:
            aList[position] = aList[position - 1]
            position = position -1 
        aList[position] = currentValue
    return aList

