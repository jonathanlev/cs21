#Jonathan Leventhal
#CS21 assignment#7
#creates organized file of bowling players, scores, and how they did


#creates file of organized scores and results
def main():
    #opens file    
    infile = open('bowlingscores.txt','r')
    outfile = open('bowlingstats.txt','w')

    #variable decleration
    name = ''
    score = 0
    result = ''
    sep = ' : '
    newline = '\n'

    try:
        line = infile.readline()
        name = str(line)
        while (line != ""): #continue until EOF
        
            if(type(line) == str):
                name = line.rstrip() 
                outfile.write(name)
                outfile.write(sep)
            
                line = infile.readline()
                score = line.rstrip()
                score = int(score)
                if(type(score) == int):
                    score = str(score)
                    outfile.write(score) 
                    outfile.write(sep)
                
                    score = int(score)
                    if (score == 300):
                        result = 'perfect'
                    elif (200 <= score < 300):
                        result = 'not too shabby'
                    elif (score < 200):
                        result = 'needs practice'
                    else:
                        result = 'invalid data'
                    outfile.write(result)
                    outfile.write(newline)
                
            line = infile.readline()
            name = line.rstrip()   
        print("Data was successfully written to file.")
            
        infile.close()
        outfile.close()
    except IOError:
        print("File IOError, program has stopped")
        
main()
