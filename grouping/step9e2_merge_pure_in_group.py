#!/bin/python
import re,csv,numpy

def main(): 
    
    sourcefile = open('43-traing.csv') 
    #sourcefile = open('43-test.csv') 
    #sourcefile = open('43-traing-validation.csv') 
    #sourcefile = open('43-validation.csv') 
    lines = sourcefile.readlines() 
    rows1 = len(lines)
    output_file = open('43-traing_10_pure_feature_grouped.csv','w')
    #output_file = open('43-test_10_pure_feature_grouped.csv','w')
    #output_file = open('43-traing-validation_10_pure_feature_grouped.csv','w')
    #output_file = open('43-validation_10_pure_feature_grouped.csv','w')

    line = lines[1].strip()
    items  = line.split(',')
    item_count  = len(items)
    feature_vector  = [None]*(item_count-3)
    
    class_vector = []
    for j in range(2,item_count-1):
        feature_vector[j-2]  = []

    for i in range(rows1):
        line = lines[i].strip()
        items  = line.split(',')
        class_vector.append(items[-1])
        for j in range(2,item_count-1):
            feature_vector[j-2].append(items[j])

    def groupMerge(*args):
        column=len(args)
        data_point_number = len(args[0])
        Merged_group = ['0']*data_point_number
        for i in range(column):
            for j in range(data_point_number):
                if str(args[i][j])==str(1):
                    Merged_group[j]=str(1)
        return Merged_group

    group3_9_12_13_14_26_28_33_34_42=groupMerge(feature_vector[2], feature_vector[8], feature_vector[11],feature_vector[12], \
    feature_vector[13],feature_vector[25], feature_vector[27], feature_vector[32],feature_vector[33], feature_vector[41])

    output_file.write('feature 3_9_13_14_26_33_34_42_pure' + ',' + ','.join(group3_9_12_13_14_26_28_33_34_42[:]) +'\n')

    sourcefile.close()
    output_file.close()

if __name__ == "__main__": main()

