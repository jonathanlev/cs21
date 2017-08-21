#Jonathan Leventhal
#cs21 assignment3
#youngest child

#intro
print('Please enter the three ages, in any order.')

#get ages
first_child = int(input('What is the age of the first child? '))
second_child = int(input('What is the age of the second child? '))
third_child = int(input('What is the age of the third child? '))

#display in ascending order
if first_child < second_child and first_child < third_child:
    youngest = first_child
elif second_child < first_child and second_child < third_child:
    youngest = second_child
else:                  
    youngest = third_child

if first_child > second_child and first_child > third_child:
    oldest = first_child
elif second_child > first_child and second_child > third_child:
    oldest = second_child
else:
    oldest = third_child

if first_child > second_child and first_child < third_child:
    middle = first_child
elif first_child < second_child and first_child > third_child:
    middle = first_child
elif second_child > first_child and second_child < third_child:
    middle = second_child
elif second_child < first_child and second_child > third_child:
    middle = second_child
else:
    middle = third_child
    
print('Ascending order: ',youngest,',',middle,',',oldest)

#get youngest childs name
youngest_name = input('What is the youngest childs name? ')

#display candle-lighter!
print('\n',youngest,'-year-old ',youngest_name,' gets to light the candles!',sep='')
