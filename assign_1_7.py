#7.	Accept number of rows from end user and print following * asterisk pattern ( half diamond – right )
star = int(input("Enter number of rows of star you want to print: "))
for i in range(star):
    print('*'*i)
for i in range(star,0,-1):
    print('*'*i)