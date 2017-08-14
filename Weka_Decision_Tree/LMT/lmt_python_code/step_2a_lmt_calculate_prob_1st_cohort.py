import csv
import os
import shutil
import time
import numpy as np

# newly crawled betting lines are saved in the inputDir folder
# inputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/leaf_nodes"
inputDir = "/Users/chao/GoogleDrive/2017-08-10-weka-data"
# csv files to be created will be saved in the outputDir folder
#outputDir = "/home/cla315/work_yeti/LMT_leaf_nodes/calculated_data"
outputDir = "/Users/chao/GoogleDrive/2017-08-10-weka-data"
# after data is exacted, .txt files will be moved to the moveToDir folder
#moveToDir = "/home/cla315/work_yeti/LMT_leaf_nodes/old_leaf_nodes"
moveToDir = "/Users/chao/GoogleDrive/2017-08-10-weka-data"

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
                wx_sum = 9.9140255259 + DraftAge_norm * -2.096901655 + (country_group == 'USA') * -0.151551637 + Height_norm * 0.2239516778 + Weight_norm * -1.316244559 + (Position == 'L') * -0.2031332891 + CSS_rank_norm * 1.790480601  + rs_GP_norm * -0.208024884 + rs_G_norm * 0.1544782659 + rs_A_norm * -0.3846712884 + rs_P_norm * -0.2841338093 + rs_PIM_norm * 0.2586378459 + rs_PlusMinus_norm * 0.9946272632 + po_A_norm * -0.8819807998 + po_PIM_norm * -0.4978595316 + po_PlusMinus_norm * 0.5804870983

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif po_PlusMinus_norm > 0.354166 and po_PlusMinus_norm > 0.395834:
                leafNode = 7
                wx_sum = -5.9425373873 + DraftAge_norm * -2.5117625116 + (country_group == 'EURO') * 0.109146088  + (country_group == 'CAN') * -0.2447997468 + (country_group == 'USA') * -0.151551637 + Height_norm * 0.2239516778 + Weight_norm * -2.3184932304 + (Position == 'L') * -0.2031332891 + CSS_rank_norm * 1.790480601  + rs_GP_norm * -1.0974078862 + rs_G_norm * 0.3646981938 + rs_A_norm * -0.8345762083 + rs_P_norm * -1.5507488616 + rs_PIM_norm * 0.739906905  + rs_PlusMinus_norm * -2.2328254555 + po_GP_norm * -0.2283804018 + po_G_norm * -0.9969467363 + po_A_norm * -0.8819807998 + po_P_norm * 0.1255351401 + po_PIM_norm * -0.4978595316 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif 0.354166 < po_PlusMinus_norm <= 0.395834 and rs_PlusMinus_norm <= 0.548:
                leafNode = 2
                wx_sum = -1.4723750665 + DraftAge_norm * -8.4534733423 + (country_group == 'EURO') * 0.109146088  + (country_group == 'CAN') * -0.2447997468 + (country_group == 'USA') * -0.151551637 + Height_norm * 0.2239516778 + Weight_norm * -2.4656945991 + (Position == 'D') * 0.0412522325 + (Position == 'L') * -0.263776591 + (Position == 'R') * -2.7990698279 + CSS_rank_norm * 1.790480601  + rs_GP_norm * -1.3002644567 + rs_G_norm * 0.8120174252 + rs_A_norm * -6.2478163476 + rs_P_norm * -1.5507488616 + rs_PIM_norm * -9.7685950734 + rs_PlusMinus_norm * -2.5684712975 + po_GP_norm * -0.2829463394 + po_G_norm * -0.9969467363 + po_A_norm * -0.3246643415 + po_PIM_norm * -61.1938446115 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif 0.354166 < po_PlusMinus_norm <= 0.395834 and rs_PlusMinus_norm > 0.548 and rs_PlusMinus_norm > 0.556:
                leafNode = 6
                wx_sum = -12.9842793443 + DraftAge_norm * -8.3636359256 + (country_group == 'EURO') * 2.2963642672 + (country_group == 'CAN') * -0.566584054 + (country_group == 'USA') * -0.0261182434 + Height_norm * 0.4342333148 + Weight_norm * -5.046278929 + (Position == 'D') * 0.0412522325 + (Position == 'L') * -0.263776591 + (Position == 'R') * -0.22167611 + CSS_rank_norm * 2.0004307114 + rs_GP_norm * 1.5679568906 + rs_G_norm * -4.4214609635 + rs_A_norm * -1.3318899902 + rs_P_norm * -1.5507488616 + rs_PIM_norm * 1.9433457466 + rs_PlusMinus_norm * 3.5295238073 + po_GP_norm * 0.2441707552 + po_G_norm * -1.4437070144 + po_A_norm * -4.8126661141 + po_P_norm * -0.2248610568 + po_PIM_norm * -21.0783161405 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif 0.354166 < po_PlusMinus_norm <= 0.395834 and 0.548 < rs_PlusMinus_norm <= 0.556 and \
                            rs_GP_norm > 0.438889:
                leafNode = 5
                wx_sum = -23.1356501984 + DraftAge_norm * -2.5650080724 + (country_group == 'EURO') * -0.1009509122 + (country_group == 'CAN') * -0.7244298206 + (country_group == 'USA') * 0.1631874771 + Height_norm * 1.963098352  + Weight_norm * -3.6635357577 + (Position == 'D') * 0.0412522325 + (Position == 'L') * -0.1482324717 + (Position == 'R') * -0.22167611 + CSS_rank_norm * 2.2051156047 + rs_GP_norm * -1.2803487041 + rs_G_norm * 0.9940748821 + rs_A_norm * -0.9502625554 + rs_P_norm * -0.3207480688 + rs_PIM_norm * 2.2477853704 + rs_PlusMinus_norm * 9.5741041366 + po_GP_norm * 0.2419954128 + po_G_norm * -5.1572756924 + po_A_norm * 0.3665478945 + po_P_norm * 0.8026166894 + po_PIM_norm * -1.0468308333 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1 / (1 + np.exp(wx_sum))

            elif 0.354166 < po_PlusMinus_norm <= 0.395834 and 0.548 < rs_PlusMinus_norm <= 0.556 and \
                            rs_GP_norm <= 0.438889 and CSS_rank_norm <= 0.227272:
                leafNode = 3
                wx_sum = -19.6378448757 + DraftAge_norm * -9.1917679858 + (country_group == 'EURO') * 1.1432737682 + (country_group == 'CAN') * -0.566584054 + (country_group == 'USA') * -0.0261182434 + Height_norm * -3.1887469463 + Weight_norm * -3.8744590012 + (Position == 'D') * -0.1372291532 + (Position == 'C') * 1.0771797652 + (Position == 'L') * -0.263776591 + (Position == 'R') * -0.349119543 + CSS_rank_norm * 12.5109506157 + rs_GP_norm * -6.4169458294 + rs_G_norm * 0.9940748821 + rs_A_norm * -13.9405183292 + rs_P_norm * -1.1388478625 + rs_PIM_norm * 8.4989407844 + rs_PlusMinus_norm * 9.5741041366 + po_GP_norm * -11.507445717 + po_G_norm * 2.9462149753 + po_A_norm * 0.0891044711 + po_P_norm * 0.8026166894 + po_PIM_norm * 5.8631618184 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1/(1 + np.exp(wx_sum))

            elif 0.354166 < po_PlusMinus_norm <= 0.395834 and 0.548 < rs_PlusMinus_norm <= 0.556 and \
                            rs_GP_norm <= 0.438889 and CSS_rank_norm > 0.227272:
                leafNode = 4
                wx_sum = -21.513458779 + DraftAge_norm * -1.8349523472 + (country_group == 'EURO') * -0.089887478 + (country_group == 'CAN') * -0.0121378312 + (country_group == 'USA') * -0.0261182434 + Height_norm * 2.5087446973 + Weight_norm * -4.2758232053 + (Position == 'D') * 0.6025874425 + (Position == 'C') * -0.1207237009 + (Position == 'L') * -0.028472116 + (Position == 'R') * -0.349119543 + CSS_rank_norm * 0.1594170035 + rs_GP_norm * -2.0897683523 + rs_G_norm * 0.9940748821 + rs_A_norm * -1.9407434833 + rs_P_norm * -1.1388478625 + rs_PIM_norm * 3.4566513169 + rs_PlusMinus_norm * 9.5741041366 + po_GP_norm * -2.1610257856 + po_G_norm * 5.4593038943 + po_A_norm * 0.0891044711 + po_P_norm * 0.8026166894 + po_PIM_norm * 5.8631618184 + po_PlusMinus_norm * 48.9736141085

                lmt_prob = 1/(1 + np.exp(wx_sum))

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


