import csv
import pandas as pd
import numpy as np

# get the average value with sql "SELECT LeafNode, avg(DraftAge_norm), avg(Weight_norm), avg(CSS_rank_norm), avg(rs_A_norm), avg(rs_GP_norm), avg(rs_P_norm), avg(rs_PIM_norm), avg(rs_PlusMinus_norm), avg(po_P_norm), avg(po_PIM_norm), avg(po_PlusMinus_norm), avg(po_A_norm), avg(country_EURO), avg(country_USA), avg(country_CAN), avg(position_R)  FROM chao_draft.lmt_testYears_CSS_null_norm_prob_for_points where DraftYear in (2001,2002)/(2007,2008) group by LeafNode;"

df1 = pd.read_csv('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv')
DraftAge_norm_avg = [0.042207792207792194, 0.05088062622309201,0.10545556805399334, 0.06395348837209304, 0.10204081632653063]
Weight_norm_avg = [0.4145541958041958, 0.4143835616438356, 0.4140672319806176, 0.39020572450804997, 0.3820970695970695]
CSS_rank_norm_avg = [0.5431709438886473, 0.5189093530838303, 0.5073842444335611, 0.47947034605541355, 0.5593529277739803]
rs_A_norm_avg = [0.19184491978609627, 0.15028203062046727, 0.212289640265555, 0.2045143638850889, 0.20891690009337066]
rs_GP_norm_avg = [0.6603535353535354, 0.5652968036529681, 0.5430446194225723, 0.5740310077519379, 0.6825396825396827]
rs_P_norm_avg = [0.20497698504027628, 0.1596150511531126, 0.2299661118309578, 0.22188695908154255, 0.24035563592525613]
rs_PIM_norm_avg = [0.18898272917062062, 0.14762490348042442, 0.1367432150313153, 0.13191241442928583, 0.17447062332239785]
rs_PlusMinus_norm_avg = [0.566, 0.47331506849315086, 0.5520000000000023, 0.634790697674419, 0.6540952380952382]
po_P_norm_avg = [0.05039525691699606, 0.022036926742108394, 0.07300581992468333, 0.06648129423660265, 0.14906832298136646]
po_PIM_norm_avg = [0.06079545454545455, 0.023972602739726033, 0.05692257217847772, 0.04544573643410852, 0.12539682539682542]
po_PlusMinus_norm_avg = [0.28693181818181823, 0.375, 0.375, 0.375, 0.5674603174603176]
po_A_norm_avg = [0.05506993006993008, 0.02370916754478399, 0.0772259236826166, 0.06663685152057243, 0.16300366300366298]
country_EURO_avg = [0.4091, 0.5342, 0.4291, 0.6163, 0.5714]
country_USA_avg = [0.0682, 0.1370, 0.2402, 0.0814, 0.0238]
country_CAN_avg = [0.5227, 0.3288, 0.3307, 0.3023, 0.4048]
position_R_avg = [0.1818, 0.2329, 0.2126, 0.1047, 0.2143]

