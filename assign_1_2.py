#2.	Accept number of rows from end user and print following * asterisk 
star = int(input("Enter number of rows of star you want to print: "))
for i in range(star+1):
    print('*'*i)
    
#OR

star = int(input("Enter number of rows of star you want to print: "))
for i in range(0,star+1):
    for j in range(i,0,-1):
        print('*',end='')
    print()