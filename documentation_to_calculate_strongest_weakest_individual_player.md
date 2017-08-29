 + Create view `chao_draft.lmt_testYears_CSS_null_norm_prob_for_points` by adding numeric columns for position_L/R/D/C and country_USA/CAN/EURO.
 
 + Calculate sum of attributes difference with positive weight, sum of attributes difference with negative weight, and individual attribute difference times weight in two cohorts(players drafted in 2001/2 ; players drafted in 2007/8). code can be found here: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/Decision_Trees/LMT/calculate_diff_sum_with_pos_neg_weights.py , https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/Decision_Trees/LMT/calculate_individual_attribute_diff_times_weight.py
 
 + Store results in view 'chao_draft.individual_player_01_02/07_08'. Some fields in this view are explained in the following table:
 
 Field | Details |
 ----- |----------------|
player_diff_total_sum | **∑+w<sub>i</sub>(x<sub>i</sub>- x̄) + ∑-w<sub>i</sub>(x<sub>i</sub>- x̄)**, sum of all attributes difference compared to the mean value of each LeafNode |
weight_pos_val | **∑+w<sub>i</sub>(x<sub>i</sub>- x̄)**, sum of attributes difference with positive weights |
weight_neg_val | **∑-w<sub>i</sub>(x<sub>i</sub>- x̄)**, sum of attributes difference with negative weights |
weighed_attribute_diff | w<sub>attribute</sub>(x<sub>attribute</sub> - x̄<sub>attribute</sub>) |

+ Strongest player in strong LeafNodes(if the rate of GP_greater_than_0 > 50%)

id | PlayerName | DraftYear | LeafNode | GP_greater_than_0 | player_diff_total_sum | lmt_prob | weight_pos_val | weight_neg_val |
---| ---------- | --------- | -------- | -------------- | -------- | ------ | ----- | ----- |
8469455 | Jason Spezza | 2001 | 3 | yes | 2.573201971432897 | 0.9282017673222154 | 1.5149518724634254 | 1.0582500989694714 |
8469474 | Colby Armstrong | 2001 | 3 | yes | 2.3783673218444847 | 0.9140841746450182 | 1.733848766183595 | 0.6445185556608896 | 
8469454 | Ilya Kovalchuk | 2001 | 3 | yes | 2.191565712215148 | 0.8982338589620239 | 1.3044223178129801 | 0.8871433944021676 | 
8474040 | Sam Gagner | 2007 | 1 | yes | 4.0264360399140795 | 0.9969284587291163 | 3.607425146070099 | 0.4190108938439805 |
8474141 | Patrick Kane | 2007 | 1 | yes | 3.575510915857473 | 0.995186829189845 | 2.8495207008828474 | 0.7259902149746256 |
8474102 | David Perron | 2007 | 1 | yes | 3.2056610480408914 | 0.9930478269051884 | 3.150558241377556 | 0.05510280666333528 |
8474059 | Linus Omark | 2007 | 4 | yes | 1.3971131080309775 | 0.7998548932406279 | 0.3747145573109591 | 1.0223985507200184 |
8474114 | Oscar Moller | 2007 | 4 | yes | 1.390128255222534 | 0.7987343664858106 | 0.4388812508432919 | 0.951247004379242 |
8474627 | Jori Lehtera | 2008 | 4 | yes | 1.3543511587556547 | 0.7929214120046657 | 0.7584214819873075 | 0.5959296767683472 |
8474146 | Spencer Machacek | 2007 | 6 | yes | 1.8902042170864255 | 0.9900950944178386 | -0.021663440345763063 | 1.9118676574321887 |
9347 | Justin Azevedo | 2008 | 6 | no | 1.7695379029302973 | 0.9888389841358178 | 0.0913124006850809 | 1.6782255022452164 | 
8474631 | Marc-Andre Bourdon | 2008 | 6 | yes | 1.6371760954445473 | 0.9872795553672469 | 0.16824162116048047 | 1.4689344742840669 |


+ Some players have high value in weight_pos_val(∑+ wi(xi- x̄)) but lower value in player_diff_total_sum(∑+wi(xi- x̄)). It means they are exceptional in some fields but also have obvious weaknesses in other fileds. e.g.

id | PlayerName | DraftYear | LeafNode | GP_greater_than_0 | player_diff_total_sum | lmt_prob | weight_pos_val | weight_neg_val | weighed_DraftAge_norm_diff | weighed_Weight_norm_diff | weighed_CSS_rank_norm_diff | weighed_rs_P_norm_diff | weighed_country_EURO_diff | weighed_rs_GP_norm_diff | weighed_rs_PIM_norm_diff | weighed_rs_PlusMinus_norm_diff | weighed_po_A_norm_diff | weighed_po_P_norm_diff | weighed_po_PIM_norm_diff | weighed_country_CAN_diff 
---| --- | ----| ---- | ---- | -- | --- | -- | --- | --- | ---| --- | ----| ---- | ---- | -- | --- | -- | --- | --- | ---- |
8469542 | Stephane Veilleux | 2001 | 3 | yes | 8.641748262585226 | 0.814777948388665 | 3.348573604539732 | -1.8534006668545049 | 0.0848315345122045 | -0.061360691633222 | -1.0909036201709423 | 0.8416343954816107 | -0.00243652510311 | 0.6469990348517232 | -0.06601310452150307 | 0.000000000000024159255961331284 | -0.6964839421620836 | 1.0981102334175368 | 0.5179770618781889 | 0.2228185611348 |

+ Some players have high value in our prediction(wx_sum, lmt_prob, player_diff_total_sum) but have GP_greater_than_0 = 'no' in
NHL. Partly because they are drafted but never sign a contract. Instead, they play in other competitive leagues. e.g.

id | PlayerName | DraftYear | LeafNode | GP_greater_than_0 | player_diff_total_sum | lmt_prob | weight_pos_val | weight_neg_val | career league |
---| ---------- | --------- | -------- | -------------- | -------- | ------ | ----- | ----- | ---- |
9347 | Justin Azevedo | 2008 | 6 | no | 1.7695379029302973 | 0.9888389841358178 | 0.0913124006850809 | 1.6782255022452164 | AHL/KHL |
































            
