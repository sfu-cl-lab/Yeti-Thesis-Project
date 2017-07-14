drop view if exists chao_draft.LM_3_class_0_view;
create view chao_draft.LM_3_class_0_view as
SELECT PlayerName, country_group, Position,
1/(1+ EXP(-43.53 +
DraftAge * (1.36) +
country_group='CAN' * (-0.4) +
country_group = 'EURO' * (0.32) +
country_group = 'USA'* (2.16) +
Height * (0.21) +
Weight * (0.05) +
Position = 'C' * (-0.84) +
Position = 'L' * (1.61) +
Position = 'D' * (-0.31) +
Position = 'R' * (1.63) +
CSS_rank * (0) +
rs_GP * (-0.01) +
rs_G * (-0.07) +
rs_A * (0.12) +
rs_P * (0) +
rs_PIM * (-0.01) +
rs_PlusMinus * (-0.07) +
po_GP * (-0) +
po_G * (-0.01) +
po_A * (-0.87) +
po_P * (-0.16) +
po_PIM * (-0.08) +
po_PlusMinus * (0.02))) AS class_0_prob, GP_greater_than_0, CSS_rank, rs_PlusMinus
FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values
where (CSS_rank >= 22 or CSS_rank=0) AND DraftAge <= 23 AND rs_GP <=23;