# pattern.py
# 1
for i in range (0,4):#for rows
    for j in range (0,4):# for columns
        print("*",end="")
    print("")
  
# Right angled triangle
for i in range (0,5):# rows
    for j in range (0,i+1):# columns
        print("*",end="")
    print("")# next line
 
# number-right angled triangle 
for i in range (1,5):# i=1,2,3,4   rows
    for j in range (1,i+1):# j=1 to i+1     columns
        print(j,end="")
    print("")

    
for i in range (1,5):# rows
    for j in range (1,i+1):# colums
        print(i,end="")
    print("")

# inverted star triangle
for i in range (5,0,-1):
    for i in range (i):
        print("*",end="")
    print("")



# inverted number triangle
for i in range (5,1,-1):
    for j in range (1,i):
        print(j,end="")
    print("")



    
