#!/bin/python
import re,csv,numpy

def main(): 
    
    sourcefile = open('SideEffects_31_Categegory_completed.csv') 
    lines = sourcefile.readlines() 
    rows1 = len(lines)
    output_file = open('SideEffects_31_Categegory_completed_corelation.csv','w')
    correlation_output_file = open('SideEffects_31_Categegory_completed_corelation_score.tsv','w')

    line = lines[1].strip()
    items  = line.split(',')
    item_count  = len(items)
    feature_vector  = [None]*(item_count-3)
    
    class_vector = []
    for j in range(3,item_count):
        feature_vector[j-3]  = []

    for i in range(rows1):
        line = lines[i].strip()
        items  = line.split(',')
        class_vector.append(items[2])
        for j in range(3,item_count):
            feature_vector[j-3].append(items[j])

    for k in range(len(feature_vector)):
        correlation=numpy.corrcoef(class_vector,feature_vector[k])[0, 1]
        correlation_output_file.write(str(k)+ '\t' + 'feature correlation with class is' + '\t'+ str(correlation) +'\n')

    output_file.write(','.join(class_vector[:]) +'\n')
    for j in range(3,item_count):
        #print(feature_vector[j-3])
        output_file.write(','.join(feature_vector[j-3][:]) +'\n')

    sourcefile.close()
    output_file.close()
    correlation_output_file.close()

if __name__ == "__main__": main()

