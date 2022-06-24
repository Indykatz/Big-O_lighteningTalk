
def bubbleSort(aList):
    outerloopCount = 0
    innerloopCount = 0
    steps = 0
    print(aList)
    for passNumber in range (len(aList)-1,0,-1):
        steps += 1
        print(f"Number to pass: {aList[passNumber]}")
        input("Press enter to continue")
        outerloopCount += 1
        print(f"Outerloop Iteration No: {outerloopCount}")
        input("Press enter to continue")
        for i in range(passNumber):
            steps += 1
            innerloopCount += 1
            print(f"Innerloop Iteration No: {innerloopCount}")
            input("Press enter to continue")
            print(f"Value of i on this iteration: {aList[i]}")
            input("Press enter to continue")
            if aList[i] > aList [i + 1]:
                steps += 1
                print("Exchange found")
                temp = aList[i]
                steps += 1
                aList[i] = aList[i +1]
                steps += 1
                aList[i +1] = temp
                steps += 1
                print(f"Exchange made {aList}")
        steps += 1
    print (f"Sorted list {aList}") 
    print (f"Outerloop Iterations {outerloopCount}")
    print (f"Innerloop Iterations {innerloopCount}")
    print (f"Steps {steps}")

# randonNumbers = [86,25, 24, 52, 10, 99, 68, 44, 67, 5]
# print(bubbleSort(randonNumbers))

randonNumbersSorted = [5, 10, 24, 25, 44, 52, 67, 68, 86, 99]
print(bubbleSort(randonNumbersSorted))