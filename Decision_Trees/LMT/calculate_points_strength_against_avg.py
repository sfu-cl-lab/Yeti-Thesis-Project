import csv
import pandas as pd
import numpy as np

df1 = pd.read_csv('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv')
DraftAge_norm_avg = df1['DraftAge_norm'].mean()
Weight_norm_avg = df1['Weight_norm'].mean()
CSS_rank_norm_avg = df1['CSS_rank_norm'].mean()
rs_A_norm_avg = df1['rs_A_norm'].mean()
rs_P_norm_avg = df1['rs_P_norm'].mean()
rs_GP_norm_avg = df1['rs_GP_norm'].mean()
rs_P_norm_avg = df1['rs_P_norm'].mean()
rs_PIM_norm_avg = df1['rs_PIM_norm'].mean()
rs_PlusMinus_norm_avg = df1['rs_PlusMinus_norm'].mean()
po_P_norm_avg = df1['po_P_norm'].mean()
po_PIM_norm_avg = df1['po_PIM_norm'].mean()
po_PlusMinus_norm_avg = df1['po_PlusMinus_norm'].mean()
po_A_norm_avg = df1['po_A_norm'].mean()
country_EURO_avg = df1['country_EURO'].mean()
country_USA_avg = df1['country_USA'].mean()
country_CAN_avg = df1['country_CAN'].mean()
position_R_avg = df1['position_R'].mean()

with open('Desktop/lmt_10years_CSS_null_norm_prob_01_02.csv', 'rwb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    vals = []
    for row in d_reader:
        DraftAge_norm_diff = float(row['DraftAge_norm']) - DraftAge_norm_avg
        Weight_norm_diff = float(row['Weight_norm']) - Weight_norm_avg
        CSS_rank_norm_diff = float(row['CSS_rank_norm']) - CSS_rank_norm_avg
        rs_A_norm_diff = float(row['rs_A_norm']) - rs_A_norm_avg
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg
        country_EURO_diff = float(row['country_EURO']) - country_EURO_avg
        rs_GP_norm_diff = float(row['rs_GP_norm']) - rs_GP_norm_avg
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg
        rs_PIM_norm_diff = float(row['rs_PIM_norm']) - rs_PIM_norm_avg
        rs_PlusMinus_norm_diff = float(row['rs_PlusMinus_norm']) -rs_PlusMinus_norm_avg
        po_A_norm_diff = float(row['po_A_norm']) - po_A_norm_avg
        po_P_norm_diff = float(row['po_P_norm']) - po_P_norm_avg
        po_PIM_norm_diff = float(row['po_PIM_norm']) - po_PIM_norm_avg
        po_PlusMinus_norm_diff = float(row['po_PlusMinus_norm']) - po_PlusMinus_norm_avg
        position_R_diff = float(row['position_R']) - position_R_avg
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

df1.to_csv('Desktop/lmt_attributes_against_avg_01_02.csv')

df2 = pd.read_csv('Desktop/lmt_10years_CSS_null_norm_prob_07_08.csv')
DraftAge_norm_avg = df2['DraftAge_norm'].mean()
Weight_norm_avg = df2['Weight_norm'].mean()
CSS_rank_norm_avg = df2['CSS_rank_norm'].mean()
rs_A_norm_avg = df2['rs_A_norm'].mean()
rs_P_norm_avg = df2['rs_P_norm'].mean()
rs_GP_norm_avg = df2['rs_GP_norm'].mean()
rs_P_norm_avg = df2['rs_P_norm'].mean()
rs_G_norm_avg = df2['rs_G_norm'].mean()
rs_PIM_norm_avg = df2['rs_PIM_norm'].mean()
rs_PlusMinus_norm_avg = df2['rs_PlusMinus_norm'].mean()
po_P_norm_avg = df2['po_P_norm'].mean()
po_PIM_norm_avg = df2['po_PIM_norm'].mean()
po_PlusMinus_norm_avg = df2['po_PlusMinus_norm'].mean()
po_A_norm_avg = df2['po_A_norm'].mean()
po_GP_norm_avg = df2['po_GP_norm'].mean()
Height_norm_avg = df2['Height_norm'].mean()
country_EURO_avg = df2['country_EURO'].mean()
country_USA_avg = df2['country_USA'].mean()
country_CAN_avg = df2['country_CAN'].mean()
position_R_avg = df2['position_R'].mean()
position_D_avg = df2['position_D'].mean()
position_L_avg = df2['position_L'].mean()

with open('Desktop/lmt_10years_CSS_null_norm_prob_07_08.csv', 'rwb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    headers = d_reader.fieldnames
    vals = []
    for row in d_reader:
        DraftAge_norm_diff = float(row['DraftAge_norm']) - DraftAge_norm_avg
        Weight_norm_diff = float(row['Weight_norm']) - Weight_norm_avg
        CSS_rank_norm_diff = float(row['CSS_rank_norm']) - CSS_rank_norm_avg
        rs_A_norm_diff = float(row['rs_A_norm']) - rs_A_norm_avg
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg
        country_EURO_diff = float(row['country_EURO']) - country_EURO_avg
        rs_GP_norm_diff = float(row['rs_GP_norm']) - rs_GP_norm_avg
        rs_P_norm_diff = float(row['rs_P_norm']) - rs_P_norm_avg
        rs_PIM_norm_diff = float(row['rs_PIM_norm']) - rs_PIM_norm_avg
        rs_PlusMinus_norm_diff = float(row['rs_PlusMinus_norm']) -rs_PlusMinus_norm_avg
        rs_G_norm_diff = float(row['rs_G_norm']) - rs_G_norm_avg
        po_A_norm_diff = float(row['po_A_norm']) - po_A_norm_avg
        po_P_norm_diff = float(row['po_P_norm']) - po_P_norm_avg
        po_GP_norm_diff = float(row['po_GP_norm']) - po_GP_norm_avg
        po_PIM_norm_diff = float(row['po_PIM_norm']) - po_PIM_norm_avg
        po_PlusMinus_norm_diff = float(row['po_PlusMinus_norm']) - po_PlusMinus_norm_avg
        position_R_diff = float(row['position_R']) - position_R_avg
        Height_norm_diff = float(row['Height_norm']) - Height_norm_avg
        position_D_diff = float(row['position_D']) - position_D_avg
        position_L_diff = float(row['position_L']) - position_L_avg
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

df2.to_csv('Desktop/lmt_attributes_against_avg_07_08.csv')

frames = [df1, df2]
result = pd.concat(frames)
result.to_csv('Desktop/lmt_attributes_against_avg_01_02_07_08.csv')




