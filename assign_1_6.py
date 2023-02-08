#6.	Accept number of rows from end user and print following * asterisk pattern ( full diamond )
star = int(input("Enter number of rows of star you want to print: "))
for i in range(0,star-1,2):
    for j in range(1,star-i):
        print(' ',end='')
    for k in range(i+1):
        print('* ',end='')
    print()
for i in range(1,star+1,2):
    for j in range(i-1):
        print(' ',end='')
    for k in range(star-i+1):
        print('* ',end='')
    print()