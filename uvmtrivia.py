#Jonathan Leventhal
#cs21 assignment5
#program to display five pieces of UVM trivia


MAX = 5
MIN = 0

#sends values 1-5 thru to trivia fn
def main():
    for i in range(1,6):
        trivia(i)
    
#displays all 5 trivia facts from values in main fn
def trivia(fact_num):
    #user_input = int(input('Enter a number between 1 and 5: '))
    #while (user_input <= MIN or user_input > MAX):
        #print('Error: Invalid number\n.\n.\n.')
        #user_input = int(input('Enter a number between 1 and 5: '))
        
    if(fact_num == 1):
        print('Fact # 1 : UVMs mascot is Rally the Catamount')
        print('\n')
    elif(fact_num == 2):
        print('Fact # 2 : UVM Rescue is an award-winning, student run state certified Advanced Life Support (ALS) ambulance. It is staffed and operated by UVM students 24 hours a day, 365 days a year.')
        print('\n')
    elif(fact_num == 3):
        print('Fact # 3 : UVM research vessel Melosira is docked near ECHO Aquarium on Lake Champlain.')
        print('\n')
    elif(fact_num == 4):
        print('Fact # 4 : Students can study in seven different colleges on campus')
        print('\n')
    elif(fact_num == 5):
        print('Fact # 5 : On a per capita basis, Vermont is the top Peace Corps volunteer-producing state in the nation.')
        print('\n')

main()

 
