#!/bin/python
import re,csv

def main(): 
    
    #sourcefile = open('Sideffects_CNS_endo_Category_in_line_sorted.tsv') # source file
    #sourcefile = open('Sideffects_CNS_eye_Category_in_line_sorted.tsv') # source file
    #sourcefile = open('Sideffects_CNS_social_Category_in_line_sorted.tsv') # source file
    #sourcefile = open('Sideffects_CNS_endo_eye_Category_in_line_sorted.tsv') # source file
    #sourcefile = open('Sideffects_CNS_endo_social_Category_in_line_sorted.tsv') # source file
    #sourcefile = open('Sideffects_CNS_eye_social_Category_in_line_sorted.tsv') # source file
    sourcefile = open('Sideffects_CNS_endo_eye_social_Category_in_line_sorted.tsv') # source file
    lines1 = sourcefile.readlines() 
    rows1 = len(lines1)
    training_drug_name_file = open('drugSideEffects_trainig-no-nutrion-topical.csv') # source file
    lines2 = training_drug_name_file.readlines() 
    rows2 = len(lines2)
    #remaining_file = open('remainig_CNS_endo.csv','w')
    #training_file = open('trainig_CNS_endo.csv','w')
    #remaining_file = open('remainig_CNS_eye.csv','w')
    #training_file = open('trainig_CNS_eye.csv','w')
    #remaining_file = open('remainig_CNS_social.csv','w')
    #training_file = open('trainig_CNS_social.csv','w')
    #remaining_file = open('remainig_CNS_endo_eye.csv','w')
    #training_file = open('trainig_CNS_endo_eye.csv','w')
    #remaining_file = open('remainig_CNS_endo_social.csv','w')
    #training_file = open('trainig_CNS_endo_social.csv','w')
    #remaining_file = open('remainig_CNS_eye_social.csv','w')
    #training_file = open('trainig_CNS_eye_social.csv','w')
    remaining_file = open('remainig_CNS_endo_eye_social.csv','w')
    training_file = open('trainig_CNS_endo_eye_social.csv','w')

    matched_times = 0
    for i in range(rows1):
        line = lines1[i].strip()
        items  = line.split('\t')
        currentCID_8_diget = items[0][4:]
        print(str(currentCID_8_diget)+'**************')

        in_the_traing_data = False
        for j in range(rows2):
            info = lines2[j].strip()
            pieces  = info.split(',')
            infoCID_8_diget = pieces[0][4:]
            if currentCID_8_diget == infoCID_8_diget:
                in_the_traing_data = True
                matched_times += 1
                training_file.write( ','.join(pieces[0:3]) + ','+','.join(items[1:]) +'\n')
                print(str(matched_times)+'===================================')
                print(str(currentCID_8_diget)+'===================================')
                break
        print(matched_times)
        if in_the_traing_data == False:
            remaining_file.write(','.join(items[:]) +'\n')
         
    sourcefile.close()
    training_drug_name_file.close()
    remaining_file.close()
    training_file.close()
if __name__ == "__main__": main()

