#script3
def stringtodic(samplestr):
    lowerstr = samplestr.lower()
    lowerstr ="".join(lowerstr.split())
    counterdict = {}
    for x in lowerstr:
        if x in counterdict:
            counterdict[x]+=1
        else:
            counterdict[x]=1
    return counterdict

samplestring = input("Enter a string: ")
print(stringtodic(samplestring))    
