import csv
import pandas as pd
import numpy as np

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

with open('Desktop/output_with_diff_07_08.csv', 'rb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    res = []
    for row in d_reader:
        res_item = (weights_DraftAge[int(row['LeafNode'])-1] * DraftAge_norm_avg[int(row['LeafNode'])-1] +
                    weights_Weight[int(row['LeafNode'])-1] * Weight_norm_avg[int(row['LeafNode'])-1] + 
                    weights_CSS_rank[int(row['LeafNode'])-1] * CSS_rank_norm_avg[int(row['LeafNode'])-1] + 
                    weights_rs_A[int(row['LeafNode'])-1] * rs_A_norm_avg[int(row['LeafNode'])-1] + 
                    weights_rs_P[int(row['LeafNode'])-1] * rs_P_norm_avg[int(row['LeafNode'])-1] + 
                    weights_country_EURO[int(row['LeafNode'])-1] * country_EURO_avg[int(row['LeafNode'])-1] +
                    weights_country_USA[int(row['LeafNode'])-1] * country_USA_avg[int(row['LeafNode'])-1] +
                    weights_country_CAN[int(row['LeafNode'])-1] * country_CAN_avg[int(row['LeafNode'])-1] +
                    weights_rs_GP[int(row['LeafNode'])-1] * rs_GP_norm_avg[int(row['LeafNode'])-1] + 
                    weights_rs_PIM[int(row['LeafNode'])-1] * rs_PIM_norm_avg[int(row['LeafNode'])-1] + 
                    weights_rs_PlusMinus[int(row['LeafNode'])-1] * rs_PlusMinus_norm_avg[int(row['LeafNode'])-1] +
                    weights_rs_G[int(row['LeafNode'])-1] * rs_G_norm_avg[int(row['LeafNode'])-1] +
                    weights_po_A[int(row['LeafNode'])-1] * po_A_norm_avg[int(row['LeafNode'])-1] + 
                    weights_po_P[int(row['LeafNode'])-1] * po_P_norm_avg[int(row['LeafNode'])-1] + 
                    weights_po_GP[int(row['LeafNode'])-1] * po_GP_norm_avg[int(row['LeafNode'])-1] +
                    weights_po_PIM[int(row['LeafNode'])-1] * po_PIM_norm_avg[int(row['LeafNode'])-1] + 
                    weights_po_PlusMinus[int(row['LeafNode'])-1] * po_PlusMinus_norm_avg[int(row['LeafNode'])-1] + 
                    weights_position_R[int(row['LeafNode'])-1] * position_R_avg[int(row['LeafNode'])-1] +
                    weights_Height[int(row['LeafNode'])-1] * Height_norm_avg[int(row['LeafNode'])-1] +
                    weights_position_D[int(row['LeafNode'])-1] * position_D_avg[int(row['LeafNode'])-1] +
                    weights_position_L[int(row['LeafNode'])-1] * position_L_avg[int(row['LeafNode'])-1])
        print row['LeafNode']
        print res_item
        res.append(res_item)

with open('Desktop/output_with_diff_07_08.csv', 'rb') as input, open('Desktop/output_07_08_weighted_mean.csv', 'wb') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')
    
    row = next(reader)  # read title line
    row.append('weighted_mean')
    writer.writerow(row)  # write enhanced title line

    it_1 = res.__iter__()
    
    for row in reader:
        if row:  # avoid empty lines that usually lurk undetected at the end of the files
            try:
                row.append(next(it_1))
            except StopIteration:
                row.append("N/A")     # not enough results: pad with N/A
            writer.writerow(row)


