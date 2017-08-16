import csv
import os
import shutil
import time
import numpy as np

# newly crawled betting lines are saved in the inputDir folder
# inputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/leaf_nodes"
inputDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'

fileNameList = [] # all file names in the input folder are saved in this list
for file in os.listdir(inputDir):
    if file.endswith('2nd_cohort_5_year_norm.csv'):
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

            lmt_prob = 0.000
            wx_sum = 0.000

            if CSS_rank_norm <= 0.046371:
                leafNode = 1
                wx_sum = 1.682576219  + DraftAge_norm * -0.6521969619 + (country_group == 'EURO') * 0.2515058744 + (country_group == 'CAN') * -0.7372739476 + Height_norm * 0.9108602568 + Weight_norm * -3.0647516341 + (Position == 'D') * 0.3626622956 + CSS_rank_norm * 19.0327179101 + rs_A_norm * -1.416228717 + rs_P_norm * -2.5182072847 + po_A_norm * -2.5818151743 + po_PlusMinus_norm * -4.5578802919

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm <= 0.061171:
                leafNode = 2
                wx_sum = 0.0225110366 + DraftAge_norm * -0.6521969619 + (country_group == 'EURO') * 0.3823693577 + (country_group == 'USA') * 0.2452964509 + Height_norm * 1.6148625242 + Weight_norm * -1.1902369165 + (Position == 'D') * 0.2475813803 + (Position == 'R') * -0.6514414089 + CSS_rank_norm * 1.7003217418 + rs_GP_norm * -0.623606065 + rs_G_norm * 0.4156266673 + rs_A_norm * -1.416228717 + rs_P_norm * -9.2361288366 + rs_PIM_norm * 0.4704279537 + rs_PlusMinus_norm * 0.516339445  + po_GP_norm * 0.6961231358 + po_PIM_norm * -0.7606931178

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm <= 0.362385 and \
                            rs_PlusMinus_norm <= 0.353211:
                leafNode = 3
                wx_sum = 0.2596899624 + DraftAge_norm * -1.2673609724 + (country_group == 'EURO') * 1.2307595534 + (country_group == 'USA') * -0.8069462064 + Height_norm * 2.2083451086 + Weight_norm * -2.1613141404 + (Position == 'D') * -0.105873252 + (Position == 'L') * -0.4271360663 + CSS_rank_norm * 1.9138640157 + rs_GP_norm * -1.5673201838 + rs_G_norm * 0.4156266673 + rs_A_norm * -0.4239688038 + rs_PIM_norm * 0.8031514348 + rs_PlusMinus_norm * -2.9754056872 + po_P_norm * 2.6843997425 + po_PIM_norm * -0.7606931178 + po_PlusMinus_norm * 2.447755103

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm <= 0.362385 and \
                            rs_PlusMinus_norm > 0.353211:
                leafNode = 4
                wx_sum = -1.0888160283 + DraftAge_norm * -1.2673609724 + (country_group == 'EURO') * -0.463850402 + Height_norm * 2.2083451086 + Weight_norm * -0.2293666258 + (Position == 'D') * -0.105873252 + (Position == 'L') * 0.0688557505 + CSS_rank_norm * 1.4879418811 + rs_GP_norm * -1.0477475885 + rs_G_norm * 0.4156266673 + rs_A_norm * -0.4239688038 + rs_P_norm * 0.5796943481 + rs_PIM_norm * 0.8031514348 + rs_PlusMinus_norm * -2.9754056872 + po_P_norm * 0.2898101074 + po_PIM_norm * -0.7606931178 + po_PlusMinus_norm * 2.447755103

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm > 0.362385 and \
                            po_A_norm <= 0.35:
                leafNode = 5
                wx_sum = 1.5482744147 + DraftAge_norm * 1.1198806299 + (country_group == 'EURO') * 0.9510946135 + Height_norm * -0.1943101707 + Weight_norm * -1.1902369165 + (Position == 'D') * -0.310508047 + (Position == 'R') * -0.1937918628 + (Position == 'L') * -0.1239741776 + CSS_rank_norm * 0.3503937449 + rs_GP_norm * -1.0504894229 + rs_G_norm * -0.1686151641 + rs_A_norm * -0.4239688038 + rs_P_norm * -0.5370008872 + rs_PIM_norm * 0.8031514348 + rs_PlusMinus_norm * 0.8075548697 + po_GP_norm * -0.3212562576 + po_PIM_norm * -1.4663079409
                lmt_prob = 1 / (1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm > 0.362385 and \
                            po_A_norm > 0.35:
                leafNode = 6
                wx_sum = -3.106876138 + DraftAge_norm * -0.0975778883 + (country_group == 'EURO') * 8.8551596038 + Height_norm * 0.6618192176 + Weight_norm * -1.1902369165 + (Position == 'D') * -0.105873252 + (Position == 'L') * -0.1239741776 + CSS_rank_norm * 0.3503937449 + rs_GP_norm * -1.0504894229 + rs_G_norm * 0.4156266673 + rs_A_norm * -0.4239688038 + rs_PIM_norm * 0.8031514348 + rs_PlusMinus_norm * 0.8075548697 + po_GP_norm * -1.089093825 + po_PIM_norm * -1.4663079409

                lmt_prob = 1 / (1 + np.exp(wx_sum))



            xk = {'id': int(row[0]), 'PlayerName': row[1], 'DraftAge_norm': DraftAge_norm, 'country_group': country_group,
                  'Height_norm': Height_norm,
                  'Weight_norm': Weight_norm, 'Position': Position, 'DraftYear': int(row[7]), 'Overall': int(row[8]),
                  'CSS_rank_norm': CSS_rank_norm,
                  'rs_GP_norm': rs_GP_norm, 'rs_G_norm': rs_G_norm, 'rs_A_norm': rs_A_norm,
                  'rs_P_norm': rs_P_norm, 'rs_PIM_norm': rs_PIM_norm,
                  'rs_PlusMinus_norm': rs_PlusMinus_norm, 'po_GP_norm': po_GP_norm, 'po_G_norm': po_G_norm,
                  'po_A_norm': po_A_norm, 'po_P_norm': po_P_norm,
                  'po_PIM_norm': po_PIM_norm, 'po_PlusMinus_norm': po_PlusMinus_norm, 'GP_greater_than_0': row[24],
                  'wx_sum': wx_sum, 'lmt_prob': lmt_prob, 'LeafNode': leafNode}
            rows_list.append(xk)
        shutil.move(inputDir + "/" + fileName + '.csv', moveToDir + "/" + fileName + '.csv')

    fieldNames = ['id','PlayerName', 'DraftAge_norm', 'country_group','Height_norm', 'Weight_norm',
                  'Position', 'DraftYear','Overall','CSS_rank_norm', 'rs_GP_norm', 'rs_G_norm', 'rs_A_norm',
                  'rs_P_norm', 'rs_PIM_norm', 'rs_PlusMinus_norm',
                  'po_GP_norm', 'po_G_norm', 'po_A_norm', 'po_P_norm',
                  'po_PIM_norm' , 'po_PlusMinus_norm', 'GP_greater_than_0', 'wx_sum', 'lmt_prob', 'LeafNode']

    with open(outputDir + "/lmt_2nd_cohort_5_year_norm_prob.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


