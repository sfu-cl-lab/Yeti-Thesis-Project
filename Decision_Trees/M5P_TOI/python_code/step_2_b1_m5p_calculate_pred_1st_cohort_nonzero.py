import csv
import os
import shutil
import time
import numpy as np

# newly crawled betting lines are saved in the inputDir folder
inputDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI'
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI/cross_validation'
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = '/Users/chao/GoogleDrive/2017-08-17_m5p_TOI'

fileNameList = [] # all file names in the input folder are saved in this list
for file in os.listdir(inputDir):
    if file.endswith('1st_cohort_nonzero_5_year_norm.csv'):
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
            leafNode = 'null'

            if CSS_rank_norm <= 0.093 and CSS_rank_norm <= 0.017:
                leafNode = 1
                m5p_pred = 3573.3658 * DraftAge_norm + 179.522 * (
                Position == 'D') - 9208.6277 * CSS_rank_norm - 106.1984 * rs_G_norm + 3739.3463 * rs_A_norm - 1807.4276 * rs_P_norm - 246.5753 * rs_PIM_norm - 174.3255 * po_GP_norm + 481.9355 * po_A_norm + 3510.762

            elif CSS_rank_norm <= 0.093 and CSS_rank_norm > 0.017:
                leafNode = 2
                m5p_pred = 1697.3487 * DraftAge_norm + 179.522 * (
                Position == 'D') - 4622.9578 * CSS_rank_norm - 2149.257 * rs_G_norm + 7403.2933 * rs_A_norm - 1807.4276 * rs_P_norm - 246.5753 * rs_PIM_norm - 174.3255 * po_GP_norm + 481.9355 * po_A_norm + 1729.0252

            elif CSS_rank_norm > 0.093 and Position == 'D':
                leafNode = 3
                m5p_pred = 157.843 * DraftAge_norm - 2056.1705 * Height_norm + 1981.9355 * Weight_norm + 157.9098 * (
                Position == 'D') - 315.7615 * CSS_rank_norm - 1051.8231 * rs_GP_norm + 406.4032 * rs_G_norm + 549.5855 * rs_A_norm - 802.4355 * rs_P_norm - 310.1854 * rs_PIM_norm - 1204.8065 * po_GP_norm + 3033.1403 * po_A_norm + 1808.4096

            elif CSS_rank_norm > 0.093 and Position != 'D':
                leafNode = 4
                m5p_pred = 3554.2616 * DraftAge_norm - 478.9424 * Height_norm + 429.0829 * Weight_norm + 231.4628 * (
                Position == 'D') - 414.8065 * CSS_rank_norm + 9273.5456 * rs_G_norm - 3279.5259 * rs_A_norm - 802.4355 * rs_P_norm - 498.9527 * rs_PIM_norm - 77.3945 * po_GP_norm + 3640.9323 * po_A_norm + 856.2872



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

    with open(outputDir + "/m5p_1st_cohort_nonzero_5_year_norm_TOI_pred.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


