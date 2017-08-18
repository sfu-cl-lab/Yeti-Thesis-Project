import csv
import os
import shutil
import time
import numpy as np

# newly crawled betting lines are saved in the inputDir folder
# inputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/leaf_nodes"
inputDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI'
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI/cross_validation'
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI'

fileNameList = [] # all file names in the input folder are saved in this list
for file in os.listdir(inputDir):
    if file.endswith('2nd_cohort_all_5_year_norm.csv'):
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
            leafNode = 'null'

            if CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm <= 0.006:
                leafNode = 1
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') + 4520.3124 * Height_norm + 5295.4732 * Weight_norm - 314989.0034 * CSS_rank_norm + 4558.1496 * rs_A_norm - 8200.0205 * rs_PIM_norm - 861.9936 * po_G_norm + 177.4996 * po_A_norm + 2431.5377 * po_P_norm + 877.4118

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm <= 0.15 and rs_PlusMinus_norm <= 0.39 and po_P_norm <= 0.054 and Height_norm <= 0.719:
                leafNode = 2
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') + 2191.2929 * Height_norm + 3210.945 * Weight_norm - 551.972 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 1941.651 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 6243.6764 * po_P_norm + 712.6242

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm <= 0.15 and rs_PlusMinus_norm <= 0.39 and po_P_norm <= 0.054 and Height_norm > 0.719:
                leafNode = 3
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') + 2247.1651 * Height_norm + 3210.945 * Weight_norm - 551.972 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 1941.651 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 6243.6764 * po_P_norm + 724.5735

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm <= 0.15 and rs_PlusMinus_norm <= 0.39 and po_P_norm > 0.054:
                leafNode = 4
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') + 2616.463 * Height_norm + 3210.945 * Weight_norm - 551.972 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 1941.651 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 6686.5627 * po_P_norm + 667.5456

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm <= 0.15 and rs_PlusMinus_norm > 0.39:
                leafNode = 5
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') + 1762.504 * Height_norm + 3210.945 * Weight_norm - 551.972 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 1941.651 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 5895.1386 * po_P_norm + 839.8362

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm > 0.15 and rs_GP_norm <= 0.675:
                leafNode = 6
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') - 197.5876 * Height_norm + 3210.945 * Weight_norm - 1322.8024 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 4388.3025 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm + 1580.7687 * rs_PlusMinus_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 1151.781 * po_P_norm + 4846.0332

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm <= 0.034 and CSS_rank_norm > 0.006 and rs_A_norm > 0.15 and rs_GP_norm > 0.675:
                leafNode = 7
                m5p_pred = 167.7573 * DraftAge_norm + 34.4004 * (
                country_group == 'USA' or country_group == 'CAN') - 197.5876 * Height_norm + 3210.945 * Weight_norm - 1059.7911 * (
                Position == 'R' or Position == 'L' or Position == 'C') - 27386.8678 * CSS_rank_norm - 5436.8674 * rs_GP_norm + 5962.7819 * rs_A_norm - 1861.6987 * rs_PIM_norm + 2258.2411 * rs_PlusMinus_norm - 1307.5802 * po_G_norm + 177.4996 * po_A_norm + 1151.781 * po_P_norm + 4511.0261

            elif CSS_rank_norm <= 0.091 and CSS_rank_norm > 0.034:
                leafNode = 8
                m5p_pred = 167.7573 * DraftAge_norm + 668.1857 * (
                country_group == 'USA' or country_group == 'CAN') - 197.5876 * Height_norm + 1080.6367 * Weight_norm - 7985.6913 * CSS_rank_norm + 4300.3035 * rs_A_norm - 552.7515 * rs_PIM_norm + 177.4996 * po_A_norm + 4371.865 * po_PlusMinus_norm - 1269.4154

            elif CSS_rank_norm > 0.091:
                leafNode = 9
                m5p_pred = 2215.7209 * DraftAge_norm + 9.7247 * (
                country_group == 'USA' or country_group == 'CAN') - 2772.3565 * Height_norm + 1870.7797 * Weight_norm - 355.6245 * (
                Position == 'C') - 960.7474 * CSS_rank_norm - 1683.0563 * rs_G_norm + 3229.8694 * rs_A_norm - 650.0636 * rs_PIM_norm + 1212.8107 * po_G_norm + 50.1778 * po_A_norm + 1463.4346


            xk = {'id': int(row[0]), 'PlayerName': row[1], 'DraftAge_norm': DraftAge_norm, 'country_group': country_group,
                  'Height_norm': Height_norm,
                  'Weight_norm': Weight_norm, 'Position': Position, 'DraftYear': int(row[7]), 'Overall': int(row[8]),
                  'CSS_rank_norm': CSS_rank_norm,
                  'rs_GP_norm': rs_GP_norm, 'rs_G_norm': rs_G_norm, 'rs_A_norm': rs_A_norm,
                  'rs_P_norm': rs_P_norm, 'rs_PIM_norm': rs_PIM_norm,
                  'rs_PlusMinus_norm': rs_PlusMinus_norm, 'po_GP_norm': po_GP_norm, 'po_G_norm': po_G_norm,
                  'po_A_norm': po_A_norm, 'po_P_norm': po_P_norm,
                  'po_PIM_norm': po_PIM_norm, 'po_PlusMinus_norm': po_PlusMinus_norm, 'sum_7yr_TOI': row[23],
                  'm5p_pred': m5p_pred, 'LeafNode': leafNode}
            rows_list.append(xk)
        shutil.move(inputDir + "/" + fileName + '.csv', moveToDir + "/" + fileName + '.csv')

    fieldNames = ['id','PlayerName', 'DraftAge_norm', 'country_group','Height_norm', 'Weight_norm',
                  'Position', 'DraftYear','Overall','CSS_rank_norm', 'rs_GP_norm', 'rs_G_norm', 'rs_A_norm',
                  'rs_P_norm', 'rs_PIM_norm', 'rs_PlusMinus_norm',
                  'po_GP_norm', 'po_G_norm', 'po_A_norm', 'po_P_norm',
                  'po_PIM_norm' , 'po_PlusMinus_norm', 'sum_7yr_TOI', 'm5p_pred', 'LeafNode']

    with open(outputDir + "/m5p_2nd_cohort_all_5_year_norm_TOI_pred.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


