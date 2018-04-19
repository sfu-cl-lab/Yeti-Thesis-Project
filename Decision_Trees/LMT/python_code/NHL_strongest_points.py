import csv
import pandas as pd
import numpy as np

weights_DraftAge = [0.6521969619, 0.6521969619, 1.2673609724, 1.2673609724, -1.1198806299, 0.0975778883]
weights_Weight = [3.0647516341, 1.1902369165, 2.1613141404, 0.2293666258, 1.1902369165, 1.1902369165]
weights_CSS_rank = [-19.0327179101, -1.7003217418, -1.9138640157, -1.4879418811, -0.3503937449, -0.3503937449]
weights_rs_A = [1.416228717, 1.416228717, 0.4239688038, 0.4239688038, 0.4239688038, 0.4239688038]
weights_rs_P = [2.5182072847, 9.2361288366, 0, -0.5796943481, 0.5370008872, 0]
weights_country_EURO = [-0.2515058744, -0.3823693577, -1.2307595534, 0.463850402, -0.9510946135, -8.8551596038]
weights_country_USA = [0, -0.2452964509, 0.8069462064, 0, 0, 0]
weights_country_CAN = [0.7372739476, 0, 0, 0, 0, 0]
weights_rs_GP = [0, 0.623606065, 1.5673201838, 1.0477475885, 1.0504894229, 1.0504894229]
weights_rs_PIM = [0, -0.4704279537, -0.8031514348, -0.8031514348, -0.8031514348, -0.8031514348]
weights_rs_PlusMinus = [0, -0.516339445, 2.9754056872, 2.9754056872, -0.8075548697, -0.8075548697]
weights_rs_G = [0, -0.4156266673, -0.4156266673, -0.4156266673, 0.1686151641, -0.4156266673]
weights_po_A = [2.5818151743, 0, 0, 0, 0, 0]
weights_po_P = [0, 0, -2.6843997425, -0.2898101074, 0, 0]
weights_po_GP = [0, -0.6961231358, 0, 0, 0.3212562576, 1.089093825]
weights_po_PIM = [0, 0.7606931178, 0.7606931178, 0.7606931178, 1.4663079409, 1.4663079409]
weights_po_PlusMinus = [4.5578802919 , 0, -2.447755103, -2.447755103, 0, 0]
weights_position_R = [0, 0.6514414089, 0, 0, 0.1937918628, 0]
weights_Height = [-0.9108602568, -1.6148625242, -2.2083451086, -2.2083451086, 0.1943101707, -0.6618192176]
weights_position_D = [-0.3626622956, -0.2475813803, 0.105873252, 0.105873252, 0.310508047, 0.105873252]
weights_position_L = [0, 0, 0.4271360663, -0.0688557505, 0.1239741776, 0.1239741776]

DraftAge_overall = 0.05717653993516049
Weight_overall = 0.4404496152533025
CSS_rank_overall = 0.4267883117994354
rs_A_overall = 0.24692548830479852
rs_P_overall = 0.2386844630058129
country_EURO_overall = 0.2149
country_USA_overall = 0.2732
country_CAN_overall = 0.5119
rs_GP_overall = 0.5643766578249338
rs_PIM_overall = 0.2143308251682636
rs_PlusMinus_overall = 0.3858321368602912
rs_G_overall = 0.22662041760185014
po_A_overall = 0.09637488947833789
po_P_overall = 0.10125706377580442
po_GP_overall = 0.22171407664867832
po_PIM_overall = 0.10321422998907787
po_PlusMinus_overall = 0.3095216317570655
position_R_overall = 0.1512
Height_overall = 0.5668103448275862
position_D_overall = 0.3634
position_L_overall = 0.1645


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

