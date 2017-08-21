#Jonathan Leventhal
#cs21 assignment#10
#program electoral_sets

import myfns

states_dictionary = myfns.make_elector_dictionary('electoralvotes.txt')
lt250K, lt350K, lt450K, lt550K, lt650K ,gt650K = myfns.make_category_sets(states_dictionary)

LT250K = 1
LT350K = 2
LT450K = 3
LT550K = 4
LT650K = 5
GT650K = 6

print('1: LT250K')
print('2: LT350K')
print('3: LT450K')
print('4: LT550K')
print('5: LT650K')
print('6: GT650K')



user_input = ' '
while user_input != "":
    user_input = input('\nChoose category 1-6, or just hit Enter when done: ')
    if user_input == "":
        break
    elif int(user_input) == LT250K:
        for item in lt250K:
            print(item)
    elif int(user_input) == LT350K:
        for item in lt350K:
            print(item)
    elif int(user_input) == LT450K:
        for item in lt450K:
            print(item)
    elif int(user_input) == LT550K:
        for item in lt550K:
            print(item)
    elif int(user_input) == LT650K:
        for item in lt650K:
            print(item)
    elif int(user_input) == GT650K:
        for item in gt650K:
            print(item)
