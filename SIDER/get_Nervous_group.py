#!/bin/python
import re,csv

def main(): 
    
    sourcefile = open('Nervous_2_columes.txt') # source file
    lines = sourcefile.readlines() 
    lastLine = lines[-1]
    outfile = open('Nervous_grouping.tsv','w')
    earlier_HLGT_name = None 
    Nervous_sideEffects = [] 
    for line in lines:
        infoList = line.strip().split('$')
        PT_name = infoList[0] 
        HLGT_name = infoList[1]
        print(HLGT_name)
        
        if earlier_HLGT_name == None or earlier_HLGT_name == HLGT_name: 
            Nervous_sideEffects.append(PT_name)
            if line == lastLine:
                print(lastLine)
                #effectsSet = set(Nervous_sideEffects)
                #effectsList = list(effectsSet)
                outfile.write(HLGT_name + '\t')
                for item in Nervous_sideEffects:
                    outfile.write(str(item) + '\t')
                outfile.write('\n')
                del Nervous_sideEffects[:] 
                del Nervous_sideEffects 
        else:
            outfile.write(earlier_HLGT_name + '\t')
            for item in Nervous_sideEffects:
                outfile.write(str(item) + '\t')
            outfile.write('\n')
            del Nervous_sideEffects[:]
            Nervous_sideEffects = []
            Nervous_sideEffects.append(PT_name)

        earlier_HLGT_name = infoList[1] 
        
    sourcefile.close()
    outfile.close()
if __name__ == "__main__": main()
