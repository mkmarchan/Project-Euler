import math

num = 600851475143
i = 2
while(i < math.sqrt(num)):
    while(num % i == 0):
    	num /= i
    i += 1
print num
