#!/bin/python
import re,csv

def main(): 
    
    Hao_2015_file = open('2002-Doniger-CID_Name_map.tsv') # source file
    lines2 = Hao_2015_file.readlines() 
    rows2 = len(lines2)
    Hao_2015_map_file = open('2002-Doniger_Name_CID_TO-SIDER.tsv','w')

    matched_times = 0
    for j in range(rows2):
        info = lines2[j].strip()
        items  = info.split('\t')
        CID=items[0].strip()
        
        founded = False
        with open('../SIDER_Drug_CID_Name.tsv') as sourcefile:
            for line in sourcefile:
                items=line.strip().split('\t')
                if len(items) > 1: 
                    currentCID = items[1].strip()
                    prefered_drugName=items[0].strip()

                if currentCID == CID:
                    founded = True
                    matched_times += 1
                    Hao_2015_map_file.write( prefered_drugName + '\t' + info +'\n')
                    break
                
        print(matched_times)
         
    Hao_2015_file.close()
    Hao_2015_map_file.close()
if __name__ == "__main__": main()

