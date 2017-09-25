
def table (rows, columns):
    line = ""
    dashes = ""
    for column in range (1,10):
        line = line + str(column) + "\t"
        dashes = dashes + "--------"
    print ("*  |" + "\t" + line)
    print ("---+" + dashes)

       
    for row in range (1,10):
        line = " "
        for column in range (1,10):
            line = line + str(row * column) + "\t"
        print (str(row) + "  |" + "\t" + line)
        
    print ("Finished...")
table (9,9)
 
        
