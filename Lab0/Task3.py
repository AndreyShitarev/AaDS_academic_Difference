import time

def LastDigit(n):
    if n ==0:
        return 0

    n = n % 60 # áåð¸ì îñòàòîê îò äåëåíèÿ íà 60, òàê êàê ïîñëåäíÿÿ öèôðà ÷èñëà ôèááîíà÷è öèêëè÷íà ïî ïåðèîäó 60

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10

    return b

start = time.perf_counter()

with open("inputLab1.txt", "r") as InputFile, open("outputLab2.txt", "w") as OutputFile:
    for line in InputFile:
        line = line.strip()

        splited = line.split()
        n = int(splited[0])
        result = LastDigit(n)
        OutputFile.write(str(result))

stop = time.perf_counter()

print(f"time of algorithm  {stop - start:.8f} secs")


