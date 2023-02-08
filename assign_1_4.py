#4.	Accept number of rows from end user and print following * asterisk pattern ( equilateral triangle )
star = int(input("Enter number of rows of star you want to print: "))
for i in range(0,star,2):
    for j in range(1,star-i):
        print(' ',end='')
    for k in range(0,i+1):
        print('* ',end='')
    print()