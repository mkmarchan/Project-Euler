import math

def isPrime(num, primeArray):
    for i in range(len(primeArray) -1):
        if (num % primeArray[i] == 0):
	    return False
	if primeArray[i] > math.sqrt(num):
	    i = len(primeArray)
    return True

primeArray = [2, 3]
num = 5
while len(primeArray) < 10001:
    if isPrime(num, primeArray):
        primeArray.append(num)
    num += 2
print primeArray[len(primeArray)-1]
