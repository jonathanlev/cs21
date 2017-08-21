#Jonathan Leventhal
#cs21 assignment#9
#program to determine freq of characters in a string


#main fn
def main():
    user_message = input('Enter a message: ')
    user_message = user_message.lower()
    print('\nYour message is:',user_message)
    
    #var dec
    alphalist = []
    countlist = []

    #message is string
    i = 0 #go thru list
    while i < len(user_message):
        alpha = user_message[i]
        #if alpha is not in alphalist then append to list
        if alpha not in alphalist:
            alphalist.append(alpha)
            j = 0 #go thru whole list
            count = 0
            while j < len(user_message):
                #count how many times alpha is in list
                if(user_message[j] == alpha):
                    count+=1   
                j+=1
            #append count to countlist
            countlist.append(count)
        #next letter
        i+=1

    #displaying results
    print('\nLetter \t Freq')
    i = 0
    while i < len(alphalist):
        print(alphalist[i],'\t',countlist[i],'\n')
        i+=1    
main()
