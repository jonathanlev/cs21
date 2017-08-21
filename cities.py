#Jonathan Leventhal
#cs21 assignment#8
#checks cities to see which states they are in, or not in


#calls all fns of prog and displays
def main():
    
    city = ''
    #get city name
    while (city != 'q'): #continue until user decides
        city = input("Enter city "+"(type 'q' to quit)"+": ")

        #city in vt?
        i = 0
        vt_city = False
        
        vtCityList = file2list('vt_municipalities.txt')
        for i in range(len(vtCityList)):
            if (city == vtCityList[i].rstrip('\n')):
                vt_city = True

        #city in nh?
        i = 0
        nh_city = False
        
        nhCityList = file2list('nh_municipalities.txt')
        for i in range(len(nhCityList)):
            if (city == nhCityList[i].rstrip('\n')):
                nh_city = True

        #print results back to user
        if (vt_city == True and nh_city == True):
            print(city,'is a city in both VT and NH.\n')
        elif (vt_city == True and nh_city == False):
            print(city,'is a city in VT.\n')
        elif (vt_city == False and nh_city == True):
            print(city,'is a city in NH.\n')
        elif (vt_city == False and nh_city == False):
            if(city == 'q'):
                break
            else:
                print('Neither VT or NH has a city by that name.\n')
    

#input filename, open file, read file, create list, return list
def file2list(user_file):
    try:
        ((user_file) == 'vt_municipalities.txt')
        
    #handle ioerror and return empty list
    except IOError:
        print('.\n.\nIOError exception')
        vtlist = []
        return(vtlist)
    
    if ((user_file) == 'vt_municipalities.txt'):
        #open file
        vtfile = open('vt_municipalities.txt','r')
        
        #read contents into list
        vtlist = vtfile.readlines()
        i = 0
    
        #strip each line of \n
        #vt
        while (i < len(vtlist)):
            vtlist[i] = vtlist[i].rstrip('\n')
            i+=1

        #close file
        vtfile.close()

        #output city lists for both states
        return(vtlist)

    try:
        ((user_file) == 'nh_municipalities.txt')
            
    #handle ioerror and return empty list
    except IOError:
            print('.\n.\nIOError exception')
            nhlist = []
            return(nhlist)
        
    if ((user_file) == 'nh_municipalities.txt'):
        #open file
        nhfile = open('nh_municipalities.txt','r')

        #read contents into list
        nhlist = nhfile.readlines()
        i = 0

        #strip each line of \n
        #nh
        while (i < len(nhlist)):
            nhlist[i] = nhlist[i].rstrip('\n')
            i+=1

        #close file
        nhfile.close()

        #output city lists for both states
        return(nhlist)
        
        
main() #main fn call
