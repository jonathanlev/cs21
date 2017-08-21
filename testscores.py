




def main():
    for i in range(5):
        score=float(input('Enter score: '))
        calc_average(score)
        determine_grade(score)

    print('scores\tnumeric grade\tletter grade')
    print('--------------------------------')
    for i in range(5):
        print('score',i,':/t',score,'\t',determine_grade(score))
    print('--------------------------------')
    ttl_avg = calc_average(score)
    print('Average score:',ttl_avg,'\t',determine_grade(ttl_avg))
        
def calc_average(a,b,c,d,e):
    average = (a+b+c+d+e)/5
    return average
        

def determine_grade(number):
    if number<100 and number>=90:
        return('A')
    elif number<90 and number>=80:
        return('B')
    elif number<80 and number>=70:
        return('C')
    elif number<70 and number>=60:
        return('D')
    else:
        return('F')

main()
    

                