DraftAge_avg = [18.2979, 18.3913, 18.4595, 18.7788, 18.4113, 19.0000]
Weight_avg = [200.5319, 200.6522, 197.8378, 197.4808, 198.5242, 198.8000]
CSS_rank_avg = [6.4043, 107.0000, 71.3333, 77.7838, 72.6019, 102.2500]
rs_A_avg = [32.0851, 4.5217, 25.3919, 28.0288, 29.0081, 47.4000]
rs_P_avg = [54.1489, 6.3913, 41.7973, 47.3654, 47.2016, 70.6000]
rs_GP_avg = [55.5319, 40.4348, 63.7297, 46.3077, 63.4677, 67.0000]
rs_G_avg = [22.0638, 2.8261, 15.9189, 19.3462, 18.1935, 23.2000]
rs_PIM_avg = [63.3191, 37.2174, 76.7703, 53.4423, 67.4435, 64.4000]
rs_PlusMinus_avg = [7.4681, -2.9130, -10.3649, 0.0000, 12.2581, 23.0000]
po_P_avg = [8.7500, 1.7692, 4.4565, 8.8679, 5.9800, 22.0000]
po_PIM_avg = [10.5750, 7.0769, 5.4783, 13.3019, 10.7400, 20.0000]
po_PlusMinus_avg = [0.1750, -0.0769, -1.4565, -0.0755, 0.1500, 8.200]
po_A_avg = [5.1750, 1.2308, 2.8261, 5.4151, 3.7300, 15.4000]
po_GP_avg = [9.0500, 9.7692, 6.8696, 10.7925, 9.5100, 19.2000]
Height_avg = [73.2553, 73.7391, 73.1486, 72.9808, 72.9516, 71.8000]

DraftAge = 18.5146
Weight = 198.4854
CSS_rank = 64.8316
rs_A = 27.1618
rs_P = 44.8727
rs_GP = 56.4377
rs_PIM = 63.0133
rs_PlusMinus = 3.0557
rs_G = 17.6764
po_A = 4.2412
po_P = 6.8327
po_GP = 9.4319
po_PIM = 10.2957
po_PlusMinus = -0.0350
Height = 73.0690

