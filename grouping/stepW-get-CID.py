#!/bin/python
import re,csv

def main(): 
    
    Hao_2015_file = open('2003-2006-2005-2015-2004-logB-drug_CID4-without-Hao.csv') # source file
    #Hao_2015_file = open('2003-NYstate-2002-Doniger-activity-permeability-drug_CID2.csv') # source file
    lines2 = Hao_2015_file.readlines() 
    rows2 = len(lines2)
    Hao_2015_map_file = open('2003-2006-2005-2004-logB-drug_CID-without-2015Hao.tsv','w')
    #Hao_2015_map_file = open('2003-NYstate-2002-Doniger-CID.tsv','w')

    matched_times = 0
    for j in range(rows2):
        info = lines2[j].strip()
        items  = info.split(',')
        
        if len(items[0].strip()) > 0:
            SID=items[0].strip()
            CID=SID.strip('CID').lstrip('1').lstrip('0')
            items[1]=CID
            Hao_2015_map_file.write( '\t'.join(items)+'\n')
        else:
            CID=items[1]
            digit_length=len(CID)
            number_of_zero=8-digit_length
            SID='CID1'+'0'*number_of_zero + CID
            items[0] = SID
            Hao_2015_map_file.write( '\t'.join(items)+'\n')
        
                
         
    Hao_2015_file.close()
    Hao_2015_map_file.close()
if __name__ == "__main__": main()

