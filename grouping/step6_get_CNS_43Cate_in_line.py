#!/bin/python
import re,csv

def main(): 
    
    #sourcefile = open('drugSideEffects_CNS_43Category_count.tsv') # source file
    #sourcefile = open('CNS_endo_Category_count.tsv') # source file
    #sourcefile = open('CNS_eye_Category_count.tsv') # source file
    #sourcefile = open('CNS_social_Category_count.tsv') # source file
    #sourcefile = open('CNS_endo_eye_Category_count.tsv') # source file
    #sourcefile = open('CNS_endo_social_Category_count.tsv') # source file
    #sourcefile = open('CNS_eye_social_Category_count.tsv') # source file
    sourcefile = open('CNS_endo_eye_social_Category_count.tsv') # source file
    lines = sourcefile.readlines() 
    lastLine = lines[-1]
    #outfile = open('drugSideEffects_CNS_43Category_count_in_line.tsv','w')
    #outfile = open('CNS_endo_Category_count_in_line.tsv','w')
    #outfile = open('CNS_eye_Category_count_in_line.tsv','w')
    #outfile = open('CNS_social_Category_count_in_line.tsv','w')
    #outfile = open('CNS_endo_eye_Category_count_in_line.tsv','w')
    #outfile = open('CNS_endo_social_Category_count_in_line.tsv','w')
    #outfile = open('CNS_eye_social_Category_count_in_line.tsv','w')
    outfile = open('CNS_endo_eye_social_Category_count_in_line.tsv','w')
    earlierCID = None 
    Nervous_sideEffects = [] 
    for line in lines:
        infoList = line.strip().split('\t')
        currentCID = infoList[0] 
        currentSideEffectCatrgory = infoList[1]
        print(currentSideEffectCatrgory)
        currentSideEffectName = infoList[2]
        print(currentSideEffectName)
        
        if earlierCID == None or earlierCID == currentCID: 
            Nervous_sideEffects.append(currentSideEffectCatrgory)
            Nervous_sideEffects.append(currentSideEffectName)
            if line == lastLine:
                print(lastLine)
                outfile.write(currentCID + '\t')
                for item in Nervous_sideEffects:
                    outfile.write(str(item) + '\t')
                outfile.write('\n')
                del Nervous_sideEffects[:] 
                del Nervous_sideEffects 
        else:
            outfile.write(earlierCID + '\t')
            for item in Nervous_sideEffects:
                outfile.write(str(item) + '\t')
            outfile.write('\n')
            del Nervous_sideEffects[:]
            Nervous_sideEffects = []
            Nervous_sideEffects.append(currentSideEffectCatrgory)
            Nervous_sideEffects.append(currentSideEffectName)
        earlierCID = infoList[0] 
        
    sourcefile.close()
    outfile.close()
if __name__ == "__main__": main()
