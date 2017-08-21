#Jonathan Leventhal
#cs21 assignment3
#egg counter

#intro
print('This program will return the required number of 1-dozen egg cartons.')

#constants
EGGS_PER_DOZEN = 12

#get number of eggs
collected_eggs = int(input('How many eggs were collected today? '))

#validate input (error check)
if collected_eggs < 0:
    print('Your value cannot be negative.')
else:
    #return how cartons will be used
    carton_total = collected_eggs // EGGS_PER_DOZEN
    print('We will pack your',collected_eggs,'eggs into',carton_total,'cartons.') 
    
    #reutrn egg remainder
    remainder = collected_eggs % EGGS_PER_DOZEN
    print('There will be',remainder,'eggs left over.')


