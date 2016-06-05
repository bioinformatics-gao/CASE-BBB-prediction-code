#!/bin/python
import re,csv
import codecs

def main(): 
    
    #sourcefile = open('2003-2006-2005-2004-logB-drug_CID-without-2015Hao-CNS.csv') # source file
    sourcefile = open('2002-Doniger-for-validation-43CNS.csv') # source file
    lines1 = sourcefile.readlines() 
    rows1 = len(lines1)
    training_drug_name_file = open('../Indication-CNS-ALL_in_line_sorted.tsv')# encoding='utf-16') # source file
    lines2 = training_drug_name_file.readlines() 
    rows2 = len(lines2)
    #training_file = open('2003-2006-2005-2004-logB-drug_CID-without-2015Hao-CNS-Indications.csv','w')
    training_file = open('2002-Doniger-for-validation-43CNS-Indications.csv','w')

    matched_times = 0
    for j in range(rows1):
        info = lines1[j].strip()
        pieces  = info.split(',')
        infoCID = pieces[0].strip()
        vector_length = len(pieces)

        founded = False
        for i in range(rows2):
            if len(lines2[i]) > 1:
                line = lines2[i].strip()
                items  = line.split('\t')
                currentCID = items[0].strip()
            
                if currentCID == infoCID:
                    founded = True
                    matched_times += 1
                    training_file.write( ','.join(pieces[0:(vector_length-2)]) + ',' + ','.join(items[1:]) + ',' + ','.join(pieces[-2:])+'\n')
                    print(str(matched_times)+'===================================')
                    print(str(currentCID)+'===================================')
                    break
        print(matched_times)
        if founded == False:
            items=['0']*43
            training_file.write( ','.join(pieces[0:(vector_length-2)]) + ',' + ','.join(items) + ',' + ','.join(pieces[-2:])+'\n')
         
    sourcefile.close()
    training_drug_name_file.close()
    #remaining_file.close()
    training_file.close()
if __name__ == "__main__": main()

