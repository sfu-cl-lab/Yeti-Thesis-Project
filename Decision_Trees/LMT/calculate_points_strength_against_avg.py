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

with open('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv', 'rwb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    vals = []
    for row in d_reader:
        DraftAge_norm_diff = float(row['DraftAge_norm']) - DraftAge_norm_avg[int(row['LeafNode'])-1]
        Weight_norm_diff = float(row['Weight_norm']) - Weight_norm_avg[int(row['LeafNode'])-1]
        CSS_rank_norm_diff = float(row['CSS_rank_norm']) - CSS_rank_norm_avg[int(row['LeafNode'])-1]
        rs_A_norm_diff = float(row['rs_A_norm']) - rs_A_norm_avg[int(row['LeafNode'])-1]
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg[int(row['LeafNode'])-1]
        country_EURO_diff = float(row['country_EURO']) - country_EURO_avg[int(row['LeafNode'])-1]
        rs_GP_norm_diff = float(row['rs_GP_norm']) - rs_GP_norm_avg[int(row['LeafNode'])-1]
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg[int(row['LeafNode'])-1]
        rs_PIM_norm_diff = float(row['rs_PIM_norm']) - rs_PIM_norm_avg[int(row['LeafNode'])-1]
        rs_PlusMinus_norm_diff = float(row['rs_PlusMinus_norm']) -rs_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        po_A_norm_diff = float(row['po_A_norm']) - po_A_norm_avg[int(row['LeafNode'])-1]
        po_P_norm_diff = float(row['po_P_norm']) - po_P_norm_avg[int(row['LeafNode'])-1]
        po_PIM_norm_diff = float(row['po_PIM_norm']) - po_PIM_norm_avg[int(row['LeafNode'])-1]
        po_PlusMinus_norm_diff = float(row['po_PlusMinus_norm']) - po_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        position_R_diff = float(row['position_R']) - position_R_avg[int(row['LeafNode'])-1]
        if row['LeafNode'] == 1:
            val = 3.0996183241 + DraftAge_norm_diff* -1.5253614015 + Weight_norm_diff * -1.4919620265 + CSS_rank_norm_diff *1.256756345 + rs_A_norm_diff * 1.3622035894 + rs_P_norm_diff * -1.5706334136
        elif row['LeafNode'] == 2:
            val = 2.3823397672 + DraftAge_norm_diff * -2.2681273438 + country_EURO_diff *0.1901788186 + Weight_norm_diff *-1.5706434401 + CSS_rank_norm_diff * 1.4750414248 + rs_GP_norm_diff *-1.1639704533 + rs_P_norm_diff * -1.5706334136 + rs_PlusMinus_norm_diff * -1.8081514932 + po_P_norm_diff * -1.4172451085 + po_PIM_norm_diff *-22.3783855159 + po_PlusMinus_norm_diff * 7.1433895008
        elif row['LeafNode'] == 3:
            val = -7.1465753249 + DraftAge_norm_diff * -2.2681273438 + country_EURO_diff * -0.0056782221 + country_CAN_diff * -0.332912836 + Weight_norm_diff * -1.5706434401 + CSS_rank_norm_diff * 2.2145122397 + rs_GP_norm_diff * -2.4135766868 + rs_P_norm_diff * -1.5706334136 + rs_PIM_norm_diff * 1.0367303956 + rs_PlusMinus_norm_diff * 10.8803616145 + po_A_norm_diff * 0.9534784316 + po_P_norm_diff * -1.4172451085 + po_PIM_norm_diff * -1.5097963896 + po_PlusMinus_norm_diff * 7.1433895008
        elif row['LeafNode'] == 4:
            val = 1.9780057039 + DraftAge_norm_diff * -2.2681273438 + country_EURO_diff * 0.1901788186 + country_CAN_diff * -0.332912836 + Weight_norm_diff * -1.5706434401 + CSS_rank_norm_diff * 1.4750414248 + rs_GP_norm_diff * -1.8403281774 + rs_P_norm_diff * -1.5706334136 + rs_PIM_norm_diff * 1.0367303956 + rs_PlusMinus_norm_diff * -0.7777586333 + po_P_norm_diff * -4.3659576659 + po_PIM_norm_diff * -5.2983383711 + po_PlusMinus_norm_diff * 7.1433895008
        else:
            val = 1.1012862109 + DraftAge_norm_diff * -0.7210529086 + Weight_norm_diff * -1.5706434401 + position_R_diff * 0.1171557532 + CSS_rank_norm_diff * 1.4750414248 + rs_GP_norm_diff * -1.1639704533 + rs_P_norm_diff * -1.5706334136 + po_P_norm_diff * -1.4172451085 + po_PlusMinus_norm_diff * 7.1433895008
        
        vals.append(val)
    df1['points'] = pd.Series(np.random.randn(len(df1['DraftAge_norm'])), index=df1.index)

df1.to_csv('Desktop/lmt_attributes_against_avg_01_02.csv', encoding='utf-8')

df2 = pd.read_csv('Desktop/lmt_10years_CSS_null_norm_prob_07_08.csv')
DraftAge_norm_avg = [0.033096926713948, 0.043478260869565216, 0.051051051051051066, 0.08653846153846147, 0.04569892473118278, 0.11111111111111112]
Weight_norm_avg = [0.46071202864967375, 0.4619027120103317, 0.43403799839443397, 0.4305026656511804, 0.4408335994889812,0.4435643564356436]
CSS_rank_norm_avg = [0.02179135209334248, 0.7012622720897614, 0.5062663469921534, 0.5087624069478907, 0.409176638917794, 0.5266129032258065]
rs_A_norm_avg = [0.2916827852998066, 0.041106719367588924, 0.2308353808353808, 0.25480769230769235, 0.26370967741935497, 0.43090909090909085]
rs_P_norm_avg = [0.28802625622453604, 0.03399629972247919, 0.22232604945370898, 0.251943535188216, 0.2510724090597117, 0.375531914893617]
rs_GP_norm_avg = [0.5553191489361703, 0.4043478260869566, 0.6372972972972974, 0.463076923076923,0.6346774193548387, 0.67]
rs_G_norm_avg = [0.2828696126568466, 0.03623188405797101, 0.204088704088704, 0.2480276134122287, 0.23325062034739463, 0.29743589743589743]
rs_PIM_norm_avg = [0.21537125488493275, 0.12658976634131913, 0.26112336826622534, 0.1817765567765567, 0.22939982444590737, 0.21904761904761907]
rs_PlusMinus_norm_avg = [0.4263127073980092, 0.3310729956122856, 0.26270766179023064, 0.35779816513761553, 0.4702574726250369, 0.5688073394495413]
po_P_norm_avg = [0.16188714153561518, 0.021739130434782605, 0.06022326674500589, 0.09824414715719063, 0.10483870967741934, 0.4782608695652174]
po_PIM_norm_avg = [0.13235294117647056, 0.0588235294117647, 0.05007949125596183, 0.09968891402714929, 0.12737191650853882, 0.29411764705882354]
po_PlusMinus_norm_avg = [0.3154805575935436, 0.30884557721139444, 0.27912395153774466, 0.309018567639257, 0.3145161290322579, 0.5931034482758621]
po_A_norm_avg = [0.14680851063829783, 0.02318840579710145, 0.05855855855855854, 0.09198717948717947, 0.10026881720430098, 0.5133333333333333]
po_GP_norm_avg = [0.26559060895084374, 0.1904047976011994, 0.14725069897483686, 0.18965517241379315, 0.264460511679644, 0.6620689655172415]
Height_norm_avg = [0.5784574468085106, 0.6086956521739131, 0.5717905405405406, 0.5612980769230769, 0.5594758064516129, 0.4875]
country_EURO_avg = [0.5106, 0.1304, 0.1486, 0.2404, 0.1371, 0.2000]
country_USA_avg = [0.1489, 0.3043, 0.1757, 0.4135, 0.2661, 0]
country_CAN_avg = [0.3404, 0.5652, 0.6757, 0.3462, 0.5968, 0.8]
position_R_avg = [0.1915, 0.1739, 0.1216, 0.1346, 0.1613, 0.2]
position_D_avg = [0.3617, 0.6087, 0.3243, 0.3558, 0.3468, 0.4]
position_L_avg = [0.1702, 0.1304, 0.1216, 0.2212, 0.1452, 0.2]

with open('Desktop/lmt_10years_CSS_null_norm_prob_07_08.csv', 'rwb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    vals = []
    for row in d_reader:
        DraftAge_norm_diff = float(row['DraftAge_norm']) - DraftAge_norm_avg[int(row['LeafNode'])-1]
        Weight_norm_diff = float(row['Weight_norm']) - Weight_norm_avg[int(row['LeafNode'])-1]
        CSS_rank_norm_diff = float(row['CSS_rank_norm']) - CSS_rank_norm_avg[int(row['LeafNode'])-1]
        rs_A_norm_diff = float(row['rs_A_norm']) - rs_A_norm_avg[int(row['LeafNode'])-1]
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg[int(row['LeafNode'])-1]
        country_EURO_diff = float(row['country_EURO']) - country_EURO_avg[int(row['LeafNode'])-1]
        rs_GP_norm_diff = float(row['rs_GP_norm']) - rs_GP_norm_avg[int(row['LeafNode'])-1]
        rs_PIM_norm_diff = float(row['rs_PIM_norm']) - rs_PIM_norm_avg[int(row['LeafNode'])-1]
        rs_PlusMinus_norm_diff = float(row['rs_PlusMinus_norm']) -rs_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        rs_G_norm_diff = float(row['rs_G_norm']) - rs_G_norm_avg[int(row['LeafNode'])-1]
        po_A_norm_diff = float(row['po_A_norm']) - po_A_norm_avg[int(row['LeafNode'])-1]
        po_P_norm_diff = float(row['po_P_norm']) - po_P_norm_avg[int(row['LeafNode'])-1]
        po_GP_norm_diff = float(row['po_GP_norm']) - po_GP_norm_avg[int(row['LeafNode'])-1]
        po_PIM_norm_diff = float(row['po_PIM_norm']) - po_PIM_norm_avg[int(row['LeafNode'])-1]
        po_PlusMinus_norm_diff = float(row['po_PlusMinus_norm']) - po_PlusMinus_norm_avg[int(row['LeafNode'])-1]
        position_R_diff = float(row['position_R']) - position_R_avg[int(row['LeafNode'])-1]
        Height_norm_diff = float(row['Height_norm']) - Height_norm_avg[int(row['LeafNode'])-1]
        position_D_diff = float(row['position_D']) - position_D_avg[int(row['LeafNode'])-1]
        position_L_diff = float(row['position_L']) - position_L_avg[int(row['LeafNode'])-1]
        country_USA_diff = float(row['country_USA']) - country_USA_avg[int(row['LeafNode'])-1]
        if row['LeafNode'] == 1:
            val = 1.682576219  + DraftAge_norm_diff * -0.6521969619 + country_EURO_diff * 0.2515058744 + country_CAN_diff * -0.7372739476 + Height_norm_diff * 0.9108602568 + Weight_norm_diff * -3.0647516341 + position_D_diff * 0.3626622956 + CSS_rank_norm_diff * 19.0327179101 + rs_A_norm_diff * -1.416228717 + rs_P_norm_diff * -2.5182072847 + po_A_norm_diff * -2.5818151743 + po_PlusMinus_norm_diff * -4.5578802919
        elif row['LeafNode'] == 2:
            val = 0.0225110366 + DraftAge_norm_diff * -0.6521969619 + country_EURO_diff * 0.3823693577 + country_USA_diff * 0.2452964509 + Height_norm_diff * 1.6148625242 + Weight_norm_diff * -1.1902369165 + position_D_diff * 0.2475813803 + position_R_diff * -0.6514414089 + CSS_rank_norm_diff * 1.7003217418 + rs_GP_norm_diff * -0.623606065 + rs_G_norm_diff * 0.4156266673 + rs_A_norm_diff * -1.416228717 + rs_P_norm_diff * -9.2361288366 + rs_PIM_norm_diff * 0.4704279537 + rs_PlusMinus_norm_diff * 0.516339445  + po_GP_norm_diff * 0.6961231358 + po_PIM_norm_diff * -0.7606931178
        elif row['LeafNode'] == 3:
            val = 0.2596899624 + DraftAge_norm_diff * -1.2673609724 + country_EURO_diff * 1.2307595534 + country_USA_diff * -0.8069462064 + Height_norm_diff * 2.2083451086 + Weight_norm_diff * -2.1613141404 + position_D_diff * -0.105873252 + position_L_diff * -0.4271360663 + CSS_rank_norm_diff * 1.9138640157 + rs_GP_norm_diff * -1.5673201838 + rs_G_norm_diff * 0.4156266673 + rs_A_norm_diff * -0.4239688038 + rs_PIM_norm_diff * 0.8031514348 + rs_PlusMinus_norm_diff * -2.9754056872 + po_P_norm_diff * 2.6843997425 + po_PIM_norm_diff * -0.7606931178 + po_PlusMinus_norm_diff * 2.447755103
        elif row['LeafNode'] == 4:
            val = -1.0888160283 + DraftAge_norm_diff * -1.2673609724 + country_EURO_diff * -0.463850402 + Height_norm_diff * 2.2083451086 + Weight_norm_diff * -0.2293666258 + position_D_diff * -0.105873252 + position_L_diff * 0.0688557505 + CSS_rank_norm_diff * 1.4879418811 + rs_GP_norm_diff * -1.0477475885 + rs_G_norm_diff * 0.4156266673 + rs_A_norm_diff * -0.4239688038 + rs_P_norm_diff * 0.5796943481 + rs_PIM_norm_diff * 0.8031514348 + rs_PlusMinus_norm_diff * -2.9754056872 + po_P_norm_diff * 0.2898101074 + po_PIM_norm_diff * -0.7606931178 + po_PlusMinus_norm_diff * 2.447755103
        elif row['LeafNode'] == 5:
            val = 1.5482744147 + DraftAge_norm_diff * 1.1198806299 + country_EURO_diff * 0.9510946135 + Height_norm_diff * -0.1943101707 + Weight_norm_diff * -1.1902369165 + position_D_diff * -0.310508047 + position_R_diff * -0.1937918628 + position_L_diff * -0.1239741776 + CSS_rank_norm_diff * 0.3503937449 + rs_GP_norm_diff * -1.0504894229 + rs_G_norm_diff * -0.1686151641 + rs_A_norm_diff * -0.4239688038 + rs_P_norm_diff * -0.5370008872 + rs_PIM_norm_diff * 0.8031514348 + rs_PlusMinus_norm_diff * 0.8075548697 + po_GP_norm_diff * -0.3212562576 + po_PIM_norm_diff * -1.4663079409
        else:
            val = -3.106876138 + DraftAge_norm_diff * -0.0975778883 + country_EURO_diff * 8.8551596038 + Height_norm_diff * 0.6618192176 + Weight_norm_diff * -1.1902369165 + position_D_diff * -0.105873252 + position_L_diff * -0.1239741776 + CSS_rank_norm_diff * 0.3503937449 + rs_GP_norm_diff * -1.0504894229 + rs_G_norm_diff * 0.4156266673 + rs_A_norm_diff * -0.4239688038 + rs_PIM_norm_diff * 0.8031514348 + rs_PlusMinus_norm_diff * 0.8075548697 + po_GP_norm_diff * -1.089093825 + po_PIM_norm_diff * -1.4663079409
        vals.append(val)
    df2['points'] = pd.Series(np.random.randn(len(df2['DraftAge_norm'])), index=df2.index)

df2.to_csv('Desktop/lmt_attributes_against_avg_07_08.csv', encoding='utf-8')

csv1 = pd.read_csv('Desktop/lmt_attributes_against_avg_01_02.csv')
csv2 = pd.read_csv('Desktop/lmt_attributes_against_avg_07_08.csv')
frames = [csv1, csv2]
result = pd.concat(frames)
result.to_csv('Desktop/lmt_attributes_against_avg_01_02_07_08.csv', encoding='utf-8')










