#9.	Accept number of rows and columns form end user and print following pattern e.g. if row = 5 and column = 5 then
star_row = int(input("Enter number of rows of star you want to print: "))
star_column = int(input("Enter number of columns of star you want to print: "))

for i in range(star_row):
    for j in range(star_column):
        print('*',end='')
    print()