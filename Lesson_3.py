#creat a list of leap year using a loop from 1980-2020.
year = range(1980, 2021)
for y in year:
     if y % 4 == 0 and (y % 100 !=0 or y % 400 == 0):
        print (y)