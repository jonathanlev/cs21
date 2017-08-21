#Jonathan Leventhal
#cs21 assignment#4
#salary compunded daily

#constants
WAGE = .01

#intro
print('This program will calculate your daily wage and total salary.')
print('Your wage starts at $',WAGE,'and compunds daily.\n')

#get days
days_worked = int(input('Enter days worked: '))

#salary
salary = WAGE
salary_total = 0
                        
#display table with salary each day and total pay
print(' Day       Amount($)')
print(' ---      ----------')
for i in range(1,days_worked+1,1):
    print(format(i,'3.0f'),end=' ')
    print(format(salary,'13.2f'))
    salary_total+=salary
    salary = (salary*2)

#return total pay
print('\nYour total pay over',days_worked,'days was $',format(salary_total,'.2f'))

#calculate and return avg daily wage
avg_daily_wage = salary_total/days_worked
print('\nAverage daily wage = $',(format(avg_daily_wage,'.2f')))
