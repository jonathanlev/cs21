#Adam Sminkey and Jonathan Leventhal
#CS21
#Program to compute leap year, part B

#Adam Sminkey and Jonathan Leventhal
#CS21
#Program to compute leap year, part A

#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)

year=int(input('Enter a year: '))

if year<=0:
    print('ERROR: Enter a positive number.')

elif year%4!=0:
    print(year,'is a common year')

elif year%100!=0:
    print(year,'is a leap year')

elif year%400!=0:
    print(year,'is a common year')
    
else:
     print(year,'is a leap year')
     
