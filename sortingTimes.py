from audioop import reverse
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
import time

def sortingRace(aList):
    totalStartTime = time.time()
    # Bubble Sort
    bubbleStartTime = time.time()
    bubbleSort(aList)
    bubbleEndTime = time.time()
    bubbleTime = (bubbleEndTime - bubbleStartTime) * 1000
    # Selection Sort
    selectionStartTime = time.time()
    bubbleSort(aList)
    selectionEndTime = time.time()
    selectionTime =(selectionEndTime - selectionStartTime) * 1000
    # insertion Sort
    insertionStartTime = time.time()
    bubbleSort(aList)
    insertionEndTime = time.time()
    insertionTime = (insertionEndTime - insertionStartTime) * 1000
    # end and print
    totalEndTime = time.time()
    sortedFunctionStartTime = time.time()
    sortedList = sorted(aList)
    sortedFunctionEndTime = time.time()
    sortedTime = (sortedFunctionEndTime - sortedFunctionStartTime) * 1000
    print(f"Bubble Sort: {bubbleSort(aList)} {bubbleTime}")
    print(f"Selection Sort: {selectionSort(aList)} {selectionTime}")
    print(f"Insertion Sort: {insertionSort(aList)} {insertionTime}")
    print(f"Sorted: {sortedList} {sortedTime}")
    # OOO Lets sort them 
    sortingAgain =  {"Bubble":bubbleTime, "Selection": selectionTime,"Insertion": insertionTime, "Sorted": sortedTime }
    sortedAgain = sorted(sortingAgain, key=sortingAgain.get)
    newSorted = {}
    for i in sortedAgain:
        newSorted[i] = sortingAgain[i]
    print(f"Ta da - all sorted: {newSorted}")
    print(f"Total time: {(totalEndTime - totalStartTime)  * 1000}")


# randonNumbers = [86,25, 24, 52, 10, 99, 68, 44, 67, 5]
# sortingRace(randonNumbers)
secongList = [86,25, 24, 52, 10, 99, 68, 44, 67, 5, 50, 67, 44, 86, 99, 1, 25, 42, 52, 68]
sortingRace(secongList)
# print("Sorted")
# randonNumbersSorted = [5, 10, 24, 25, 44, 52, 67, 68, 86, 99]
# sortingRace(randonNumbersSorted)
# randonNumbersSortedReverse = [99, 86, 68, 67, 52, 44, 25, 24, 10, 5]
# sortingRace(randonNumbersSortedReverse)
