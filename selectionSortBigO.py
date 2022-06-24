def selectionSort(aList):
    for endSlot in range (len(aList) -1, 0, -1):            # n(
        positionOfMax = 0                                   # 1 +
        for location in range(1, endSlot + 1):              # n(
            if aList[location] > aList[positionOfMax]:      # 1 + 
                positionOfMax = location                    # 1 +
        temp = aList[endSlot]                               # 1 +
        aList[endSlot] = aList[positionOfMax]               # 1 +
        aList[positionOfMax] = temp                         # 1 ))
    return aList

#  T(n) = n(1 + n( 1 + 1 + 1 + 1 + 1))
#  T(n) = n(1 + n(5))
#  T(n) = n(n(5))
#  T(n) = 5n^2
#  O(n) = n^2