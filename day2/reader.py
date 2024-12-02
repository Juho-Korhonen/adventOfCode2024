# returnType must be int, double or str

def turnDataCorrectType(datapoint, returnType):
    if(returnType == "int"):
        return int(datapoint)
    elif(returnType == "float"):
        return float(datapoint)
    elif(returnType == "str"):
        return str(datapoint)

def getData(filepath, returnType):
    file = open(filepath, "r")
    lines = file.readlines()

    formattedData = []

    for line in lines:
        line = line.replace("\n", "")
        dataAsArray = line.split(" ")
        dataAsCorrectType = []
        for datapoint in dataAsArray:
            dataAsCorrectType.append(turnDataCorrectType(datapoint, returnType))
        formattedData.append(dataAsCorrectType)

    return formattedData


# Will turn 

# 7 2 3 4
# 5 2 3 1
# 3 1 2 3

# To

# [[7, 2, 3, 4],
#  [5, 2, 3, 1],
#  [3, 1, 2, 3]]

# if returnType is int