with open('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv', 'rb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    vals_positive = []
    vals_negative = []
    DraftAge_norm_diff_list = []
    Weight_norm_diff_list = []
    CSS_rank_norm_diff_list = []
    rs_A_norm_diff_list = []
    rs_P_norm_diff_list = []
    country_EURO_diff_list = []
    rs_GP_norm_diff_list = []
    rs_PIM_norm_diff_list = []
    rs_PlusMinus_norm_diff_list = []
    po_A_norm_diff_list = []
    po_P_norm_diff_list = []
    po_PIM_norm_diff_list = []
    po_PlusMinus_norm_diff_list = []
    position_R_diff_list = []
    country_CAN_diff_list = []
    for row in d_reader:
        DraftAge_norm_diff = float(row['DraftAge_norm']) - DraftAge_norm_avg[int(row['LeafNode'])-1]
        DraftAge_norm_diff_list.append(DraftAge_norm_diff)
        Weight_norm_diff = float(row['Weight_norm']) - Weight_norm_avg[int(row['LeafNode'])-1]
        Weight_norm_diff_list.append(Weight_norm_diff)
        CSS_rank_norm_diff = float(row['CSS_rank_norm']) - CSS_rank_norm_avg[int(row['LeafNode'])-1]
        CSS_rank_norm_diff_list.append(CSS_rank_norm_diff)
        rs_A_norm_diff = float(row['rs_A_norm']) - rs_A_norm_avg[int(row['LeafNode'])-1]
        rs_A_norm_diff_list.append(rs_A_norm_diff)
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg[int(row['LeafNode'])-1]
        rs_P_norm_diff_list.append(rs_P_norm_diff)
        country_EURO_diff = float(row['country_EURO']) - country_EURO_avg[int(row['LeafNode'])-1]
        country_EURO_diff_list.append(country_EURO_diff)
        rs_GP_norm_diff = float(row['rs_GP_norm']) - rs_GP_norm_avg[int(row['LeafNode'])-1]
        rs_GP_norm_diff_list.append(rs_GP_norm_diff)
        rs_PIM_norm_diff = float(row['rs_PIM_norm']) - rs_PIM_norm_avg[int(row['LeafNode'])-1]
        rs_PIM_norm_diff_list.append(rs_PIM_norm_diff)
        rs_PlusMinus_norm_diff = float(row['rs_PlusMinus_norm']) -rs_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        rs_PlusMinus_norm_diff_list.append(rs_PlusMinus_norm_diff)
        po_A_norm_diff = float(row['po_A_norm']) - po_A_norm_avg[int(row['LeafNode'])-1]
        po_A_norm_diff_list.append(po_A_norm_diff)
        po_P_norm_diff = float(row['po_P_norm']) - po_P_norm_avg[int(row['LeafNode'])-1]
        po_P_norm_diff_list.append(po_P_norm_diff)
        po_PIM_norm_diff = float(row['po_PIM_norm']) - po_PIM_norm_avg[int(row['LeafNode'])-1]
        po_PIM_norm_diff_list.append(po_PIM_norm_diff)
        po_PlusMinus_norm_diff = float(row['po_PlusMinus_norm']) - po_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        po_PlusMinus_norm_diff_list.append(po_PlusMinus_norm_diff)
        position_R_diff = float(row['position_R']) - position_R_avg[int(row['LeafNode'])-1]
        position_R_diff_list.append(position_R_diff)
        country_CAN_diff = float(row['country_CAN']) - country_CAN_avg[int(row['LeafNode'])-1]
        country_CAN_diff_list.append(country_CAN_diff)
        if int(row['LeafNode']) == 1:
            val_neg = CSS_rank_norm_diff *-1.256756345 + rs_A_norm_diff * -1.3622035894
            val_pos = DraftAge_norm_diff* 1.5253614015 + Weight_norm_diff * 1.4919620265 + rs_P_norm_diff * 1.5706334136             
        elif int(row['LeafNode']) == 2:
            val_neg = country_EURO_diff *-0.1901788186 + CSS_rank_norm_diff * -1.4750414248 + po_PlusMinus_norm_diff * -7.1433895008
            val_pos = DraftAge_norm_diff * 2.2681273438 + Weight_norm_diff *1.5706434401 + rs_GP_norm_diff *1.1639704533 + rs_P_norm_diff * 1.5706334136 + rs_PlusMinus_norm_diff * 1.8081514932 + po_P_norm_diff * 1.4172451085 + po_PIM_norm_diff *22.3783855159
        elif int(row['LeafNode']) == 3:
            val_neg = CSS_rank_norm_diff * -2.2145122397 + rs_PIM_norm_diff * -1.0367303956 + rs_PlusMinus_norm_diff * -10.8803616145 + po_A_norm_diff * -0.9534784316 + po_PlusMinus_norm_diff * -7.1433895008
            val_pos = DraftAge_norm_diff * 2.2681273438 + country_EURO_diff * 0.0056782221 + country_CAN_diff * 0.332912836 + Weight_norm_diff * 1.5706434401 + rs_GP_norm_diff * 2.4135766868 + rs_P_norm_diff * 1.5706334136 + po_P_norm_diff * 1.4172451085 + po_PIM_norm_diff * 1.5097963896
        elif int(row['LeafNode']) == 4:
            val_neg = country_EURO_diff * -0.1901788186 + CSS_rank_norm_diff * -1.4750414248 + rs_PIM_norm_diff * -1.0367303956 + po_PlusMinus_norm_diff * -7.1433895008
            val_pos = DraftAge_norm_diff * 2.2681273438 + country_CAN_diff * 0.332912836 + Weight_norm_diff * 1.5706434401 + rs_GP_norm_diff * 1.8403281774 + rs_P_norm_diff * 1.5706334136 + rs_PlusMinus_norm_diff * 0.7777586333 + po_P_norm_diff * 4.3659576659 + po_PIM_norm_diff * 5.2983383711
        elif int(row['LeafNode']) == 5:
            val_neg = position_R_diff * -0.1171557532 + CSS_rank_norm_diff * -1.4750414248 + po_PlusMinus_norm_diff * -7.1433895008
            val_pos = DraftAge_norm_diff * 0.7210529086 + Weight_norm_diff * 1.5706434401 + rs_GP_norm_diff * 1.1639704533 + rs_P_norm_diff * 1.5706334136 + po_P_norm_diff * 1.4172451085 
        vals_positive.append(val_pos)
        vals_negative.append(val_neg)

with open('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv', 'rb') as input, open('Desktop/output_lmt_points_01_02_pos_neg_points_with_diff.csv', 'wb') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    row = next(reader)  # read title line
    row.append('weight_pos_val')
    row.append('weight_neg_val')
    row.append('DraftAge_norm_diff')
    row.append('Weight_norm_diff')
    row.append('CSS_rank_norm_diff')
    row.append('rs_A_norm_diff')
    row.append('rs_P_norm_diff')
    row.append('country_EURO_diff')
    row.append('rs_GP_norm_diff')
    row.append('rs_PIM_norm_diff')
    row.append('rs_PlusMinus_norm_diff')
    row.append('po_A_norm_diff')
    row.append('po_P_norm_diff')
    row.append('po_PIM_norm_diff')
    row.append('po_PlusMinus_norm_diff')
    row.append('position_R_diff')
    row.append('country_CAN_diff')
    writer.writerow(row)  # write enhanced title line

    it_pos = vals_positive.__iter__()  # create an iterator on the result
    it_neg = vals_negative.__iter__()
    it_1 = DraftAge_norm_diff_list.__iter__()
    it_2 = Weight_norm_diff_list.__iter__()
    it_3 = CSS_rank_norm_diff_list.__iter__()
    it_4 = rs_A_norm_diff_list.__iter__()
    it_5= rs_P_norm_diff_list.__iter__()
    it_6 = country_EURO_diff_list.__iter__()
    it_7 = rs_GP_norm_diff_list.__iter__()
    it_9 = rs_PIM_norm_diff_list.__iter__()
    it_10 = rs_PlusMinus_norm_diff_list.__iter__()
    it_11 = po_A_norm_diff_list.__iter__()
    it_12 = po_P_norm_diff_list.__iter__()
    it_13 = po_PIM_norm_diff_list.__iter__()
    it_14 = po_PlusMinus_norm_diff_list.__iter__()
    it_15 = position_R_diff_list.__iter__()
    it_16 = country_CAN_diff_list.__iter__()
    
    for row in reader:
        if row:  # avoid empty lines that usually lurk undetected at the end of the files
            try:
                row.append(next(it_pos))  # add a result to current row
                row.append(next(it_neg))
                row.append(next(it_1))
                row.append(next(it_2))
                row.append(next(it_3))
                row.append(next(it_4))
                row.append(next(it_5))
                row.append(next(it_6))
                row.append(next(it_7))
                row.append(next(it_9))
                row.append(next(it_10))
                row.append(next(it_11))
                row.append(next(it_12))
                row.append(next(it_13))
                row.append(next(it_14))
                row.append(next(it_15))
                row.append(next(it_16))
            except StopIteration:
                row.append("N/A")     # not enough results: pad with N/A
            writer.writerow(row)




