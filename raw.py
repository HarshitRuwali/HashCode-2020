def solve(MAX, inputList):

    currentIndexList = [] 
    currentValueList = []
    solutionIndexList = [] 
    solutionValueList = [] 

    fullSize = len(inputList)

    startIndex = fullSize 
    maxScore = 0 
    sum = 0

    while((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

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
        if (maxScore < sum):  # If currently generated solution has the best score
            maxScore = sum  # Save its value

            solutionIndexList = []
            solutionValueList = []

            for y in currentIndexList:
                solutionIndexList.append(y)  
            for y in currentValueList:
                solutionValueList.append(y) 

        if (maxScore == MAX):  # If current solution is the perfect solution
            break 
        if(len(currentValueList) != 0):
            lastVal = currentValueList.pop() # Remove the last element from current values
            sum = sum - lastVal # Subtract it from sum

        if(len(currentIndexList) != 0):
            lastIndex = currentIndexList.pop() # Remove the last element from current indexes
            startIndex = lastIndex # Make it as the starting index for the next iteration

        if(len(currentIndexList) == 0 and (startIndex == 0)): # If solution generating is almost finished
            break # Stop solution generating

    print("SCORE = " + str(maxScore))     # Print the score of the best solution

    return solutionIndexList  # Return indexes list of the best solution


def process(fileName):

    # Print data to console
    print("")
    print("#####")
    print(fileName)
    print("#####")

    #  Read the open file by name
    inputFile = open(inputFilesDirectory + fileName + ".in", "rt")

    #  Read file
    firstLine = inputFile.readline()
    secondLine = inputFile.readline()
    inputFile.close()


    #  Print input data
    print("INPUT")
    print(firstLine)
    print(secondLine)

    #  Assign parameters
    MAX, NUM = list(map(int, firstLine.split()))

    #  Create the pizza list by reading the file
    inputList = list(map(int, secondLine.split()))

    outputList = solve(MAX, inputList)  # Solve the problem and get output
       
    print("")
    print("OUTPUT")
    print(len(outputList))

    outputString = ""
    for l in outputList:
        outputString = outputString + str(l) + " "
    print(outputString)

    outputFile = open(outputFilesDirectory + fileName + ".out", "w")
    outputFile.write(str(len(outputList)) + "\n")
    outputFile.write(outputString)
    outputFile.close()


inputFilesDirectory = "Input/"  
outputFilesDirectory = "Output/" 

fileNames = ["a_example", "b_small", "c_medium",
             "d_quite_big", "e_also_big"]  


for fileName in fileNames:  # Take each and every file and solve
    process(fileName)
    #fileName(open)