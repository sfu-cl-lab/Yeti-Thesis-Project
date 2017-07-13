drop view if exists chao_draft.LM_7_class_0_view;
create view chao_draft.LM_7_class_0_view as
SELECT PlayerName, country_group, Position,
(-25.9 +
DraftAge * (-0.22) +
country_group='CAN' * (-0.02) +
country_group = 'EURO' * (0.3) +
country_group = 'USA'* (-0.06) +
Height * (0.67) +
Weight * (-0.09) +
Position = 'C' * (1.03) +
Position = 'L' * (-3) +
Position = 'D' * (0.01) +
Position = 'R' * (-0.06) +
CSS_rank * (0) +
rs_GP * (-0.05) +
rs_G * (-0.02) +
rs_A * (-0.01) +
rs_P * (0) +
rs_PIM * (0) +
rs_PlusMinus * (0.18) +
po_GP * (-0) +
po_G * (-0) +
po_A * (0.08) +
po_P * (0.03) +
po_PIM * (-0.01) +
po_PlusMinus * (23.4)) AS class_0_prob, GP_greater_than_0, CSS_rank, rs_PlusMinus
FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values
where (CSS_rank >= 22 or CSS_rank=0) AND DraftAge >= 24;