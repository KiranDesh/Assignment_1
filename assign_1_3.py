#3.	Accept number of rows from end user and print following * asterisk pattern 
star = int(input("Enter number of rows of star you want to print: "))
for i in range(star,0,-1):
    print(i*'*')
    
    
#OR

star = int(input("Enter number of rows of star you want to print: "))
for i in range(0,star):
    for j in range(star-i,0,-1):
        print('*',end='')
    print()