import math

print ("Welcome to the simple Trigonometry helper.")

print ("Would you like to do. (Enter the number corresponding to the function:)")

print("1.sin")
print("2.cos")
print("3.tan")

trig = input ("Which function would you like to use? 1, 2, or 3?")

if trig=='1':
    a= eval(input("Enter the number to sine:"))
    print (math.sin(a))

if trig=='2':
    b= eval(input("Enter the number to cosine:"))
    print (math.cos(b))

if trig=='3':
    c= eval(input("Enter the number to tangent:"))
    print (math.tan(c))
