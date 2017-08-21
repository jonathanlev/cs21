#Jonathan Leventhal
#cs21 assignment3
#program to count up money

print('Guess how many coins will add up to one dollar.')

#constants
PENNY = .01
NICKLE = .05
DIME = .1
QUARTER = .25

#get number of pennies, nickels, dimes, and quarters
p_pennies = int(input('How many pennies do you have? '))
p_nickles = int(input('How many nickles do you have? '))
p_dimes = int(input('How many dimes do you have? '))
p_quarters = int(input('How many quarters do you have? '))

#return final result
coin_total = float((p_pennies*PENNY) + (p_nickles*NICKLE) + (p_dimes*DIME) + (p_quarters*QUARTER))

print('*\n*\n*\n*\n*\n*\n*')
print('=======================================')

if coin_total == 1:
    print('Congratulations! You won the game!')
elif coin_total < 1:
    print('Sorry, your total of $',coin_total,'is less than $1.00')
elif coin_total > 1:
    print('Sorry, your total of $',coin_total,'is more than $1.00')
    
