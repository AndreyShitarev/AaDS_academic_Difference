def Sum1 (a, b):
    return a + b

def Sum2 (a, b):
    return a + b**2

with open("inputLab1.txt", "r") as InputFile, open("outputLab2.txt", "w") as OutputFile:
    for line in InputFile:
        line = line.strip()

        splited = line.split()
        FirstNumber = int(splited[0])
        SecondNumber = int(splited[1])

        result = Sum1(FirstNumber, SecondNumber)
      # result = Sum2(FirstNumber, SecondNumber) # Если нужен вариант для суммы a + b**2
        OutputFile.write(str(result)) 
