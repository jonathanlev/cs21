#Jonathan Leventhal
#cs21 assignment2 cputime
#calculating the time it takes a CPU to execute...
#a set of machine language instructions by using a formula

#intro
print('This program calculates the total CPU time to run a program.\n')

#get number of machine instructions
instructions = float(input('Enter number of machine language instructions: '))

#get cycles per instruction
cpi = float(input('Enter average number of cycles per instruction (CPI): '))

#get clock rate
clock_rate = float(input('Enter clock rate (cycles per second): '))
print('\n')

#calculate
cpu_time = (instructions * cpi) / clock_rate

#return
print('==============================================================================')
print('This CPU will take a whopping', format(cpu_time, '.3f'),'seconds to successfully run the program.')
print('==============================================================================')
