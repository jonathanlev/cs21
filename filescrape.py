#Jonathan Leventhal
#CS21 assignment#7
#program to search, grab, and return data segment from a file

#reads file for desired data, and returns
def main():
       #checks for correct filename
       userfile = input('Filename: ')
       while (userfile != 'partisan.txt'):
              print(userfile,'is not a valid filename.')
              userfile = input('Filename: ')

       #opens file    
       userfile = open('partisan.txt','r')

       #starting line
       first_line = "Variables/Columns"
       
       #var line holds the info of one line
       line = userfile.readline()
       
       while (line != ""): #runs as long as string is not empty
              line = userfile.readline()
              line = line.rstrip()
              if (line.rstrip() == first_line): #checks line for our desired line     
                     print (first_line)
                     for i in range(5): #prints next 5 lines
                            line = userfile.readline()
                            line = line.rstrip()
                            print (line)
              else:
                     line = userfile.readline()       
       userfile.close()
       print ('\nAll done!')
       
main() #calls the main function
