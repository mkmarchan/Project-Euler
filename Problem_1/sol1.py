#!$PATH:/c/Python27

f = open("output.txt", "w");

sum = 0

for i in range(1000/3 + 1):
    sum += i*3
    print i*3

for i in range(1000/5):
    if(i % 3 != 0):
        sum += i*5
    	print i*5

f.write(str(sum))
