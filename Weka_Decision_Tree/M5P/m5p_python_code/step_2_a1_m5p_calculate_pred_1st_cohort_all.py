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
outputDir = '/Users/chao/GoogleDrive/2017-08-10_m5p'
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

            if CSS_rank_norm <= 0.127:
                leafNode = 1
                m5p_pred = 597.8472 * DraftAge_norm - 1.2577 * (country_group == 'CAN' or country_group == 'EURO') \
                           + 106.5363 * Height_norm + 10.1571 * Weight_norm - 1128.1086 * CSS_rank_norm \
                           + 289.2918 * rs_A_norm - 615.1441 * rs_PlusMinus_norm - 2.5092 * po_GP_norm \
                           + 14.3962 * po_A_norm + 394.2357

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 \
                    and rs_PlusMinus_norm <= 0.548:
                leafNode = 2
                m5p_pred = 9.3224 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 3.6096 * Height_norm + 22.0303 * Weight_norm - 14.2555 * CSS_rank_norm \
                           + 11.2123 * rs_A_norm + 17.6755 * rs_PlusMinus_norm - 0.7226 * po_GP_norm \
                           - 1.7353 * po_G_norm + 9.2861 * po_A_norm + 36.5947 * po_P_norm - \
                           21.9599 * po_PIM_norm - 2.2438 * po_PlusMinus_norm - 8.0038

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 \
                    and rs_PlusMinus_norm > 0.548:
                leafNode = 3
                m5p_pred = 9.3224 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 62.0161 * Height_norm + 114.511 * Weight_norm - 50.9901 * CSS_rank_norm \
                           + 47.6403 * rs_GP_norm + 7.4484 * rs_A_norm + 5.9361 * rs_PlusMinus_norm \
                           - 0.7226 * po_GP_norm - 1.7353 * po_G_norm + 9.2861 * po_A_norm \
                           + 191.6447 * po_P_norm - 164.7013 * po_PIM_norm - 2.2438 * po_PlusMinus_norm \
                           - 0.0034

            elif CSS_rank_norm >  0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm > 0.556:
                leafNode = 4
                m5p_pred = 9.3224 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 3.6096 * Height_norm + 17.8294 * Weight_norm - 11.7814 * CSS_rank_norm \
                           + 8.6264 * rs_A_norm - 2.5772 * rs_PlusMinus_norm - 0.7226 * po_GP_norm \
                           - 1.7353 * po_G_norm + 9.2861 * po_A_norm + 22.6332 * po_P_norm \
                           - 16.8695 * po_PIM_norm - 2.2438 * po_PlusMinus_norm + 2.712

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm <= 0.321:
                leafNode = 5
                m5p_pred = 29.983 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 168.8161 * Height_norm + 211.905 * Weight_norm \
                           - 40.8581 * (Position == 'D' or Position == 'L' or Position == 'C') \
                           + 39.4684 * (Position == 'L' or Position == 'C') - 7.1393 * CSS_rank_norm \
                           - 173.904 * rs_G_norm + 2.8499 * rs_A_norm + 147.6809 * rs_P_norm \
                           + 74.0613 * rs_PIM_norm - 2.5772 * rs_PlusMinus_norm + 9.4089 * po_GP_norm \
                           - 17.1355 * po_G_norm + 14.6416 * po_A_norm - 4.5815 * po_PlusMinus_norm + 39.748

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm > 0.321 \
                    and rs_G_norm <= 0.295:
                leafNode = 6
                m5p_pred = 54.2681 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 63.5365 * Height_norm + 226.12 * Weight_norm \
                           + 165.8188 * (Position == 'D' or Position == 'L' or Position == 'C') \
                           - 92.7196 * (Position == 'L' or Position == 'C') - 7.1393 * CSS_rank_norm \
                           + 458.7444 * rs_G_norm + 2.8499 * rs_A_norm + 23.6355 * rs_PIM_norm \
                           - 2.5772 * rs_PlusMinus_norm + 323.5786 * po_GP_norm - 39.951 * po_G_norm \
                           + 14.6416 * po_A_norm - 4.5815 * po_PlusMinus_norm - 213.005

            elif CSS_rank_norm >  0.127 and DraftAge_norm >  0.107 and DraftAge_norm > 0.321 \
                    and rs_G_norm > 0.295:
                leafNode = 7
                m5p_pred = 54.2681 * DraftAge_norm - 0.3622 * (country_group == 'CAN' or country_group == 'EURO') \
                           - 63.5365 * Height_norm + 75.669 * Weight_norm \
                           + 76.918 * (Position == 'D' or Position == 'L' or Position == 'C') \
                           - 40.2174 * (Position == 'L' or Position == 'C') - 7.1393 * CSS_rank_norm \
                           + 2.8499 * rs_A_norm + 23.6355 * rs_PIM_norm - 2.5772 * rs_PlusMinus_norm \
                           + 103.9115 * po_GP_norm - 39.951 * po_G_norm + 14.6416 * po_A_norm \
                           - 4.5815 * po_PlusMinus_norm - 4.1491


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


