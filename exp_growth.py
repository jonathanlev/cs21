#Jonathan Leventhal
#cs21 assignment#4
#program to calculate exponential growth

user_input = 'y' #value to control loop

#get values
while user_input == 'y' or user_input == 'Y':
    a = float(input('Initial quantity: '))
    r = float(input('Growth rate: '))
    x = int(input('Number of time intervals: '))

    #input validation
    while a < 0 or x < 0:
        print('Error: intial quantity and duration must be greater than 0.')
        a = float(input('Initial quantity: '))
        r = float(input('Growth rate: '))
        x = int(input('Number of time intervals: '))
    
    #calculation and display
    y = a*(1+r)**x
    print('After',x,'time periods, the new amount is',format(y,'.2f'))

    #continue
    user_input = input('Would you like to run again? (y/n)\n')
    if user_input == 'n' or user_input == 'N':
        quit()
