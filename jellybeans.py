#Jonathan Leventhal
#cs21 assignment#6
#jelly bean guessing game

import math
import random

#gen random int between 1 and 10 for h and r
#knowing dimensions, user guesses # of beans
#1 and 10 and constants, use in randint
#use math.pi with vol


def main():
    MIN = 1
    MAX = 10
    
    print('Welcome to the jellybean guessing game')
    print('Program is generating jar size')
    print('.')
    print('.')
    print('.')
    
    a = random.randint(MIN,MAX)
    b = random.randint(MIN,MAX)
    
    jar_volume = computeVolume(a,b)
    print('Your jar:')
    print('Height =',a,'in.')
    print('Radius =',b,'in.')
    print()
    guess = int(input('Guess the amount of jelly beans: '))
    print()
    act_beans = computeBeans(jar_volume)
    print('Actual number of beans:',format(act_beans,'0.0f'))
    print('Your guess:',guess)
    print()
    print('====================')
    classifyGuess(act_beans,guess)
    print('====================')
    
def computeVolume(height,radius): #accept h and r, return volume of jar
    volume = (math.pi)*(radius**2)*(height)
    return volume

def computeBeans(volume): #accept vol, compute total num of beans, return beans
    BEAN_VOL = .47
    MAX_VOL_BEANS = .8
    num_beans = (MAX_VOL_BEANS*volume)/BEAN_VOL
    return num_beans

def classifyGuess(act_num_beans,guess_num_beans): #return accuracy of guess
    NINETY_PERCENT = .9
    ONETEN_PERCENT = 1.1
    if (guess_num_beans < (act_num_beans*NINETY_PERCENT)):
        result = print('Sorry - too low')
    elif (guess_num_beans > (act_num_beans*ONETEN_PERCENT)):
        result = print('Sorry - too high')
    elif ((act_num_beans*NINETY_PERCENT) < guess_num_beans < (act_num_beans*ONETEN_PERCENT)):
        result = print('Yes, your guess is close enough')
    return result

main()
