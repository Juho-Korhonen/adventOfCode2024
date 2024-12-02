from reader import getData

data = getData("data.txt", "int")

totalSafeReports = 0

def returnListWithouth(withouthIndex, row):
    newRow = []
    for index, item in enumerate(row):
        if(index != withouthIndex):
            newRow.append(item)
    return newRow


rows = []
for row in data:
    rowModifications = []

    for indexToIgnore in range(0,len(row)): #loop through each index of row
        rowModifications.append(returnListWithouth(indexToIgnore, row))

    rows.append(rowModifications)


def isAnyLevelSafe(data):
    safeReports = 0
    unsafeReports = 0
    for row in data:
        previousItem = 0
        rowIsSafe = True
        isIncreasing = None 

        for index, item in enumerate(row):
            if(index == 1): # Set whether items need to decrease on Increase
                if(item - previousItem < 0):
                    isIncreasing = False
                else:
                    isIncreasing = True

            if(not index == 0): 
                sum = item - previousItem
                if((isIncreasing and sum < 0) or ((not isIncreasing) and sum > 0)): # Check if whole row is only decreasing / only increasing
                    rowIsSafe = False

                difference = abs(sum)
                if(not (3 >= difference >= 1)): # Check if (3 >= item >= 1)
                    rowIsSafe = False
            previousItem = item

        if(rowIsSafe):
            safeReports+=1
        else: 
            unsafeReports+=1

    return safeReports >= 1


for row in rows:
    if(isAnyLevelSafe(row)):
        totalSafeReports += 1

print(totalSafeReports)