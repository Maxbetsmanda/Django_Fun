def main_Program():
    print ("This Program will implement the Triangle Classification Algorithm")

    i = eval(input("Enter the length of side # 1: "))
    j = eval(input("Enter the length of side # 2: "))
    k = eval(input("Enter the length of side # 3: "))
    
    result = tri_Class(i, j, k)
    print (result, "****")



def tri_Class(i, j, k):

    if i<=0 or j<=0 or k<=0:
        print ("This can NOT form a triangle")
        return 4

    else:
        tri = 0

        if i == j:
            tri = tri + 1

        if i == k:
            tri = tri + 2

        if j == k:
            tri = tri + 3
        if tri == 0:

            if i + j <= k or j + k <= i or i + k <= j:
                tri = 4
                print ("This can NOT form a triangle")
                return tri
            else:
                tri = 1
                print ("This is a scalene triangle")
                return tri

        if tri > 3:
            tri = 3
            print ("This is an equilateral triangle")
            return tri

        if tri == 1 and i + j > k:
            tri = 2
            print ("This is an isosceles triangle")
            return tri


        if tri == 2 and i + k > j:
            tri = 2
            print ("This is an isosceles triangle")
            return tri


        if tri == 3 and j + k > i:
            tri = 2
            print ("This is an isosceles triangle")
            return tri


        else:
            tri = 4
            print ("This can NOT form a triangle")
            return tri



main_Program()






