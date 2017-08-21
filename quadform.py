#Adam Sminkey and Jonathan Leventhal
#CS21
#Program to compute quadratic formula

import math

print('Welcome to the quadratic formula calculator.')

#getting variables
a = float(input('Enter a value for "a": '))
b = float(input('Enter a value for "b": '))
c = float(input('Enter a value for "c": '))

#calculations
if (b**2-(4*a*c)) == 0:
    print(-b/(2*a))
elif (b**2-(4*a*c)) < 0:
    print('No real roots')
elif (b**2-(4*a*c)) > 0:
    qf = (math.sqrt(b**2-(4*a*c)))
    print('Roots are: ',format(((-b-qf)/(2*a)),'.1f'), 'and',format(((-b+qf)/(2*a)),'.1f'))
              


    
