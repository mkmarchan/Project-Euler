def isPrime(num, primeArray):
    for i in primeArray:
	if num % i == 0:
	    return False
    return True

primeArray = [3]

f = open("output.txt", "w")

num = 5
sum = 5
f.write(str(1) + "\n")
while num < 20000:
    if isPrime(num, primeArray):
    	f.write(str(num - primeArray[len(primeArray) - 1]) + "\n")
	primeArray.append(num)
	sum += num
#	print "current num: " + str(num) + " current sum: " + str(sum)
    num += 2
# print "current num: " + str(num) + " current sum: " + str(sum)
