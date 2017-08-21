#Jonathan Leventhal
#cs21 assignment#8
#calculates total pay for an employee based on specific hours and payrate
#calculates total payroll and avg paycheck if multiple employees are entered



#get user input
#compute total pay
#write user and summary info to txt file
def main():

    #files
    outfile = open('payroll.txt','w')

    #var dec
    count = 0
    totalpay = 0.0
    name_list = []
    hours_list = []
    rate_list = []
    pay_list = []
    keep_going = 'y' #looping var
    newline = '\n'
    tab = '\t'
    
    while (keep_going=='y'): #continue until user inputs n
        #iteration counter
        count+=1
        
        #get name
        name = input('Enter name: ')            
        name_list.append(name)

        
        #get valid hours worked    
        try:
            hours_worked = float(input('Enter hours worked: '))
        except ValueError:
            print('ERROR: hours worked must be a float')
            hours_worked = float(input('\nEnter hours worked: '))
        hours_worked = format(hours_worked,'0.2f')    
        hours_list.append(hours_worked)

        
        #get valid hourly rate    
        try:
            hourly_rate = float(input('Enter hourly rate: '))
        except ValueError:
            print('\tERROR: hourly rate must be a float')
            hourly_rate = float(input('\nEnter hourly rate: '))
        hourly_rate = format(hourly_rate,'0.2f')
        rate_list.append(hourly_rate)

        #calc total pay
        pay = float(hours_worked) * float(hourly_rate)
        pay = format(pay,'0.2f')
        pay_list.append(pay)
        
        #total payroll counter
        totalpay = float(totalpay) + float(pay)
        totalpay = format(totalpay,'0.2f')
        
        keep_going = input('Another employee? (y/n)')

        
    #average paycheck calc
    avg_paycheck_calc = float(totalpay)/(float(count))
    avg_paycheck_calc = format(avg_paycheck_calc,'0.2f')
    
    i = 0
    name_list_len = len(name_list)
    
    for i in range(name_list_len):
        #write name to file 
        outfile.write(name_list[i])
        outfile.write(tab)            

        #write hours to file
        outfile.write(hours_list[i]+' ')

        #write rate to file
        outfile.write(rate_list[i]+' ')

        #write pay to file
        outfile.write(pay_list[i])
        outfile.write(newline)
    
    out_totalpay = 'Total Payroll = $' + str(totalpay)
    out_avg_paycheck = 'Average Paycheck = $' + str(avg_paycheck_calc)

    outfile.write(newline)
    outfile.write(out_totalpay)
    outfile.write(newline)
    outfile.write(out_avg_paycheck)
    print('.')
    print('.')
    print('.')
    print('File successfully updated.')
    outfile.close()
main()
