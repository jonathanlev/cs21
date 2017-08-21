#Jonathan Leventhal
#cs21 assignment#10
#program electoral_dictionaries

import myfns

states_dictionary = myfns.make_elector_dictionary('electoralvotes.txt')
total = 0

for item in states_dictionary:
    total += int(states_dictionary[item][1])
    
wintotal = int(total/2)+1
print('The total number of electoral votes is',total)
print('The total number of electoral votes needed to win is',wintotal)
print()

user_input = ' '
while user_input != "":
    user_input = input('Choose a state or hit enter when done: ')
    if user_input in states_dictionary:
        print('Population:',states_dictionary[user_input][0],'\tElectoral votes:',states_dictionary[user_input][1],'\n')
    elif user_input not in states_dictionary and user_input != "":
        print('Try again, Not a valid state name.\n')
    else:
        print('\nThanks for using my program.')
    

