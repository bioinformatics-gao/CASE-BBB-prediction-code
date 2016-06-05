#!/bin/python
import re,csv

def main(): 
    
    sourcefile = open('CNS_grouping.tsv')
    lines1 = sourcefile.readlines() 
    rows1 = len(lines1)
    total_side_effects_file = open('drugSideEffects1-PT-only1.tsv') 
    lines2 = total_side_effects_file.readlines() 
    rows2 = len(lines2)
    output_file = open('0323_CID-drugSideEffects_CNS_43Category_count.tsv','w')
    matched_times = 0

    drug_side_effects = [None] * rows2
    drug_side_names = [None] * rows2
    for i in range(rows2):
        info = lines2[i].strip()
        pieces  = info.split('\t')
        drug_side_names[i] = pieces[0].strip()
        drug_side_effects[i] = pieces[1:]
        for u in range(len(drug_side_effects[i])):
            drug_side_effects[i][u]  = drug_side_effects[i][u].strip()

    items = [None] * rows1
    PT_effects = [None] * rows1
    for j in range(rows1):
        line = lines1[j].strip()
        items[j]  = line.split('\t')
        PT_effects[j] = items[j][1:]
        for v in range(len(PT_effects[j])):
            PT_effects[j][v] = PT_effects[j][v].strip()

    for i in range(rows2):
        found_in_CNS=False    
        for m in range(len(drug_side_effects[i])):
            for j in range(rows1): 
                for n in range(len(PT_effects[j])):     
                    #if re.search(str(drug_side_effects[i][m]), str(items[j][n]), re.I):
                    if drug_side_effects[i][m].lower()==PT_effects[j][n].lower():
                        found_in_CNS=True  
                        matched_times += 1
                        output_file.write(drug_side_names[i] + '\t'+ str(j)+'\t'+PT_effects[j][n] +'\n')

        if found_in_CNS==False:
            print(str(drug_side_names[i]) + 'NOT found!')
            output_file.write(drug_side_names[i] + '\t'+'NONE' + '\t' + 'NONE'+ '\n')         
         
    sourcefile.close()
    total_side_effects_file.close()
    output_file.close()
if __name__ == "__main__": main()

