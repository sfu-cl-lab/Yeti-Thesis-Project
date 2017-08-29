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
    if file.endswith('1st_cohort_5_year_norm.csv'):
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

            if po_PlusMinus_norm <= 0.354166: 
			    leafNode = 1
			    wx_sum = -3.0996183241 + DraftAge_norm * 1.5253614015 + Weight_norm * 1.4919620265 + CSS_rank_norm * -1.256756345 + rs_A_norm * -1.3622035894 + rs_P_norm * 1.5706334136 
			    lmt_prob = 1/(1 + np.exp(-wx_sum))

			elif po_PlusMinus_norm > 0.354166 and po_PlusMinus_norm <= 0.395834 and rs_PlusMinus_norm <= 0.548:
			    leafNode = 2
			    wx_sum = -2.3823397672 + DraftAge_norm * 2.2681273438 + (country_group == 'EURO') * -0.1901788186 + Weight_norm * 1.5706434401 + CSS_rank_norm * -1.4750414248 + rs_GP_norm * 1.1639704533 + rs_P_norm * 1.5706334136 + rs_PlusMinus_norm * 1.8081514932 + po_P_norm * 1.4172451085 + po_PIM_norm * 22.3783855159 + po_PlusMinus_norm * -7.1433895008 
			    lmt_prob = 1/(1 + np.exp(-wx_sum))

			elif po_PlusMinus_norm > 0.354166 and po_PlusMinus_norm <= 0.395834 and rs_PlusMinus_norm > 0.548 and rs_PlusMinus_norm <= 0.556:
			    leafNode = 3
			    wx_sum = 7.1465753249 + DraftAge_norm * 2.2681273438 + (country_group == 'EURO') * 0.0056782221 + (country_group == 'CAN') * 0.332912836  + Weight_norm * 1.5706434401 + CSS_rank_norm * -2.2145122397 + rs_GP_norm * 2.4135766868 + rs_P_norm * 1.5706334136 + rs_PIM_norm * -1.0367303956 + rs_PlusMinus_norm * -10.8803616145 + po_A_norm * -0.9534784316 + po_P_norm * 1.4172451085 + po_PIM_norm * 1.5097963896 + po_PlusMinus_norm * -7.1433895008 
			    lmt_prob = 1/(1 + np.exp(-wx_sum))

			elif po_PlusMinus_norm > 0.354166 and po_PlusMinus_norm <= 0.395834 and rs_PlusMinus_norm > 0.548 and rs_PlusMinus_norm > 0.556:
			    leafNode = 4
			    wx_sum = -1.9780057039 + DraftAge_norm * 2.2681273438 + (country_group == 'EURO') * -0.1901788186 + (country_group == 'CAN') * 0.332912836  + Weight_norm * 1.5706434401 + CSS_rank_norm * -1.4750414248 + rs_GP_norm * 1.8403281774 + rs_P_norm * 1.5706334136 + rs_PIM_norm * -1.0367303956 + rs_PlusMinus_norm * 0.7777586333 + po_P_norm * 4.3659576659 + po_PIM_norm * 5.2983383711 + po_PlusMinus_norm * -7.1433895008 
			    lmt_prob = 1/(1 + np.exp(-wx_sum))

			elif po_PlusMinus_norm > 0.354166 and po_PlusMinus_norm > 0.395834:
			    leafNode = 5
			    wx_sum = -1.1012862109 + DraftAge_norm * 0.7210529086 + Weight_norm * 1.5706434401 + (Position == 'R') * -0.1171557532 + CSS_rank_norm * -1.4750414248 + rs_GP_norm * 1.1639704533 + rs_P_norm * 1.5706334136 + po_P_norm * 1.4172451085 + po_PlusMinus_norm * -7.1433895008 
			    lmt_prob = 1/(1 + np.exp(-wx_sum))



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

    with open(outputDir + "/lmt_1st_cohort_5_year_norm_prob.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(rows_list)
    # moved imported .txt file to another  folder


