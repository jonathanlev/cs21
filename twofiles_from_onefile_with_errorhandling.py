# Alison Pechenick
# CS21 F16
# Read randNums.txt, create two files:  pos.txt, neg.txt


try:
    inRand = open('CS21randNums.txt','r')
    outPos = open('pos.txt','w')
    outNeg = open('neg.txt','w')
except IOError:
    print('Sorry, unable to open your file(s).')
else:
    for line in inRand:
        try:
           num = int(line)
        except ValueError:
            print('Oops!  Found a non-numeric value:  ',line.rstrip('\n'))
        else:
            if num > 0:
                outPos.write(str(num) + '\n')
            elif num < 0:
                outNeg.write(str(num) + '\n')
    inRand.close()
    outPos.close()
    outNeg.close()
    
