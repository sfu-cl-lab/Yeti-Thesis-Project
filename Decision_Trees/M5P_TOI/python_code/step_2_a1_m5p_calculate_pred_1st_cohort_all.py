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
            leafNode = 'null'

            if CSS_rank_norm <= 0.127:
                leafNode = 1
                m5p_pred = 10427.702 * DraftAge_norm + 149.6874 * Weight_norm + 1096.9188 * (
                Position == 'D') - 20337.991 * CSS_rank_norm + 5525.0183 * rs_A_norm - 96.0679 * rs_PIM_norm - 167.6074 * rs_PlusMinus_norm - 280.3559 * po_G_norm + 427.1036 * po_P_norm + 1257.7288

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm <= 0.548:
                leafNode = 2
                m5p_pred = 163.968 * DraftAge_norm - 135.1609 * Height_norm + 314.55 * Weight_norm + 6.7023 * (
                Position == 'D') - 187.3613 * CSS_rank_norm - 31.8671 * rs_G_norm + 191.466 * rs_A_norm - 27.0918 * rs_PIM_norm + 198.6178 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 768.2221 * po_P_norm - 383.7508 * po_PIM_norm - 76.6293

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm <= 0.033:
                leafNode = 3
                m5p_pred = 163.968 * DraftAge_norm - 986.5307 * Height_norm + 1290.888 * Weight_norm + 6.7023 * (
                Position == 'D') - 634.0948 * CSS_rank_norm + 68.0415 * rs_GP_norm - 31.8671 * rs_G_norm + 146.1291 * rs_A_norm - 91.8425 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 707.8166 * po_P_norm - 382.6898 * po_PIM_norm + 348.5094

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and rs_PIM_norm <= 0.14:
                leafNode = 4
                m5p_pred = 163.968 * DraftAge_norm - 263.9612 * Height_norm + 482.2982 * Weight_norm + 6.7023 * (
                Position == 'D') - 248.3079 * CSS_rank_norm + 715.7193 * rs_GP_norm - 2489.2316 * rs_G_norm + 3104.7879 * rs_A_norm - 1318.5244 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 1034.6945 * po_P_norm - 630.3842 * po_PIM_norm + 473.2571

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and rs_PIM_norm > 0.14:
                leafNode = 5
                m5p_pred = 163.968 * DraftAge_norm - 263.9612 * Height_norm + 482.2982 * Weight_norm + 6.7023 * (
                Position == 'D') - 248.3079 * CSS_rank_norm + 781.4397 * rs_GP_norm - 612.3799 * rs_G_norm + 780.8312 * rs_A_norm - 1453.7244 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 1034.6945 * po_P_norm - 630.3842 * po_PIM_norm + 61.0233

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm > 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033:
                leafNode = 6
                m5p_pred = 163.968 * DraftAge_norm - 52.4564 * Height_norm + 223.5991 * Weight_norm + 6.7023 * (
                Position == 'D') - 165.0673 * CSS_rank_norm - 31.8671 * rs_G_norm + 168.9468 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 542.7248 * po_P_norm - 281.2213 * po_PIM_norm + 31.5981

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and DraftAge_norm <= 0.321:
                leafNode = 7
                m5p_pred = 543.3077 * DraftAge_norm - 2653.6617 * Height_norm + 2944.0775 * Weight_norm - 360.5671 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 1808.1757 * rs_G_norm + 2083.5774 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 96.8336 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 606.2757

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and DraftAge_norm > 0.321 and Position == 'D':
                leafNode = 8
                m5p_pred = 995.4115 * DraftAge_norm - 1048.2937 * Height_norm + 1043.7941 * Weight_norm + 1020.4324 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm + 2443.8734 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 1897.2435 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm - 230.9171

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm <= 0.117:
                leafNode = 9
                m5p_pred = 995.4115 * DraftAge_norm - 4900.9862 * Height_norm + 4697.1298 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm + 1775.8938 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4783.1616 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 199.7798

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm > 0.117 and po_P_norm <= 0.141 and Weight_norm <= 0.365:
                leafNode = 10
                m5p_pred = 995.4115 * DraftAge_norm - 6023.5196 * Height_norm + 7089.2424 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4174.7677 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 586.8466
            if CSS_rank_norm <= 0.127:
                leafNode = 1
                m5p_pred = 10427.702 * DraftAge_norm + 149.6874 * Weight_norm + 1096.9188 * (
                Position == 'D') - 20337.991 * CSS_rank_norm + 5525.0183 * rs_A_norm - 96.0679 * rs_PIM_norm - 167.6074 * rs_PlusMinus_norm - 280.3559 * po_G_norm + 427.1036 * po_P_norm + 1257.7288

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm <= 0.548:
                leafNode = 2
                m5p_pred = 163.968 * DraftAge_norm - 135.1609 * Height_norm + 314.55 * Weight_norm + 6.7023 * (
                Position == 'D') - 187.3613 * CSS_rank_norm - 31.8671 * rs_G_norm + 191.466 * rs_A_norm - 27.0918 * rs_PIM_norm + 198.6178 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 768.2221 * po_P_norm - 383.7508 * po_PIM_norm - 76.6293

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm <= 0.033:
                leafNode = 3
                m5p_pred = 163.968 * DraftAge_norm - 986.5307 * Height_norm + 1290.888 * Weight_norm + 6.7023 * (
                Position == 'D') - 634.0948 * CSS_rank_norm + 68.0415 * rs_GP_norm - 31.8671 * rs_G_norm + 146.1291 * rs_A_norm - 91.8425 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 707.8166 * po_P_norm - 382.6898 * po_PIM_norm + 348.5094

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and rs_PIM_norm <= 0.14:
                leafNode = 4
                m5p_pred = 163.968 * DraftAge_norm - 263.9612 * Height_norm + 482.2982 * Weight_norm + 6.7023 * (
                Position == 'D') - 248.3079 * CSS_rank_norm + 715.7193 * rs_GP_norm - 2489.2316 * rs_G_norm + 3104.7879 * rs_A_norm - 1318.5244 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 1034.6945 * po_P_norm - 630.3842 * po_PIM_norm + 473.2571

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm <= 0.556 and rs_PlusMinus_norm > 0.548 and po_P_norm > 0.033 and rs_PIM_norm > 0.14:
                leafNode = 5
                m5p_pred = 163.968 * DraftAge_norm - 263.9612 * Height_norm + 482.2982 * Weight_norm + 6.7023 * (
                Position == 'D') - 248.3079 * CSS_rank_norm + 781.4397 * rs_GP_norm - 612.3799 * rs_G_norm + 780.8312 * rs_A_norm - 1453.7244 * rs_PIM_norm + 51.2948 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 1034.6945 * po_P_norm - 630.3842 * po_PIM_norm + 61.0233

            elif CSS_rank_norm > 0.127 and DraftAge_norm <= 0.107 and rs_PlusMinus_norm > 0.556:
                leafNode = 6
                m5p_pred = 163.968 * DraftAge_norm - 52.4564 * Height_norm + 223.5991 * Weight_norm + 6.7023 * (
                Position == 'D') - 165.0673 * CSS_rank_norm - 31.8671 * rs_G_norm + 168.9468 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm - 79.0623 * po_G_norm + 542.7248 * po_P_norm - 281.2213 * po_PIM_norm + 31.5981

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm <= 0.321:
                leafNode = 7
                m5p_pred = 543.3077 * DraftAge_norm - 2653.6617 * Height_norm + 2944.0775 * Weight_norm - 360.5671 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 1808.1757 * rs_G_norm + 2083.5774 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 96.8336 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 606.2757

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm > 0.321 and Position == 'D':
                leafNode = 8
                m5p_pred = 995.4115 * DraftAge_norm - 1048.2937 * Height_norm + 1043.7941 * Weight_norm + 1020.4324 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm + 2443.8734 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 1897.2435 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm - 230.9171

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm <= 0.117:
                leafNode = 9
                m5p_pred = 995.4115 * DraftAge_norm - 4900.9862 * Height_norm + 4697.1298 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm + 1775.8938 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4783.1616 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 199.7798

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm > 0.117 and po_P_norm <= 0.141 and Weight_norm <= 0.365:
                leafNode = 10
                m5p_pred = 995.4115 * DraftAge_norm - 6023.5196 * Height_norm + 7089.2424 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4174.7677 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 586.8466

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm > 0.117 and po_P_norm <= 0.141 and Weight_norm > 0.365:
                leafNode = 11
                m5p_pred = 995.4115 * DraftAge_norm - 6256.8001 * Height_norm + 7089.2424 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4174.7677 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 794.9421

            elif CSS_rank_norm > 0.127 and DraftAge_norm > 0.107 and DraftAge_norm > 0.321 and Position != 'D' and po_GP_norm > 0.117 and po_P_norm > 0.141:
                leafNode = 12
                m5p_pred = 995.4115 * DraftAge_norm - 6781.1181 * Height_norm + 7323.5996 * Weight_norm + 1044.9918 * (
                Position == 'D') - 112.9595 * CSS_rank_norm - 66.5558 * rs_G_norm + 135.6548 * rs_A_norm - 27.0918 * rs_PIM_norm - 47.2664 * rs_PlusMinus_norm + 4174.7677 * po_GP_norm - 79.0623 * po_G_norm + 202.1105 * po_P_norm + 1034.1508

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

    with open(outputDir + "/m5p_1st_cohort_all_5_year_norm_TOI_pred.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


