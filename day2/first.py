from reader import getData

data = getData("data.txt", "int")

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

print(safeReports, unsafeReports)