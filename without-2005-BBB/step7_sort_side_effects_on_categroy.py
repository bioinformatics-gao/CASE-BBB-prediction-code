#!/bin/python
import re,csv

def main(): 
    
    sourcefile = open('0323-drugSideEffects_CNS_43Category_count_in_line.tsv') # source file
    lines = sourcefile.readlines() 
    lastLine = lines[-1]
    outfile = open('0323-Sideffects_CNS_in_line_sorted.tsv','w')

    for line in lines:
        Category_effects = [0]*43
        infoList = line.strip().split('\t')
        currentCID = infoList[0] 
        
        if infoList[1] != 'NONE': 
            currentSideEffectMatch = infoList[1:]
            length = len(currentSideEffectMatch)
         
            for i in range(0,length,2):
                index=int(currentSideEffectMatch[i])  
                Category_effects[index] += 1

            outfile.write(currentCID + '\t')
            outfile.write('\t'.join(str(x) for x in Category_effects)+'\n')

        else:
            outfile.write(currentCID + '\t' + '\t'.join(str(x) for x in Category_effects)+'\n')

    sourcefile.close()
    outfile.close()
        
if __name__ == "__main__": main()
