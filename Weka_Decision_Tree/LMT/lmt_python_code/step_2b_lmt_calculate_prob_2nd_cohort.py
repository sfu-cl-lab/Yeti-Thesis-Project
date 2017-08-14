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
                wx_sum = 3.8010334235 + DraftAge_norm * -0.7752412071 + (country_group == 'EURO') * 0.3877915448 + (country_group == 'USA') * -0.0223408917 + (country_group == 'CAN') * -3.5644521366 + Height_norm * -0.0779159498 + Weight_norm * -4.5234693342 + (Position == 'L') * -0.6490666463 + (Position == 'D') * 0.4454671351 + (Position == 'C') * -0.37479603 + (Position == 'R') * 0.2175504444 + CSS_rank_norm * 34.2074038871 + rs_GP_norm * 1.6182802395 + rs_G_norm * -5.9075925827 + rs_A_norm * -1.0772889254 + rs_P_norm * -2.6085715759 + rs_PIM_norm * -4.6718283846 + rs_PlusMinus_norm * 5.7605495357 + po_GP_norm * -1.7870363582 + po_G_norm * 1.7979103301 + po_A_norm * -9.2216831113 + po_PIM_norm * 5.3911904995 + po_PlusMinus_norm * -13.2220438811

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm <= 0.061171:
                leafNode = 2
                wx_sum = -0.7725165442 + DraftAge_norm * 0.816992601  + (country_group == 'EURO') * 0.3633552461 + (country_group == 'USA') * 0.2510391159 + Height_norm * 2.0353551886 + Weight_norm * -2.514560879 + (Position == 'L') * 0.1935070643 + (Position == 'D') * 0.1663314879 + (Position == 'C') * -0.7056949337 + (Position == 'R') * -0.9613782344 + CSS_rank_norm * 1.9205062878 + rs_GP_norm * -2.3366864286 + rs_G_norm * 0.2361661828 + rs_A_norm * -0.858771945 + rs_P_norm * -8.6065214609 + rs_PIM_norm * 1.0370793568 + rs_PlusMinus_norm * -0.9341059546 + po_GP_norm * 5.5292253703 + po_G_norm * 5.4567465398 + po_A_norm * -11.484574548 + po_PIM_norm * -2.2369755328 + po_PlusMinus_norm * 6.976025739

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm <= 0.362385 and \
                            rs_PlusMinus_norm <= 0.353211:
                leafNode = 3
                wx_sum = 0.7533496812 + DraftAge_norm * -0.6004314173 + (country_group == 'EURO') * 1.9006579282 + (country_group == 'USA') * -1.3248376675 + (country_group == 'CAN') * 0.012789531  + Height_norm * 3.9487047678 + Weight_norm * -3.6611475798 + (Position == 'L') * -0.6468692773 + (Position == 'D') * -0.098866021 + (Position == 'C') * 0.1407968664 + (Position == 'R') * 0.1914750802 + CSS_rank_norm * 2.6187990626 + rs_GP_norm * -2.4514081182 + rs_G_norm * 0.432691425  + rs_A_norm * -1.4974545718 + rs_P_norm * 1.1664802867 + rs_PIM_norm * 1.4231146279 + rs_PlusMinus_norm * -5.5570655327 + po_GP_norm * 0.3165275229 + po_G_norm * 0.2815983075 + po_A_norm * 1.7836587136 + po_P_norm * 1.6841012034 + po_PIM_norm * -1.6716917974 + po_PlusMinus_norm * 2.3883158709

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm <= 0.362385 and \
                            rs_PlusMinus_norm > 0.353211:
                leafNode = 4
                wx_sum = -1.1505331087 + DraftAge_norm * -1.8353947973 + (country_group == 'EURO') * -0.3944399825 + (country_group == 'USA') * 0.1501179562 + (country_group == 'CAN') * 0.012789531  + Height_norm * 2.6371897201 + Weight_norm * -0.2330511806 + (Position == 'L') * 0.1226314598 + (Position == 'D') * -0.0247945064 + (Position == 'C') * -0.1396264259 + (Position == 'R') * 0.0270910465 + CSS_rank_norm * 1.6329149455 + rs_GP_norm * -1.913968068 + rs_G_norm * 0.2647649791 + rs_A_norm * -0.0194169356 + rs_P_norm * 1.7236691177 + rs_PIM_norm * 1.5338563807 + rs_PlusMinus_norm * -4.7260515563 + po_GP_norm * 1.7916006591 + po_G_norm * -0.5178963891 + po_A_norm * -0.6122034374 + po_P_norm * -1.2493600896 + po_PIM_norm * -1.3876412109 + po_PlusMinus_norm * 3.1191291424

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif CSS_rank_norm > 0.046371 and rs_P_norm > 0.061171 and rs_PlusMinus_norm > 0.362385:
                leafNode = 5
                wx_sum = 2.188353218 + DraftAge_norm * 1.9396022487 + (country_group == 'EURO') * 0.9377255384 + (country_group == 'USA') * -0.0244360728 + (country_group == 'CAN') * -0.1213982503 + Height_norm * -0.0605153269 + Weight_norm * -1.8120062557 + (Position == 'L') * 0.1196896547 + (Position == 'D') * -0.4129535679 + (Position == 'C') * 0.1519311343 + (Position == 'R') * 0.0779365585 + CSS_rank_norm * -0.0062954048 + rs_GP_norm * -0.932566085 + rs_G_norm * -2.0375877655 + rs_A_norm * -0.6474451594 + rs_P_norm * 0.8157485088 + rs_PIM_norm * 1.2256419957 + rs_PlusMinus_norm * 0.2299693574 + po_GP_norm * 0.2432439667 + po_G_norm * 0.6992716565 + po_A_norm * -1.9627179943 + po_PIM_norm * -2.6740489483 + po_PlusMinus_norm * -0.2538421761

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


