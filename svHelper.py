import re

# this program converts from data stream to structural
def convertToStructural(inputline):
    #keytypes = ["~","|","&"]
    inputsA = re.sub("[assign,; ]", "",inputline)
    processInput = re.split("[&|~=]",inputsA)
    # for i in range(len(inputs)):
    # finalSet = inputs[0]
    
    stringVar = ""
    outputLines = ""
    andStatement = "and A%s(%s,%s,%s)"
    orStatement = "or O%s(%s,%s,%s)"
    notStatement = "not N%s(%s,%s)"
    wire = "w%s"
    wireBuild = "wire "
    print (inputsA) 
    imod = 0
    for i in range(1,len(processInput)-1):
        pos = inputsA.find(processInput[i],imod,len(inputsA))
        if pos!=-1:
            var = inputsA[pos + len(processInput[i])]
            print(inputsA[pos + len(processInput[i])])
            if var == "&" and i<len(processInput)+1:
                wireBuild += wire %(i) + ", "
                outputLines += andStatement%(i,processInput[i],processInput[i+1],wire %(i)) + "\n"

            
        imod += len(processInput[i])

    # for i in range(1,len(processInput)-1):
    #     pos = inputsA.find(processInput[i],imod,len(inputsA))
    #     if pos!=-1:
    #         var = inputsA[pos + len(processInput[i])]
    #         print(inputsA[pos + len(processInput[i])])
    #         if var == "|" and i<len(processInput)+1:
    #             wireBuild += wire %(i) + ", "
    #             outputLines += orStatement%(i,processInput[i],processInput[i+1],wire %(i)) + "\n"

            
    #     imod += len(processInput[i])
            
    print(wireBuild)
    print(outputLines)
    return outputLines

if __name__ == "__main__":
    print(convertToStructural("assign F[3] = A[3]&A[2]&A[1]|A[2];"))