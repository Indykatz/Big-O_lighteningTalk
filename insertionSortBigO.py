def insertionSort(aList):
    for index in range(1, len(aList)):                              # n(
        currentValue = aList[index]                                 # 1 +
        position = index                                            # 1 +
        while position > 0 and aList[position] > currentValue:      # n(
            aList[position] = aList[position - 1]                   # 1 +
            position = position -1                                  # 1 +
        aList[position] = currentValue                              # 1))
    return aList

# T(n) = n(1 + 1 + n(1 + 1 + 1))
# T(n) = n(2 + n(3))
# T(n) = n(2 + 3n)
# T(n) = 2n + 3n^2
# O(n) = n^2
