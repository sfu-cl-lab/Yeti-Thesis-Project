import csv
import pandas as pd
import numpy as np

weights_DraftAge = [1.5253614015, 2.2681273438, 2.2681273438, 2.2681273438, 0.7210529086]
weights_Weight = [1.4919620265, 1.5706434401, 1.5706434401, 1.5706434401, 1.5706434401]
weights_CSS_rank = [-1.256756345, -1.4750414248, -2.2145122397, -1.4750414248, -1.4750414248]
weights_rs_A = [-1.3622035894, 0, 0, 0, 0]
weights_rs_P = [1.5706334136, 1.5706334136, 1.5706334136, 1.5706334136, 1.5706334136]
weights_country_EURO = [0, -0.1901788186, 0.0056782221, -0.1901788186, 0]
weights_rs_GP = [0, 1.1639704533, 2.4135766868, 1.8403281774, 1.1639704533]
weights_rs_PIM = [0, 0, -1.0367303956, -1.0367303956, 0]
weights_rs_PlusMinus = [0, 1.8081514932, -10.8803616145, 0.7777586333, 0]
weights_po_A = [0, 0, -0.9534784316, 0, 0]
weights_po_P = [0, 1.4172451085, 1.4172451085, 4.3659576659, 1.4172451085]
weights_po_PIM = [0, 22.3783855159, 1.5097963896, 5.2983383711, 0]
weights_po_PlusMinus = [0, -7.1433895008, -7.1433895008, -7.1433895008, -7.1433895008]
weights_position_R = [0, 0, 0, 0, -0.1171557532]
weights_country_CAN = [0, 0, 0.332912836, 0.332912836, 0]
weights_0 = [-3.0996183241, -2.3823397672, 7.1465753249, -1.9780057039, -1.1012862109]

with open('Desktop/output_with_diff_01_02.csv', 'rb') as csvfile:
    d_reader = csv.DictReader(csvfile)
    weighted_DraftAge = []
    weighted_Weight = []
    weighted_CSS_rank = []
    weighted_rs_A = []
    weighted_rs_P = []
    weighted_country_EURO = []
    weighted_rs_GP = []
    weighted_rs_PIM = []
    weighted_rs_PlusMinus = []
    weighted_po_A = []
    weighted_po_P = []
    weighted_po_PIM = []
    weighted_po_PlusMinus = []
    weighted_position_R = []
    weighted_country_CAN = []
    Weights_0_val = []
    for row in d_reader:
        weighted_DraftAge.append(float(weights_DraftAge[int(row['LeafNode'])-1]) * float(row['DraftAge_norm_diff']))
        weighted_Weight.append(float(weights_Weight[int(row['LeafNode'])-1]) * float(row['Weight_norm_diff']))
        weighted_CSS_rank.append(float(weights_CSS_rank[int(row['LeafNode'])-1]) * float(row['CSS_rank_norm_diff']))
        weighted_rs_A.append(float(weights_rs_A[int(row['LeafNode'])-1]) * float(row['rs_A_norm_diff']))
        weighted_rs_P. append(float(weights_rs_P[int(row['LeafNode'])-1]) * float(row['rs_P_norm_diff']))
        weighted_country_EURO.append(float(weights_country_EURO[int(row['LeafNode'])-1]) * float(row['country_EURO_diff']))
        weighted_rs_GP.append(float(weights_rs_GP[int(row['LeafNode'])-1]) * float(row['rs_GP_norm_diff']))
        weighted_rs_PIM.append(float(weights_rs_PIM[int(row['LeafNode'])-1]) * float(row['rs_PIM_norm_diff']))
        weighted_rs_PlusMinus.append(float(weights_rs_PlusMinus[int(row['LeafNode'])-1]) * float(row['rs_PlusMinus_norm_diff']))
        weighted_po_A.append(float(weights_po_A[int(row['LeafNode'])-1]) * float(row['po_A_norm_diff']))
        weighted_po_P.append(float(weights_po_P[int(row['LeafNode'])-1]) * float(row['po_P_norm_diff']))
        weighted_po_PIM.append(float(weights_po_PIM[int(row['LeafNode'])-1]) * float(row['po_PIM_norm_diff']))
        weighted_po_PlusMinus.append(float(weights_po_PlusMinus[int(row['LeafNode'])-1]) * float(row['po_PlusMinus_norm_diff']))
        weighted_position_R.append(float(weights_position_R[int(row['LeafNode'])-1]) * float(row['position_R_diff']))
        weighted_country_CAN.append(float(weights_country_CAN[int(row['LeafNode'])-1]) * float(row['country_CAN_diff']))
        Weights_0_val.append(float(weights_0[int(row['LeafNode'])-1]))

with open('Desktop/output_with_diff_01_02.csv', 'rb') as input, open('Desktop/output_with_diff_01_02_weighted_diff.csv', 'wb') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    row = next(reader)  # read title line
    row.append('weighed_DraftAge_norm_diff')
    row.append('weighed_Weight_norm_diff')
    row.append('weighed_CSS_rank_norm_diff')
    row.append('weighed_rs_A_norm_diff')
    row.append('weighed_rs_P_norm_diff')
    row.append('weighed_country_EURO_diff')
    row.append('weighed_rs_GP_norm_diff')
    row.append('weighed_rs_PIM_norm_diff')
    row.append('weighed_rs_PlusMinus_norm_diff')
    row.append('weighed_po_A_norm_diff')
    row.append('weighed_po_P_norm_diff')
    row.append('weighed_po_PIM_norm_diff')
    row.append('weighed_po_PlusMinus_norm_diff')
    row.append('weighed_position_R_diff')
    row.append('weighed_country_CAN_diff')
    row.append('weight_0')
    writer.writerow(row)  # write enhanced title line

    it_1 = weighted_DraftAge.__iter__()
    it_2 = weighted_Weight.__iter__()
    it_3 = weighted_CSS_rank.__iter__()
    it_4 = weighted_rs_A.__iter__()
    it_5 = weighted_rs_P.__iter__()
    it_6 = weighted_country_EURO.__iter__()
    it_7 = weighted_rs_GP.__iter__()
    it_8 = weighted_rs_PIM.__iter__()
    it_9 = weighted_rs_PlusMinus.__iter__()
    it_10 = weighted_po_A.__iter__()
    it_11 = weighted_po_P.__iter__()
    it_12 = weighted_po_PIM.__iter__()
    it_13 = weighted_po_PlusMinus.__iter__()
    it_14 = weighted_position_R.__iter__()
    it_15 = weighted_country_CAN.__iter__()
    it_16 = Weights_0_val.__iter__()
    
    for row in reader:
        if row:  # avoid empty lines that usually lurk undetected at the end of the files
            try:
                row.append(next(it_1))
                row.append(next(it_2))
                row.append(next(it_3))
                row.append(next(it_4))
                row.append(next(it_5))
                row.append(next(it_6))
                row.append(next(it_7))
                row.append(next(it_8))
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


