 + Create view `chao_draft.lmt_testYears_CSS_null_norm_prob_for_points` by adding numeric columns for position_L/R/D/C and country_USA/CAN/EURO.
 
 + Calculate sum of attributes difference with positive weight, sum of attributes difference with negative weight, and individual attribute difference times weight in two cohorts(players drafted in 2001/2 ; players drafted in 2007/8). code can be found here: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/Decision_Trees/LMT/calculate_diff_sum_with_pos_neg_weights.py , https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/Decision_Trees/LMT/calculate_individual_attribute_diff_times_weight.py
 
 + Store results in view 'chao_draft.individual_player_01_02/07_08'. Some fields in this view are explained in the following table:
 
 Field | Details |
 ----- |----------------|
player_diff_total_sum | **∑wi(xi- x̄)**, sum of all attributes difference compared to the mean value of each LeafNode |
weight_pos_val | **∑+wi(xi- x̄)**, sum of attributes difference with positive weights |
weight_neg_val | **∑-wi(xi- x̄)**, sum of attributes difference with negative weights |
weighed_attribute_diff | w<sub>attribute</sub>(x<sub>attribute</sub> - x̄<sub>attribute</sub>) |





















            
