drop view if exists chao_draft.LM_5_class_0_view;
create view chao_draft.LM_5_class_0_view as
SELECT PlayerName, country_group, Position,
1/(1+ EXP(-4.64 +
DraftAge * (-0.1) +
country_group='CAN' * (-0.02) +
country_group = 'EURO' * (0.18) +
country_group = 'USA'* (0.15) +
Height * (0.16) +
Weight * (-0.02) +
Position = 'C' * (-0.08) +
Position = 'L' * (-0.06) +
Position = 'D' * (0.03) +
Position = 'R' * (-0.23) +
CSS_rank * (0.01) +
rs_GP * (-0.03) +
rs_G * (0.01) +
rs_A * (-0.01) +
rs_P * (0) +
rs_PIM * (0) +
rs_PlusMinus * (0.03) +
po_GP * (0.01) +
po_G * (-0.04) +
po_A * (-0) +
po_P * (-0) +
po_PIM * (-0) +
po_PlusMinus * (0.07))) AS class_0_prob, GP_greater_than_0, CSS_rank, rs_PlusMinus
FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values
where (CSS_rank >= 22 or CSS_rank=0) AND DraftAge <= 23 AND rs_GP >= 24 AND rs_PlusMinus = 0;