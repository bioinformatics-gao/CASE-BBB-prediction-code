#!/bin/python
import re,csv

def main(): 
    
    sourcefile = open('CNS_endo_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_eye_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_social_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_endo_eye_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_endo_social_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_eye_social_Category_count_in_line.tsv') # source file
    #sourcefile = open('CNS_endo_eye_social_Category_count_in_line.tsv') # source file

    lines = sourcefile.readlines() 
    lastLine = lines[-1]

    groupingfile = open('CNS_endo_grouping.tsv')
    #groupingfile = open('CNS_eye_grouping.tsv')
    #groupingfile = open('CNS_social_grouping.tsv')
    #groupingfile = open('CNS_endo_eye_grouping.tsv')
    #groupingfile = open('CNS_endo_social_grouping.tsv')
    #groupingfile = open('CNS_eye_social_grouping.tsv')
    #groupingfile = open('CNS_endo_eye_social_grouping.tsv')

    lines1 = groupingfile.readlines() 
    group_length=len(lines1) 

    outfile = open('Sideffects_CNS_endo_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_eye_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_social_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_endo_eye_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_endo_social_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_eye_social_Category_in_line_sorted.tsv','w')
    #outfile = open('Sideffects_CNS_endo_eye_social_Category_in_line_sorted.tsv','w')

    for line in lines:
        Category_effects = [0]*group_length
        infoList = line.strip().split('\t')
        currentCID = infoList[0] 
        currentSideEffectMatch = infoList[1:]
        length = len(currentSideEffectMatch)
         
        for i in range(0,length,2):
            index=int(currentSideEffectMatch[i])  
            Category_effects[index] =+1

        outfile.write(currentCID + '\t')
        outfile.write('\t'.join(str(x) for x in Category_effects)+'\n')

    sourcefile.close()
    outfile.close()
        
if __name__ == "__main__": main()
