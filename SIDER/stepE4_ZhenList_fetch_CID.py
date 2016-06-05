#!/bin/python
import re,csv,codecs

def main(): 
    
    Hao_2015_file = open('drugSideEffects-12-08.tsv', encoding='utf-16') # source file
    lines2 = Hao_2015_file.readlines() 
    rows2 = len(lines2)
    Hao_2015_map_file = open('drugSideEffects-12-08_CID_Name_map.tsv','w')
    matched_times = 0
    
    for j in range(rows2):
        info = lines2[j].strip()
        drugName = info.lower()
        drugName1= drugName.replace(' ', '')

        founded = False
        with open('../CID-Synonym-filtered') as sourcefile:
            for line in sourcefile:
                items  = line.split('\t')
                currentCID = items[0].strip()
                thisName=items[1].strip().lower()
                thisName1=thisName.replace(' ', '')

                if  thisName1  == drugName1:
                    founded = True
                    matched_times += 1
                    Hao_2015_map_file.write(currentCID + '\t' + info +'\n')
                    break
            
            if founded == False:
                Hao_2015_map_file.write('NONE' + '\t' + info +'\n') 
        print(matched_times)


    Hao_2015_file.close()
    Hao_2015_map_file.close()
if __name__ == "__main__": main()

