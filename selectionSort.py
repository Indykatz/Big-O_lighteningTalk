def selectionSort(aList):
    for endSlot in range (len(aList) -1, 0, -1):
        positionOfMax = 0
        for location in range(1, endSlot + 1):
            if aList[location] > aList[positionOfMax]:
                positionOfMax = location
        temp = aList[endSlot]
        aList[endSlot] = aList[positionOfMax]
        aList[positionOfMax] = temp
    return aList

