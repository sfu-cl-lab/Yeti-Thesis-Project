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
    if file.endswith('1st_cohort_all_5_year_norm.csv'):
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
            CSS_rank_norm = float(row[9])
            if CSS_rank_norm > 1:
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

            if CSS_rank_norm <= 0.127 :
                leafNode = 1
                m5p_pred = 597.9996 * DraftAge_norm + 106.5363 * Height_norm + 9.8049 * Weight_norm - 1127.6081 * CSS_rank_norm + 289.3785 * rs_A_norm - 616.0347 * rs_PlusMinus_norm + 11.4244 * po_A_norm + 393.4203

            elif CSS_rank_norm >  0.127 and DraftAge_norm <= 0.107 and  rs_PlusMinus_norm <= 0.556 and\
                            rs_PlusMinus_norm <= 0.548 :
                leafNode = 2
                m5p_pred = 9.0388 * DraftAge_norm - 9.7452 * Height_norm + 21.9805 * Weight_norm - 12.7246 * CSS_rank_norm + 5.2956 * rs_GP_norm + 2.2765 * rs_G_norm + 2.8152 * rs_A_norm + 19.6862 * rs_PlusMinus_norm + 25.3498 * po_A_norm + 16.047 * po_P_norm - 25.1397 * po_PIM_norm - 2.4222 * po_PlusMinus_norm - 8.8717

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 \
                    and rs_PlusMinus_norm > 0.548:
                leafNode = 3
                m5p_pred = 9.0388 * DraftAge_norm - 64.9413 * Height_norm + 107.0689 * Weight_norm - 48.9355 * CSS_rank_norm + 51.9904 * rs_GP_norm + 2.2765 * rs_G_norm + 2.8152 * rs_A_norm + 6.2285 * rs_PlusMinus_norm + 18.1168 * po_A_norm + 176.7668 * po_P_norm - 162.0322 * po_PIM_norm - 2.4222 * po_PlusMinus_norm + 0.0954


            elif CSS_rank_norm >  0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm > 0.556:
                leafNode = 4
                m5p_pred = 9.0388 * DraftAge_norm - 3.3978 * Height_norm + 17.5093 * Weight_norm - 11.342 * CSS_rank_norm + 7.2895 * rs_G_norm + 2.8152 * rs_A_norm - 2.7749 * rs_PlusMinus_norm + 26.5349 * po_A_norm - 15.2928 * po_PIM_norm - 2.4222 * po_PlusMinus_norm + 2.0705


            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm <= 0.085 and rs_PIM_norm <= 0.044 :
                leafNode = 5
                m5p_pred = 14.5169 * DraftAge_norm - 70.5345 * Height_norm + 91.3478 * Weight_norm - 13.263 * (Position == 'D' or Position == 'L' or Position == 'C') + 12.7763 * (Position == 'L' or Position == 'C') - 6.9432 * CSS_rank_norm - 4.4902 * rs_G_norm + 34.0722 * rs_A_norm + 27.1771 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm + 11.6505 * po_A_norm - 5.0588 * po_PlusMinus_norm + 17.215

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm <= 0.085 and rs_PIM_norm > 0.044 :
                leafNode = 6
                m5p_pred = 18.1169 * DraftAge_norm - 70.5345 * Height_norm + 91.3478 * Weight_norm - 13.263 * (Position == 'D' or Position == 'L' or Position == 'C') + 12.7763 * (Position == 'L' or Position == 'C') - 6.9432 * CSS_rank_norm + 30.0379 * rs_G_norm + 34.0722 * rs_A_norm + 24.9946 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm + 11.6505 * po_A_norm - 5.0588 * po_PlusMinus_norm + 16.5097

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm >  0.085 and Weight_norm <= 0.413:
                leafNode = 7
                m5p_pred = 8.9168 * DraftAge_norm - 202.2526 * Height_norm + 216.8269 * Weight_norm - 13.9623 * (Position == 'D' or Position == 'L' or Position == 'C') + 12.9743 * (Position == 'L' or Position == 'C') - 6.9432 * CSS_rank_norm - 74.8297 * rs_G_norm + 32.2248 * rs_A_norm + 7.504 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm - 76.1213 * po_GP_norm - 11.4836 * po_G_norm + 184.9085 * po_A_norm - 5.0588 * po_PlusMinus_norm + 61.8264

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm >  0.085 and Weight_norm > 0.413 and CSS_rank_norm <= 0.328 and\
                            Height_norm <= 0.464:
                leafNode = 8
                m5p_pred = 28.9168 * DraftAge_norm - 84.8117 * Height_norm + 113.3567 * Weight_norm - 61.8256 * (Position == 'D' or Position == 'L' or Position == 'C') + 97.6642 * (Position == 'L' or Position == 'C') - 34.5661 * CSS_rank_norm - 122.4925 * rs_G_norm + 77.312 * rs_A_norm + 7.504 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm + 11.6505 * po_A_norm - 185.2811 * po_PlusMinus_norm + 163.1801

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm >  0.085 and Weight_norm > 0.413 and CSS_rank_norm <= 0.328 and\
                            Height_norm > 0.464 and po_A_norm <= 0.212:
                leafNode = 9
                m5p_pred = 28.9168 * DraftAge_norm - 29.319 * (country_group == 'CAN' or country_group == 'EURO') - 84.8117 * Height_norm + 113.3567 * Weight_norm - 71.5109 * (Position == 'D' or Position == 'L' or Position == 'C') + 59.5398 * (Position == 'L' or Position == 'C') - 34.5661 * CSS_rank_norm - 112.692 * rs_G_norm + 77.312 * rs_A_norm + 21.7638 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm - 5.3805 * po_A_norm - 151.3431 * po_PlusMinus_norm + 178.5752

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm >  0.085 and Weight_norm > 0.413 and CSS_rank_norm <= 0.328 and\
                            Height_norm > 0.464 and po_A_norm > 0.212:
                leafNode = 10
                m5p_pred = 28.9168 * DraftAge_norm - 17.3613 * (country_group == 'CAN' or country_group == 'EURO') - 84.8117 * Height_norm + 113.3567 * Weight_norm - 62.7262 * (Position == 'D' or Position == 'L' or Position == 'C') + 59.5398 * (Position == 'L' or Position == 'C') - 34.5661 * CSS_rank_norm - 112.692 * rs_G_norm + 77.312 * rs_A_norm + 27.8751 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm - 12.6795 * po_A_norm - 151.3431 * po_PlusMinus_norm + 158.4673

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321 and\
                            rs_P_norm >  0.085 and Weight_norm > 0.413 and CSS_rank_norm > 0.328:
                leafNode = 11
                m5p_pred = 28.9168 * DraftAge_norm - 84.8117 * Height_norm + 113.3567 * Weight_norm - 60.673 * (Position == 'D' or Position == 'L' or Position == 'C') + 59.5734 * (Position == 'L' or Position == 'C') - 59.8871 * CSS_rank_norm - 132.5608 * rs_G_norm + 112.2421 * rs_A_norm + 7.504 * rs_PIM_norm - 2.7749 * rs_PlusMinus_norm + 10.9267 * po_GP_norm - 11.4836 * po_G_norm + 11.6505 * po_A_norm - 137.601 * po_PlusMinus_norm + 134.5219

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm > 0.321 and \
                            rs_G_norm <= 0.295:
                leafNode = 12
                m5p_pred = 52.136 * DraftAge_norm - 62.2143 * Height_norm + 228.719 * Weight_norm + 165.9862 * (Position == 'D' or Position == 'L' or Position == 'C') - 92.8132 * (Position == 'L' or Position == 'C') - 6.9432 * CSS_rank_norm + 459.2074 * rs_G_norm + 2.8152 * rs_A_norm - 2.7749 * rs_PlusMinus_norm + 326.9261 * po_GP_norm - 30.9647 * po_G_norm + 11.6505 * po_A_norm - 5.0588 * po_PlusMinus_norm - 212.2504

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm > 0.321 and \
                            rs_G_norm > 0.295:
                leafNode = 13
                m5p_pred = 52.136 * DraftAge_norm - 62.2143 * Height_norm + 78.1161 * Weight_norm + 76.9957 * (Position == 'D' or Position == 'L' or Position == 'C') - 40.258 * (Position == 'L' or Position == 'C') - 6.9432 * CSS_rank_norm + 2.8152 * rs_A_norm - 2.7749 * rs_PlusMinus_norm + 107.0373 * po_GP_norm - 30.9647 * po_G_norm + 11.6505 * po_A_norm - 5.0588 * po_PlusMinus_norm - 3.1836

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

    with open(outputDir + "/m5p_1st_cohort_all_5_year_norm_pred.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


