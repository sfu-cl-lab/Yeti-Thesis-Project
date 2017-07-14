drop view if exists chao_draft.LM_1_class_0_view;
create view chao_draft.LM_1_class_0_view as
SELECT PlayerName, country_group, Position,
1/(1+ EXP(14.89 +
DraftAge * (-0.59) +
country_group='CAN' * (-0.06) +
country_group = 'EURO' * (0.98) +
country_group = 'USA'* (-0.06) +
Height * (-0.05) +
Weight * (-0.01) +
Position = 'C' * (0.2) +
Position = 'L' * (-0.28) +
Position = 'D' * (-0.35) +
Position = 'R' * (0.12) +
CSS_rank * (0.07) +
rs_GP * (0) +
rs_G * (-0.03) +
rs_A * (-0.02) +
rs_PIM * (0.01) +
rs_PlusMinus * (-0.07) +
po_GP * (0.04) +
po_A * (0) +
po_P * (0.03) +
po_PIM * (-0) +
po_PlusMinus * (-0.29))) AS class_0_prob, GP_greater_than_0, CSS_rank, rs_PlusMinus
FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values
where (CSS_rank <= 21 AND CSS_rank!=0) AND rs_PlusMinus <= 0;