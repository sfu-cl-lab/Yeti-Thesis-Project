import csv
import os
import shutil
import time
import numpy as np

# newly crawled betting lines are saved in the inputDir folder
# inputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/leaf_nodes"
inputDir = '/Users/chao/GoogleDrive/2017-08-10_m5p'
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = '/Users/chao/GoogleDrive/2017-08-10_m5p/cross_validation'
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = '/Users/chao/GoogleDrive/2017-08-10_m5p'

fileNameList = [] # all file names in the input folder are saved in this list
for file in os.listdir(inputDir):
    if file.endswith('2nd_cohort_nonzero_5_year_norm.csv'):
        #splitext(file)[0] remove the .txt extension from file name
        fileName = os.path.splitext(file)[0]
        fileNameList.append(fileName)
print fileNameList

rows_list = []
for fileName in fileNameList:
    with open(inputDir + "/" + fileName + '.csv', 'r') as inputFile:
        csv_data = csv.reader(inputFile)
        firstLine = True
        for row in csv_data:
            if firstLine:
                firstLine = False
                continue
            DraftAge_norm = float(row[2])
            country_group = row[3]
            Height_norm = float(row[4])
            Weight_norm = float(row[5])
            Position = row[6]
            try:
                CSS_rank_norm = float(row[9])
            except ValueError:
                CSS_rank_norm = 1
            rs_GP_norm = float(row[10])
            rs_G_norm = float(row[11])
            rs_A_norm = float(row[12])
            rs_P_norm = float(row[13])
            rs_PIM_norm = float(row[14])
            rs_PlusMinus_norm = float(row[15])
            po_GP_norm = float(row[16])
            po_G_norm = float(row[17])
            po_A_norm = float(row[18])
            po_P_norm = float(row[19])
            po_PIM_norm = float(row[20])
            po_PlusMinus_norm = float(row[21])

            m5p_pred = 0.000

            if CSS_rank_norm <= 0.046 :
                leafNode = 1
                m5p_pred = 20.7453 * DraftAge_norm - 36.3923 * Height_norm + 48.9316 * Weight_norm - 4574.6118 * CSS_rank_norm + 38.0795 * rs_A_norm + 369.2346 * rs_PlusMinus_norm - 10.0392 * po_GP_norm + 35.5451 * po_G_norm + 165.2282

            elif CSS_rank_norm >  0.046 and po_P_norm <= 0.076:
                leafNode = 2
                m5p_pred = 17.5651 * DraftAge_norm - 229.522 * Height_norm + 222.9462 * Weight_norm + 1.9807 * (Position == 'R' or Position == 'L') - 14.5463 * CSS_rank_norm - 13.0132 * rs_G_norm + 36.6428 * rs_A_norm - 74.1137 * rs_PIM_norm + 9.0977 * rs_PlusMinus_norm - 7.1763 * po_GP_norm + 27.0008 * po_G_norm + 137.3803

            elif CSS_rank_norm >  0.046 and po_P_norm > 0.076:
                leafNode = 3
                m5p_pred = 29.2156 * DraftAge_norm - 52.3832 * Height_norm + 47.4811 * Weight_norm + 4.0569 * (Position == 'R' or Position == 'L') + 51.1164 * (Position == 'L') - 19.6737 * CSS_rank_norm - 26.6534 * rs_G_norm + 257.6262 * rs_A_norm + 9.0977 * rs_PlusMinus_norm - 11.4267 * po_GP_norm + 43.7184 * po_G_norm + 75.9537

            xk = {'id': int(row[0]), 'PlayerName': row[1], 'DraftAge_norm': DraftAge_norm, 'country_group': country_group,
                  'Height_norm': Height_norm,
                  'Weight_norm': Weight_norm, 'Position': Position, 'DraftYear': int(row[7]), 'Overall': int(row[8]),
                  'CSS_rank_norm': CSS_rank_norm,
                  'rs_GP_norm': rs_GP_norm, 'rs_G_norm': rs_G_norm, 'rs_A_norm': rs_A_norm,
                  'rs_P_norm': rs_P_norm, 'rs_PIM_norm': rs_PIM_norm,
                  'rs_PlusMinus_norm': rs_PlusMinus_norm, 'po_GP_norm': po_GP_norm, 'po_G_norm': po_G_norm,
                  'po_A_norm': po_A_norm, 'po_P_norm': po_P_norm,
                  'po_PIM_norm': po_PIM_norm, 'po_PlusMinus_norm': po_PlusMinus_norm, 'sum_7yr_GP': row[22],
                  'm5p_pred': m5p_pred, 'LeafNode': leafNode}
            rows_list.append(xk)
        shutil.move(inputDir + "/" + fileName + '.csv', moveToDir + "/" + fileName + '.csv')

    fieldNames = ['id','PlayerName', 'DraftAge_norm', 'country_group','Height_norm', 'Weight_norm',
                  'Position', 'DraftYear','Overall','CSS_rank_norm', 'rs_GP_norm', 'rs_G_norm', 'rs_A_norm',
                  'rs_P_norm', 'rs_PIM_norm', 'rs_PlusMinus_norm',
                  'po_GP_norm', 'po_G_norm', 'po_A_norm', 'po_P_norm',
                  'po_PIM_norm' , 'po_PlusMinus_norm', 'sum_7yr_GP', 'm5p_pred', 'LeafNode']

    with open(outputDir + "/m5p_2nd_cohort_nonzero_5_year_norm_pred.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


