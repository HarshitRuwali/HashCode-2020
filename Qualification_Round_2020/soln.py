
def solve(MAX, inputList):
    currentLibrary = []
    max_score = 0
    startIndex = []
    currentValue = []

    sum = 0
    startIndex = fullSize   

    libraryindex = []
    libraryscanning = []

    while(len(startIndex)> 0 and len(currentLibrary)>0):
        startIndex = startIndex - 1
        for i in range(startIndex, -1, -1):

            currentValue = inputList[i]

            tempSum = sum + currentValue 

            if (tempSum == MAX):  
                sum = tempSum
                currentIndexList.append(i) 
                currentValueList.append(currentValue)
                break

            elif (tempSum > MAX):
                continue  

            elif (tempSum < MAX):
                sum = tempSum
                currentIndexList.append(i) 
                currentValueList.append(currentValue) 
                continue  
        if (maxScore < sum):
            maxScore = sum 

            solutionIndexList = []
            solutionValueList = []

            for y in currentIndexList:
                solutionIndexList.append(y)  
            for y in currentValueList:
                solutionValueList.append(y) 

        if (maxScore == MAX):
            break 

        if(len(currentValueList) != 0):
            lastVal = currentValueList.pop()
            sum = sum - lastVal 

        if(len(currentIndexList) != 0):
            lastIndex = currentIndexList.pop() 
            startIndex = lastIndex 

        if(len(currentIndexList) == 0 and (startIndex == 0)): 
            break

    print("SCORE = " + str(maxScore))  

    return solutionIndexList  


def process(fileName):

    print("######")
    print(fileName)
    print("######")

    inputFile = open(fileName + ".txt", "rt")

    #  Reading file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()

    print("INPUT")
    print(firstLine)
    print(secondLine)

    #  Assigning parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Creating the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)
       
    print("")
    print("OUTPUT")
    print(len(outputList))

    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    #os.mkdir(outputFile) 
    outputFilesDirectory = "Output/"

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()

    inputFilesDirectory = "Input/"  
   

fileNames = ["a_example", "b_read_on", "c_incunabula",
             "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]  

for fileName in fileNames:  
    process(fileName)
