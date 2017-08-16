import csv
import os
import shutil
import time
import numpy as np


# newly crawled betting lines are saved in the inputDir folder
# inputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/leaf_nodes"
inputDir = "/Users/chao/GoogleDrive/2017-08-10_lmt"
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = "/Users/chao/GoogleDrive/2017-08-10_lmt"
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = "/Users/chao/GoogleDrive/2017-08-10_lmt"

fileNameList = [] # all file names in the input folder are saved in this list
for file in os.listdir(inputDir):
    if file.endswith('5_year_original.csv'):
                #splitext(file)[0] remove the .txt extension from file name
        fileName = os.path.splitext(file)[0]
        fileNameList.append(fileName)
print fileNameList

col_dict = {'DraftAge': 2, 'Height': 5, 'Weight': 6, 'CSS_rank': 10, 'rs_GP': 11, 'rs_G': 12, 'rs_A': 13, 'rs_P': 14,
            'rs_PIM': 15, 'rs_PlusMinus': 16, 'po_GP': 17, 'po_G': 18, 'po_A': 19, 'po_P': 20, 'po_PIM': 21,
            'po_PlusMinus': 22}

for fileName in fileNameList:
    max_min_dict = {}
    for col in col_dict:
        col_index = col_dict[col]
        with open(inputDir + "/" + fileName + '.csv', 'r') as inputFile:
            csv_data = csv.reader(inputFile)
            firstLine = True
            max_val = -99999
            min_val = 99999
            for row in csv_data:
                if firstLine:
                    firstLine = False
                    continue
                try:
                    if max_val < float(row[col_index]):
                        max_val = float(row[col_index])
                    if min_val > float(row[col_index]):
                        min_val = float(row[col_index])
                except ValueError:
                    continue
            max_min_dict[col + '_max'] = max_val
            max_min_dict[col + '_min'] = min_val
    print str(max_min_dict)

    rows_list = []
    with open(inputDir + "/" + fileName + '.csv','r') as inputFile2:
        csv_data = csv.reader(inputFile2)
        firstLine = True
        for row in csv_data:
            row_dict = {}
            if firstLine:
                firstLine = False
                continue

            for col_2 in col_dict:
                print col_2
                col_index_2 = col_dict[col_2]
                try:
                    row_dict[col_2 + '_norm'] = (float(row[col_index_2]) - max_min_dict[col_2 + '_min']) / (
                    max_min_dict[col_2 + '_max'] - max_min_dict[col_2 + '_min'])
                except ZeroDivisionError:
                    row_dict[col_2 + '_norm'] = max_min_dict[col_2 + '_max']
                except ValueError:
                    row_dict[col_2 + '_norm'] = '999'
            row_dict['id'] = row[0]
            row_dict['PlayerName'] = row[1]
            row_dict['country_group'] = row[4]
            row_dict['Position'] = row[7]
            row_dict['DraftYear'] = row[8]
            row_dict['Overall'] = row[9]
            row_dict['sum_7yr_GP'] = row[23]
            row_dict['sum_7yr_TOI'] = row[24]
            row_dict['GP_greater_than_0'] = row[25]

            rows_list.append(row_dict)
        shutil.move(inputDir + "/" + fileName + '.csv', moveToDir + "/" + fileName + '.csv')

    fieldNames = ['id', 'PlayerName', 'DraftAge_norm', 'country_group', 'Height_norm', 'Weight_norm',
                      'Position', 'DraftYear', 'Overall', 'CSS_rank_norm', 'rs_GP_norm', 'rs_G_norm', 'rs_A_norm',
                      'rs_P_norm', 'rs_PIM_norm', 'rs_PlusMinus_norm',
                      'po_GP_norm', 'po_G_norm', 'po_A_norm', 'po_P_norm',
                      'po_PIM_norm', 'po_PlusMinus_norm', 'sum_7yr_GP', 'sum_7yr_TOI','GP_greater_than_0']

        # using the same naming format for csv files
    with open(outputDir + '/' + fileName[:-9] + "_norm.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)

