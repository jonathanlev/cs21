#Jonathan Leventhal
#cs21 assignment#10
#program myfns
    
#function to create dictionary
def make_elector_dictionary(fname):
    
    elec_dict = {} #create empty dict
    
    try:
        input_file = open(fname,'r') #open input file
        line = input_file.readline()
        while line != "":
            key = line.rstrip('\n') #state name
            line = input_file.readline()
            popn = line.rstrip('\n') #population
            line = input_file.readline()
            votes = line.rstrip('\n') #votes
            line = input_file.readline()
            elec_dict[key] = [popn,votes] #dictionary entry
            
    except IOError:
        print('Error: file not found.') #error message
    
    input_file.close() #close input file
    
    return elec_dict #return dictionary

#function to split into sets
def make_category_sets(dictionary):
    set1 = set()
    set2 = set()
    set3 = set()
    set4 = set()
    set5 = set()
    set6 = set()
    
    for key in dictionary:
        ratio = int(dictionary[key][0]) / int(dictionary[key][1])
        
        if ratio < 250000:
            set1.add(key)
        elif 250000 <= ratio < 350000:
            set2.add(key)
        elif 350000 <= ratio < 450000:
            set3.add(key)
        elif 450000 <= ratio < 550000:
            set4.add(key)
        elif 550000 <= ratio < 650000:
            set5.add(key)
        elif ratio >= 650000:
            set6.add(key)
            
    return set1,set2,set3,set4,set5,set6,

#function to print selected set
def print_set(sset):
    for item in sset:
        print(item)
