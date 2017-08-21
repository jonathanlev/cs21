#Jonathan Leventhal
#cs21 assignment#6
#program to compute mpg


#prompt for two floats
#ttl miles driven
#% of ttl miles driven on highway
#validate input f1 should be + and f2 should be 0-100
#while loop, cont with new trips until user is done
def main():
    again = 'y'
    while (again == 'y'):
        print('Computing your gas expenses...')
        total_miles = float(input('Enter total miles driven: '))
        while (total_miles < 0):
            total_miles = float(input('\nError, must be positive.\n\tEnter total miles driven: '))
        percent_highway_miles = float(input('Enter % of total miles driven on highway: '))
        while(percent_highway_miles <= 0 or percent_highway_miles >= 100):
            percent_highway_miles = float(input('\nError, must between 0 and 100.\n\tEnter % of total miles driven on highway: '))

        total_gas = totalGallons(total_miles,percent_highway_miles)
        total_price = gasExpense(total_gas)
    
        print('\nHere is the information for your trip')
        print('Total miles:',total_miles)
        print('Gas consumption:',(format(total_gas,'0.1f')),'gal')
        print('Total cost: $',(format(total_price,'0.2f')))

        print('\nWould you like to compute gas expense for another trip?')
        again = input('(y/n): ')
        if (again == 'n'):
            break    
        else:
            again == 'y'
            print()
               
#2 input params
#2 constants, city and highway mpg
#compute and return ttl gas cnsmptn
def totalGallons(ttl_miles,prcnt_highway_miles):
    CITY_MPG = 29
    HIGHWAY_MPG = 39
    total_highway_miles = (prcnt_highway_miles / 100)*ttl_miles
    total_city_miles = (ttl_miles - total_highway_miles)
    
    ttl_gas_consumption = (total_highway_miles/HIGHWAY_MPG)+(total_city_miles/CITY_MPG)
    return ttl_gas_consumption

#1 input param
#compute and rtrn total spent on gasoline for trip
#constant price of 2.19 per gallon
def gasExpense(c):
    GAS_PRICE = 2.19
    ttl_spent = GAS_PRICE*c
    return ttl_spent

main()
