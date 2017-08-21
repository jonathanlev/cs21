#Jonathan Leventhal
#cs21 assignment2 paybill
#calculating price of meal with tax and tip

#intro
print('This program will determine the total price of your meal.')

#get food price
food_price = (float(input('Please enter the price of your meal: ')))
              
#calculate
TIP = .18
TAX = .07              
tip = food_price * TIP
tax = food_price * TAX

#return
print('\nYour bill includes ...\n')
print('\n===================')
print('Food: ', format(food_price, '11.2f'))
print('Tip: ', format(tip, '12.2f'))
print('Tax: ', format(tax, '12.2f'))
print('===================')
print('\n\nYour total is: $', format(food_price + tax + tip,'.2f',))
              
              
