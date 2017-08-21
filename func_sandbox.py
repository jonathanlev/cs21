#Adam Sminkey and Jonathan Leventhal
#CS21
#Lab 5, part 2

import random

def main():
    
    print('Lets convert your USD to CAD...')
    usd_val = float(input('Enter your USD value: '))
    print('This USD amount is worth $',format(usd2can(usd_val),'0.2f'),'Canadian dollars.')

    print('')

    for i in range(10):
        print(roomdraw())

    print('')
    
    num = 3
    verdict = checkType(num,int)
    print(num,'is an int: ',verdict)
    if verdict == True:
        print('Got that right!')
            
    num = 3.2
    verdict = checkType(num,int)
    print(num,'is an int: ',verdict)
    if verdict:
        print('Did the rules of arithmetic suddenly change?')
    else:
        print('Computer knows an int from a float.')
    
    verdict = checkType(4.2,float)
    print(4.2, 'is a float: ',verdict)
        
    print(4.2,'is a string: ',checkType(4.2,str))

    verdict = checkType('Catamounts!',str)
    print("\'Catamounts!\'", 'is a string: ',verdict)
    
    verdict = checkType('Catamounts!',int)
    print("\'Catamounts!\'", 'is an int: ',verdict)
    
    

def usd2can(usd_amount):
    RATE = 1.33
    cad_amount = RATE*usd_amount
    return cad_amount
    
def roomdraw():
    number=random.randint(1,4)
    if number==1:
        return 'University Heights'
    elif number==2:
        return 'Main Campus'
    elif number==3:
        return 'Athletic Campus'
    else:
        return 'Trinity Campus'

def checkType(value,data_type):
    if (type(value) == data_type):
        return True
    else:
        return False

main()
