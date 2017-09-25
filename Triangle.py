print ("This program will determine if three lengths can form a Triangle.")

a = int (input ("Enter length 1:"))

b = int (input ("Enter length 2:"))

c = int (input ("Enter length 3:"))

if a > (b + c) or b > (a + c) or c > (a + b):
    print ('No')
else:
    print ('Yes')
