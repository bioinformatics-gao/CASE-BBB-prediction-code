#!/bin/python
import re,csv
import codecs

def main(): 
    
    sourcefile = open('../0323-Sideffects_CNS_in_line_sorted.tsv') # source file
    lines1 = sourcefile.readlines() 
    rows1 = len(lines1)
    #training_drug_name_file = open('2003-2006-2005-2004-logB-drug_CID-without-2015Hao.tsv')# encoding='utf-16') # source file
    training_drug_name_file = open('2002-Doniger_Name_CID_TO-SIDER-remove-conflicts2-remove-in-training2.csv')# encoding='utf-16') # source file
    lines2 = training_drug_name_file.readlines() 
    rows2 = len(lines2)
    #training_file = open('2003-2006-2005-2004-logB-drug_CID-without-2015Hao-CNS.csv','w')
    training_file = open('2002-Doniger-for-validation-43CNS.csv','w')

    matched_times = 0
    for j in range(rows2):
        info = lines2[j].strip()
        #pieces  = info.split('\t')
        pieces  = info.split(',')
        infoCID = pieces[0].strip()

        founded = False
        for i in range(rows1):
            line = lines1[i].strip()
            items  = line.split('\t')
            currentCID = items[0].strip()
            
            if currentCID == infoCID:
                founded = True
                matched_times += 1
                training_file.write(','.join(pieces[0:2]) +','+ ','.join(items[1:]) +',' + ','.join(pieces[2:]) + '\n')
                #print(pieces[0:2])
                #training_file.write(','.join(pieces[0:3]) +','+','.join(items[1:]) +'\n')
                print(str(matched_times)+'===================================')
                print(str(currentCID)+'===================================')
                break
        print(matched_times)
        if founded == False:
            training_file.write( ','.join(pieces[0:3]) + '\n')
         
    sourcefile.close()
    training_drug_name_file.close()
    #remaining_file.close()
    training_file.close()
if __name__ == "__main__": main()

