#Jonathan Leventhal
#cs21 assignment#9
#program to take a string, encrypt it, and return it


#main fn
#accepts message, sends to getshift fn, computes/prints new message
def main():
    
    #get secret message
    user_input = str(input('Message to encrypt: '))

    #get shift amount
    shift_amount = ""
    shift_amount = getshift(user_input)

    #compute encrypted message
    newmsg = ""
    i = 0
    while i < len(user_input):
        val = ord(user_input[i]) + shift_amount
        char = chr(val)
        newmsg += char
        i+=1

    #print encrypted message
    print(newmsg)

#computes shift amount
def getshift(raw_message):

    #def variables
    total = 0
    ch = 0

    #create total amount in string
    while ch < len(raw_message):
        n = ord(raw_message[ch])
        total = total + n
        ch+=1

    #computing shift amount
    shift = total%4+3

    #return shift amount
    return shift       
    
main()
