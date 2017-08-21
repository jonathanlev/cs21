#Jonathan Leventhal
#cs21 assignment#9
#program to search a txt file using string testing methods


#main fn
#search file
#compute data
#return data
def main():

    #get file name
    user_file_name = input("Enter file name: ")
    while (user_file_name != 'dracula.txt'):
        print(user_file_name,'is not a valid file name.')
        user_file_name = input("Enter file name: ")
    
    #open file
    user_file = open('dracula.txt','r')

    #var dec
    num_uppercase = 0
    num_lowercase = 0
    num_digit = 0
    num_whitespace = 0
    i = 0
    
    #read file contents
    file_contents = user_file.read()

    while (file_contents != ""):
        file_contents = file_contents.rstrip()
        while (i < len(file_contents)):
            #uppercase letters
            if (file_contents[i].isupper()):
                num_uppercase = num_uppercase + 1
                
            #lowercase letters
            elif (file_contents[i].islower()):
                num_lowercase = num_lowercase + 1
                
            #digits
            elif (file_contents[i].isdigit()):
                num_digit = num_digit + 1
                
            #whitespace
            elif (file_contents[i].isspace()):
                num_whitespace = num_whitespace + 1
                
            #counter
            i+=1
        file_contents = user_file.readline()
        file_contents = file_contents.rstrip()
        
    #return vals
    print('Uppercase letters:',num_uppercase)
    print('Lowercase letters: ',num_lowercase)
    print('Digits:',num_digit)
    print('Spaces:',num_whitespace)
    
    #close file        
    user_file.close()
    
main()
