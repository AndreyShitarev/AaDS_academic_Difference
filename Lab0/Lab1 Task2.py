import time

def calc_fib(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a + b

    return b

start = time.perf_counter()

with open("inputLab1.txt", "r") as InputFile, open("outputLab2.txt", "w") as OutputFile:
    for line in InputFile:
        line = line.strip()
    splitted = line.split()
    n = int(splitted[0])
    result = calc_fib(n)
    OutputFile.write(str(result))

stop = time.perf_counter()

print(f"time of algorithm  {stop - start:.8f} secs")



