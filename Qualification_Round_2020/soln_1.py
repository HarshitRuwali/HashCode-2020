def(MAX, ):
    day = []
    maxsum = []
    



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
