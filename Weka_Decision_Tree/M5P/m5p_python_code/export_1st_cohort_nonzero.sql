SELECT t1.* 
FROM chao_draft.join_skater_and_season_stats_10_years_CSS_null_norm as t1,
chao_draft.lmt_10years_CSS_null_norm_prob as t2
where t1.id = t2.id and (
(t1.sum_7yr_GP > 0 and t1.DraftYear < 2001) 
or (t2.lmt_prob >= 0.5 and t1.DraftYear > 2000 and t1.DraftYear < 2003) 
);