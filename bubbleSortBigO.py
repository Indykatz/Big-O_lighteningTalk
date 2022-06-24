def bubbleSort(aList):
    for passNumber in range (len(aList)-1,0,-1): # n(
        for i in range(passNumber):              # n(
            if aList[i] > aList [i + 1]:         # 1 +
                temp = aList[i]                  # 1 +   
                aList[i] = aList[i +1]           # 1 +      
                aList[i +1] = temp               # 1) 
    return aList

# T(n) = n(n(1 + 1 + 1 + 1))
# T(n) = n(n(4))
# T(n) = 4n^2
# O(n) = n^2