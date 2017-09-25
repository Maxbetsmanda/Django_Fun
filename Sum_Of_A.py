print ("This program will sum a series of numbers.")

a=1
sumofinput = 0
while a != 0:
    print ("Enter the next number (enter 0 when finished)")
    a = eval(input())
    sumofinput += a

print ("The sum of your numbers is", str(sumofinput))
