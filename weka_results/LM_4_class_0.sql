drop view if exists chao_draft.LM_4_class_0_view;
create view chao_draft.LM_4_class_0_view as
SELECT PlayerName, country_group, Position,
1/(1+ EXP(-0.87 +
DraftAge * (0.02) +
country_group='CAN' * (-0.02) +
country_group = 'EURO' * (1.24) +
country_group = 'USA'* (-0.79) +
Height * (0.09) +
Weight * (-0.02) +
Position = 'C' * (0.15) +
Position = 'L' * (-0.07) +
Position = 'D' * (0.19) +
Position = 'R' * (-0.07) +
CSS_rank * (0) +
rs_GP * (-0.03) +
rs_G * (0.01) +
rs_A * (-0.02) +
rs_P * (0) +
rs_PIM * (0) +
rs_PlusMinus * (-0.01) +
po_GP * (-0.02) +
po_G * (-0.01) +
po_A * (-0.02) +
po_P * (0.03) +
po_PIM * (-0.01) +
po_PlusMinus * (0.04))) AS class_0_prob, GP_greater_than_0, CSS_rank, rs_PlusMinus
FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values
where (CSS_rank >= 22 or CSS_rank=0) AND DraftAge <= 23 AND rs_GP <=23;