with open('Desktop/FID_input_07_08.csv', 'rb') as input, open('Desktop/FID_output_07_08.csv', 'wb') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')
    
    row = next(reader)  # read title line
    row.append('Weight')
    row.append('avg_cluster_normalized')
    row.append('avg_overall_normalized')
    row.append('avg_cluster_original')
    row.append('avg_overall_original')
    writer.writerow(row) 
    
    for row in reader:
        print row[0]
        if row[0] == 'DraftAge':
            row.append(weights_DraftAge[int(row[1]) - 1])
            row.append(DraftAge_norm_avg[int(row[1]) -1])
            row.append(DraftAge_overall)
            row.append(DraftAge_avg[int(row[1]) -1])
            row.append(DraftAge)
        elif row[0] == 'Weight':
            row.append(weights_Weight[int(row[1]) - 1])
            row.append(Weight_norm_avg[int(row[1]) -1])
            row.append(Weight_overall)
            row.append(Weight_avg[int(row[1]) -1])
            row.append(Weight)
        elif row[0] == 'CSS_rank':
            row.append(weights_CSS_rank[int(row[1]) - 1])
            row.append(CSS_rank_norm_avg[int(row[1]) -1])
            row.append(CSS_rank_overall)
            row.append(CSS_rank_avg[int(row[1]) -1])
            row.append(CSS_rank)
        elif row[0] == 'rs_A':
            row.append(weights_rs_A[int(row[1]) - 1])
            row.append(rs_A_norm_avg[int(row[1]) -1])
            row.append(rs_A_overall)
            row.append(rs_A_avg[int(row[1]) -1])
            row.append(rs_A)
        elif row[0] == 'rs_P':
            row.append(weights_rs_P[int(row[1]) - 1])
            row.append(rs_P_norm_avg[int(row[1]) -1])
            row.append(rs_P_overall)
            row.append(rs_P_avg[int(row[1]) -1])
            row.append(rs_P)
        elif row[0] == 'country_EURO':
            row.append(weights_country_EURO[int(row[1]) - 1])
            row.append(country_EURO_avg[int(row[1]) -1])
            row.append(country_EURO_overall)
            row.append(country_EURO_avg[int(row[1]) -1])
            row.append(country_EURO_overall)
        elif row[0] == 'country_USA':
            row.append(weights_country_USA[int(row[1]) - 1])
            row.append(country_USA_avg[int(row[1]) -1])
            row.append(country_USA_overall)
            row.append(country_USA_avg[int(row[1]) -1])
            row.append(country_USA_overall)
        elif row[0] == 'country_CAN':
            row.append(weights_country_CAN[int(row[1]) - 1])
            row.append(country_CAN_avg[int(row[1]) -1])
            row.append(country_CAN_overall)
            row.append(country_CAN_avg[int(row[1]) -1])
            row.append(country_CAN_overall)
        elif row[0] == 'rs_GP':
            row.append(weights_rs_GP[int(row[1]) - 1])
            row.append(rs_GP_norm_avg[int(row[1]) -1])
            row.append(rs_GP_overall)
            row.append(rs_GP_avg[int(row[1]) -1])
            row.append(rs_GP)
        elif row[0] == 'rs_PIM':
            row.append(weights_rs_PIM[int(row[1]) - 1])
            row.append(rs_PIM_norm_avg[int(row[1]) -1])
            row.append(rs_PIM_overall)
            row.append(rs_PIM_avg[int(row[1]) -1])
            row.append(rs_PIM)
        elif row[0] == 'rs_PlusMinus':
            print rs_PlusMinus
            row.append(weights_rs_PlusMinus[int(row[1]) - 1])
            row.append(rs_PlusMinus_norm_avg[int(row[1]) -1])
            row.append(rs_PlusMinus_overall)
            row.append(rs_PlusMinus_avg[int(row[1]) -1])
            row.append(rs_PlusMinus)
        elif row[0] == 'rs_G':
            row.append(weights_rs_G[int(row[1]) - 1])
            row.append(rs_G_norm_avg[int(row[1]) -1])
            row.append(rs_G_overall)
            row.append(rs_G_avg[int(row[1]) -1])
            row.append(rs_G)
        elif row[0] == 'po_A':
            row.append(weights_po_A[int(row[1]) - 1])
            row.append(po_A_norm_avg[int(row[1]) -1])
            row.append(po_A_overall)
            row.append(po_A_avg[int(row[1]) -1])
            row.append(po_A)
        elif row[0] == 'po_P':
            row.append(weights_po_P[int(row[1]) - 1])
            row.append(po_P_norm_avg[int(row[1]) -1])
            row.append(po_P_overall)
            row.append(po_P_avg[int(row[1]) -1])
            row.append(po_P)
        elif row[0] == 'po_GP':
            row.append(weights_po_GP[int(row[1]) - 1])
            row.append(po_GP_norm_avg[int(row[1]) -1])
            row.append(po_GP_overall)
            row.append(po_GP_avg[int(row[1]) -1])
            row.append(po_GP)
        elif row[0] == 'po_PIM':
            row.append(weights_po_PIM[int(row[1]) - 1])
            row.append(po_PIM_norm_avg[int(row[1]) -1])
            row.append(po_PIM_overall)
            row.append(po_PIM_avg[int(row[1]) -1])
            row.append(po_PIM)
        elif row[0] == 'po_PlusMinus':
            row.append(weights_po_PlusMinus[int(row[1]) - 1])
            row.append(po_PlusMinus_norm_avg[int(row[1]) -1])
            row.append(po_PlusMinus_overall)
            row.append(po_PlusMinus_avg[int(row[1]) -1])
            row.append(po_PlusMinus)
        elif row[0] == 'position_R':
            row.append(weights_position_R[int(row[1]) - 1])
            row.append(position_R_avg[int(row[1]) -1])
            row.append(position_R_overall)
            row.append(position_R_avg[int(row[1]) -1])
            row.append(position_R_overall)
        elif row[0] == 'Height':
            row.append(weights_Height[int(row[1]) - 1])
            row.append(Height_norm_avg[int(row[1]) -1])
            row.append(Height_overall)
            row.append(Height_avg[int(row[1]) -1])
            row.append(Height)
        elif row[0] == 'position_D':
            row.append(weights_position_D[int(row[1]) - 1])
            row.append(position_D_avg[int(row[1]) -1])
            row.append(position_D_overall)
            row.append(position_D_avg[int(row[1]) -1])
            row.append(position_D_overall)
        elif row[0] == 'position_L':
            row.append(weights_position_L[int(row[1]) - 1])
            row.append(position_L_avg[int(row[1]) -1])
            row.append(position_L_overall)
            row.append(position_L_avg[int(row[1]) -1])
            row.append(position_L_overall)
        writer.writerow(row)




