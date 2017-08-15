### Step 1: crawl season-by-season statistics for all skaters who played games (GP > 0) in NHL between season 1998-1999 to season 2016-2017. 
+ Data is crawled from NHL.com, under "STATS" --> "PLAYERS". i.e. link here: http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=S&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,1&sort=points,goals,assists
+ Python scripts and sample data files can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_NHL_season_stats
+ The data is written to database as table `chao_draft.NHL_season_stats_1998_2016_original` (referred as table_1 in this context for convenience).
+ Note: this dataset also includes skaters who got drafted before 1998 and after 2008 which is outside of the range of our intest. Those skaters will be screened out in further process.
   
### Step 2: screen players in table_1; crawl player statistics for skaters who got drafted between year 1998-2008.
+ With player id (e.g. PlayerId = 8473593) obtained from table_1, crawl player stats for skaters who got drafted between 1998-2008 from NHL.com using url = "http://www.nhl.com/player/" + player_id
+ Python scripts and sample data files can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_NHL_player_stats
+ Record each players demographic info, draft info as well as his season stats for the last season he played before he got drafted into NHL.
+ The data is written to database as table `chao_draft.NHL_skaters_stats_1998_2008_original` (referred as table_2).
+ Total number of distinct skaters in table_2 is 1106.
+ Note that skaters in `table_1` and `table_2` have played greater than zero game (GP > 0) in NHL. 
+ Based on PlayerId, eliminate season stats for skaters who got drafted outside the draft year range of 1998-2008 in table_1, save the season stats of our interest as 
view `chao_draft.NHL_season_stats_for_skaters_drafted_1998_2008_view` (view_3) and table `chao_draft.NHL_season_stats_for_skaters_drafted_1998_2008` (table_3).
+ Important note: table_3 contains skaters who got drafted within the draft year range of our interest BUT DID NOT PLAY games in their first 7 seasons in NHL. To be exact, there are 28 of them who didn't play any games (including playoffs) in NHL until their 8th season or later on.
 
### Step 3: get player stats for skaters who got drafted into NHL but never played games in NHL.
+ Crawl player stats for all skaters who got drafted between 1998-2008 from eliteprospects.com in regardless these skaters ended up playing gmaes in NHL or not.
+ Data is crawled from eliteprospects.com, under "DRAFTS" --> select draft year between 1998-2008.
+ Python scripts and sample data files can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_elite_prospects
+ Only skaters' stats are recorded. Goalies are ommitted.
+ The data is written to database as table `chao_draft.elite_prospects_skaters_stats_1998_2008_original` (table_4).
+ Total number of distinct skaters in table_4 is 2480.
+ Identify all 1106 players from table_2 in table_4 using the unique (DraftYear, Overall) key for each player, saved as `chao_draft.elite_nhl_duplicated_skaters_view`(view_4).
      
      create view chao_draft.elite_nhl_duplicated_skaters_view as
      select distinct eliteId, t1.PlayerName as elite_name, t2.PlayerName as nhl_name, PlayerId, t2.DraftYear, t2.Overall
      from chao_draft.elite_prospects_skaters_stats_1998_2008_original as t1,
      chao_draft.NHL_skaters_stats_1998_2008_original as t2
      where t1.DraftYear = t2.DraftYear and t1.Overall = t2.Overall
      order by t2.DraftYear, t2.Overall;
         
+ Removing players appeared in table_2(GP > 0) from table_4, are the skaters who got drafted but never played in NHL. Saved as
view `chao_draft.elite_zerogames_skaters_find_CSSrank_view`(view_5) and table `chao_draft.elite_zerogames_skaters_find_CSSrank` (table_5)
      
      create table chao_draft.elite_zerogames_skaters_find_CSSrank as
      select distinct eliteId, PlayerName, BirthDate, Birthplace, DraftYear, Overall
      from chao_draft.elite_prospects_skaters_stats_1998_2008_original
      where eliteId not in
      (select eliteId from chao_draft.elite_nhl_duplicated_skaters_view);
      
+ Total number of distinct skaters in table_5 (GP = 0) is 2480 - 1106 = 1374.
+ Note: It rarely happens but a few skaters got drafted twice by NHL. In that case, only the stats of their second draft is recorded. Therefore, in table_5, there is one player (eliteId = 19183, PlayerName = Teigan Zahn) who has a draft year later than year 2008. 
 
### Step 4: obtain final Central Scouting Services(CSS) rank for all skaters from North America and Europe.
+ The final CSS rank is available only on draftanalyst.com --> under "Rankings" --> "Year-to-Year Central Scouting Final Rankings".
+ Scrape the rankings for skaters only (not interested in goalies) from both North America or Europe between draft year 1998-2008.
+ The data is written to database as table `chao_draft.draft_analyst_CSS_rank` (table_6)
+ Note: In comparison , draft year 2003 has the least number of CSS ranks available, i.e. there are only 55 ranks available skaters from north America and Europe in total. 


   DraftYear | count(*) |
   ---------- |-----|
   1998 | 146 |
   1999 | 296 |
   2000 | 309 |
   2001 | 309 |
   2002 | 220 |
   2003 | 55 |
   2004 | 390 |
   2005 | 280 | 
   2006 | 379 |
   2007 | 385 |
   2008 | 385 |


### Step 5: find corresponding CSS ranks from table_6 for skaters in table_2 (GP > 0) and table_5 (GP = 0).
+ Firstly, many skaters' CSS ranks can be matched by simply joining table_2 (or table_5) with table_6 on same DraftYear and same PlayerName.
+ However, due to misspelling or the use of nicknames, many skaters' ranks need to be matched painfully in the manual way.
+ Also upated table_6 with corresponding PlayerId from table_2 and eliteId from table_5.
+ Note: many PlayerNames in table_6 have been modified corresponding to table_2 and table_5.

### Step 6: create seven-season stats tables that are equivalent to Wilson's table.
+ Depending on including playoffs in NHL or not, two views are created as 
`chao_draft.season_sums_with_playoffs_1998_2008_view` (view_7) and `chao_draft.season_sums_regular_season_only_1998_2008_view` (view_8).
These two views have summed the number of GP and TOI in minutes for each season for each player.
+ Based on view_7 and view_8, repectively, two tables that contain skaters' first seven-season stats in NHL are created as
`chao_draft.seven_season_sums_with_playoffs_1998_2008` (table_7) and `chao_draft.seven_season_sums_regular_season_only_1998_2008` (table_8)
+ Note: as mentioned in step 2, there are 28 players among the 1106 players who got drafted between 1998 and 2008 and eventually did play games in NHL. However, they did not play any games (including playoffs) in their first seven seasons in NHL. 
+ From table_8, eliminate players who got drafted in year 2003 (as a large portion of them have no CSS ranks) we get view_9 as `chao_draft.seven_season_sums_regular_season_only_10_years_view`.
+ There are 988 distinct players in view_9.

#### Note on the seven-season stats table.
+ According to one of Schucker's paper: https://arxiv.org/abs/1411.5754, a player's first 7 seasons in NHL is counted chronologically in the straightforward way: e.g. for a player who got drafted in 1998, his 1st season in NHL is 1998-1999, 2nd is 1999-2000, .... , his 7th season is 2004-2005. Whether this player played games or not in these 7 seasons, these seasons are unchagned.
+ However, in Wilson's data, a player's frist 7 seasons in NHL are counted as only the 7 seasons in which a player did play games in NHL. Take the player "Scott Parker" for example, Wilson skipped season 1999-2000 and season 2004-2005 during which Parker didn't play games, and added season 2005-2006 and season 2006-2007 as Parker's seven season. As a result, the sum of seven-season of GP for a larger number of players is incorrect in Wilson's dataset.
+ The following example is taken from table_3.

PlayerId | 8465016 | GP |
-------- |-------- | --------|
PlayerName | Scott Parker |   |
DraftYear | 1998 |       |
1st season | 1998-1999 | 27 |
2nd season | 1999-2000 | 0 |
3rd season | 2000-2001 | 69 |
4th season | 2001-2002 | 63 |
5th season | 2002-2003 | 43 |
6th season | 2003-2004 | 50 |
7th season | 2004-2005 | 0 |
8th season | 2005-2006 | 10 |
9th season | 2006-2007 | 21 |
10th season | 2007-2008 | 25 |
Wison's sum | = 27 + 69 + 63 + 43 + 50 + 10 + 21 | = 283 |
Correct sum | = 27 + 0 + 69 + 63 + 43 + 50 + 0 | = 252

### Step 7: skater stats with CSS rank for year 1998-2002 and 2004-2008.
+ Player stats for skaters in table_2 including their CSS ranks is saved as view `chao_draft.nhl_nonzerogames_skaters_stats_1998_2008_view`(view_10). There are 1106 distinct players in view_10; 778 of them have CSS ranks.
+ Excluding year 2003, player stats for skaters in view_9 including their CSS ranks is saved as view `chao_draft.nhl_nonzerogames_skaters_stats_10_years_view`(view_11). There are 988 distinct players in view_11; 741 of them have CSS ranks.
+ Player stats for skaters in table_4 including their CSS ranks is saved as view `chao_draft.elite_zerogames_skaters_stats_1998_2008_view`(view_12). There are 1373 distinct players in view_12; 832 of them have CSS ranks.
+ Excluding year 2003, player stats for skaters in table_4 including their CSS ranks is saved as view `chao_draft.elite_zerogames_skaters_stats_10_years_view`(view_13). There are 1236 distinct players in view_13; 817 of them have CSS ranks.
+ Union view_11 and view_13 to include player stats for all skater, whether played for NHL or not, in one view as `chao_draft.all_skaters_stats_10_years_view` (view_14). There are 988+1236=2224 distinct players in view_14; 741+817=1558 of them have CSS ranks.


### Step 8: summerize all players' and seasons' statisticts in one row.
+ Summerize each skater's demographic info, the stats (such as GP, G, A, P, etc.) of his regular season and playoffs in the last season before he got drafted into NHL, as well as his first seven season's performance in NHL, into one row.
+ Based on view_14, sum each skaters' regular seasons stats in view `chao_draft.all_skaters_stats_regularseason_sum_10_years_view` (view_15).
+ Similarly, based on view_14, sum each skaters' playoffs stats in view `chao_draft.all_skaters_stats_playoffs_sum_10_years_view` (view_16).
+ Join skaters stats with seasons stats in one row, saved as view `chao_draft.join_skater_and_season_stats_10_years_view` (view_17).
+ Materialize view_17 as table `chao_draft.join_skater_and_season_stats_10_years`(table_17). Add 'country_group' column (i.e. 'CAN', 'USA' or 'EURO') and 'GP_greater_than_0' column (i.e. 'yes' or 'no'). 

         alter table chao_draft.join_skater_and_season_stats_10_years
         add column country_group VARCHAR(10) after Country;
         update chao_draft.join_skater_and_season_stats_10_years
         set country_group = case
         when Country = 'Canada' or Country = 'CAN' then 'CAN'
         when Country = 'USA' then 'USA'
         else 'EURO'
         end;
         
         alter table chao_draft.join_skater_and_season_stats_10_years
         add column GP_greater_than_0 VARCHAR(10);
         update chao_draft.join_skater_and_season_stats_10_years
         set GP_greater_than_0 = case
         when sum_7yr_GP > 0 then 'yes'
         else 'no'
         end;
 
##### Issue solved: unclear position of 46 skaters in view_17
+ 46 skaters in view_17 have unclear positions (i.e. 'W' or 'F'). They are obtained from eliteprospects.com.
+ These 46 skaters' specific position can be found from NHL.com and hockeydb.com 
+ Their old and new position info is saved as `chao_draft.position_unclear_skaters_10_years` (table_18).

         update chao_draft.join_skater_and_season_stats_10_years as t1,
         chao_draft.position_unclear_skaters_10_years as t2
         set t1.Position = t2.new_position
         where t1.id = t2.eliteId;

+ In table_17, missing/null values exist in several columns such as CSS_rank, po_GP, po_G, ..., sum_7yr_GP and sum_7yr_TOI. However, except for column CSS_rank for a player, other null values are known to be zero. Therefore, we create a new table `chao_draft.join_skater_and_season_stats_10_years_CSS_null`(table_19) to fill those missing values with zero, leaving only the CSS_rank column with missing values.
+ There are 2224 players in table_19; 1558 of them have CSS ranks; 964 of them have GP > 0 in their first seven years in NHL.

### Step 9: normalize data for Logistic/Linear Model Tree in Weka.
+ Using the same schema as in Schuckers' paper, divide the 10 years of skater and season stats into two cohorts.

cohort| 1st | | 2nd  | |
-------|---- |----------- |---| ---- |
set| training set | test set | training set | test set |
years | 1998, 1999 & 2000 | 2001 & 2002 | 2004, 2005 & 2006 | 2007 & 2008 |
num. of skaters in cohort | 1210 | | 1014 | |
num. of skaters in set | 711 | 499 | 637 | 377 |
num. of skaters with GP > 0 | 305 | 193 | 282 | 184 |
    
+ Need to normalize training and test data together for each cohort.
+ Normalization code and data is saved here:  
+ Normalized data is written to database, saved as table `chao_draft.join_skater_and_season_stats_10_years_CSS_null_norm`(table_20)

### Step 10: run Logistic Model Tree(LMT) in Weka on table_20

+ Run Weka and read from database sever by following the instructions from here: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/How%20to%20connect%20to%20MySql%20database%20in%20WEKA.md
+ Note: we keep the missing values as null because "LMT can deal with binary and multi-class target variables, numeric and nominal attributes and missing values".
+ Save two datasets as .arff files and rename as `skater_and_season_stats_GP0_first3years_cleaned.arff` and `skater_and_season_stats_GP0_second3years_cleaned.arff`, respectively. Weka data files and results are saved in the fold `weka_results` in this repository.
+ To run LMT on the above two datasets in Weka, under 'Classify' --> choose 'Classifier' --> 'trees' --> 'LMT'. Change the following settings for LMT: `doNotMakeSplitPointActualValue = True`, `numDecimalPlaces = 6`.   Under 'Test opstions' choose 'Use training set'. 
+ Run tests, save weka outputs as `results_first3years.txt` and `results_second3years.txt`, respectively, saved in the same folder 'weka_results'.
+ Use the weights from the above two txt files to build models to predict player performance for cohort 1 & 2, repectively.

### Step 10: predict formance of players 
+ use models to predict players who got drafted in 2001&2002 in cohort 1, and 2007&2008 in cohort 2, repectivley.
+ python code can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/Logistic_Model_Tree
+ When plugging players stats into the model, we need to replace missing values in `table_17` with 0 and save the new table as `chao_draft.join_skater_and_season_stats_10_years_no_null_values` (referred as `table_18`). 
+ The players' probabilty of playing games in NHL or not is written to database and saved as `chao_draft.lmt_prediction_1st_cohort` and `chao_draft.lmt_prediction_2nd_cohort`.

### Step 11: calculate rankings with ties for Spearman rank correlation
+ clean the original discontinuous draft number/overall for year 01, 02, 07 & 08 as we didn't take goalies into account.
Save as `chao_draft.rerank_overall_2001/2/7/8` (referred as `table_19s`).

      create table chao_draft.rerank_overall_2002 as
      SELECT id, PlayerName, DraftYear, Overall as original_overall,
        @prev := @curr,
        @curr := Overall,
        @rank := IF(@prev = @curr, @rank, @rank + @i) AS skaters_overall,
        IF(@prev <> Overall, @i:=1, @i:=@i+1) AS counter
      FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values,
        (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
      where DraftYear = 2002
      order by Overall ASC
      
+ calculte the true rankings for players based on their 7-year sum of GP/TOI. Save as `chao_draft`.`rank_sum_7yr_GP_2001/2/7/8` (referred as `table_20s`) and `chao_draft`.`rank_sum_7yr_TOI_2001/2/7/8` (referred as `table_21s`)

      create table chao_draft.rank_sum_7yr_GP_2002 as
      SELECT id, PlayerName, DraftYear, sum_7yr_GP,
        @prev := @curr,
        @curr := sum_7yr_GP,
        @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_sum_7yr_GP,
        IF(@prev <> sum_7yr_GP, @i:=1, @i:=@i+1) AS counter
      FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values,
        (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
      where DraftYear = 2002
      order by sum_7yr_GP DESC;
      
      create table chao_draft.rank_sum_7yr_TOI_2002 as
      SELECT id, PlayerName, DraftYear, sum_7yr_TOI,
        @prev := @curr,
        @curr := sum_7yr_TOI,
        @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_sum_7yr_TOI,
        IF(@prev <> sum_7yr_TOI, @i:=1, @i:=@i+1) AS counter
      FROM chao_draft.join_skater_and_season_stats_10_years_no_null_values,
        (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
      where DraftYear = 2002
      order by sum_7yr_TOI DESC;
      
 + rank the predicitons given by LMT models. `chao_draft`.`rank_lmt_prob_2001/2/7/8` (referred as `table_22s`)

         create table chao_draft.rank_lmt_prob_2002 as
         SELECT id, PlayerName, DraftYear, class_0_prob,
           @prev := @curr,
           @curr := class_0_prob,
           @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_prob,
           IF(@prev <> class_0_prob, @i:=1, @i:=@i+1) AS counter
         FROM chao_draft.lmt_prediction_1st_cohort,
           (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
         where DraftYear = 2002
         order by class_0_prob DESC
 
 + Union `table_19s`, `table_20s` and `table_21s`. Save as `chao_draft.union_overall_GP_TOI_1278_VIEW`(referred as `view_23`).
 + Union `table_22s`. Save as `chao_draft.union_rank_lmt_prob_1278_view`(referred as `view_24`).

 
### Step 12: run 3-class Logistic Model Tree(LMT) in Weka on the new table_17
+ Add 3-class labels in `table_17` as "Good" for sum_7yr_GP = 0, "Better" for 1 <= sum_7yr_GP < 160, & "Better" for sum_7yr_GP >= 160
+ Use the same schema when dividing dataset into training and test datasets.
+ Use the same settings in Weka as in Step 9.
+ Results are saved in https://github.com/sfu-cl-lab/Yeti-Thesis-Project/tree/master/Weka_Decision_Tree/LMT

### Step 13: Build M5P dicision tree model with training dataset
+ M5P in weka can also deal with missing values. The training dataset should only contain skaters who played greater than 0 games in NHL.
+ Create view `chao_draft.m5p_training_set_1st_cohort_view` (`view_27`) and `chao_draft.m5p_training_set_2nd_cohort_view` (`view_28`) based on `table_17`.
+ There are 305 and 282 skaters in `view_27` and `view_28`, respectively.
+ M5P decision tree settings are as follows: numDecimalPlaces = 6, buildRegressionTree = False, unpruned = False, etc.
+ M5P input .arff files and outputs are saved in: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/tree/master/Weka_Decision_Tree/M5P 

### Step 14: Select players with LMT probability >= 0.5 as M5P test set
+ Join `table_18`with `table_22s` on selecting players with LMT probability >= 0.5 to get views `chao_draft.m5p_test_set_2001_view`, `chao_draft.m5p_test_set_2002_view`, `chao_draft.m5p_test_set_2007_view` and `chao_draft.m5p_test_set_2008_view` (`view_29s`).
+ Need to normalize data by running python code. Then calculate predected sum_7yr_GP with training model. Code can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/M5P_Model_Tree
+ Results are written back to database as `chao_draft`.`m5p_prediction_1st_cohort` & `chao_draft`.`m5p_prediction_2nd_cohort` (`table_30s`)
+ Rank predicted 7-year GP given by M5P model and obtain `chao_draft.rank_m5p_prob_2001`, `chao_draft.rank_m5p_prob_2002`, `chao_draft.rank_m5p_prob_2007` and `chao_draft.rank_m5p_prob_2008` (`table_31s`)
+ Note: Those player who have LMT probabilty < 0.5, are ranked together with players in table_31s and tied at at the bottom in order to calculate Spearman rank correlation 
+ Union `table_30s` to get `chao_draft.union_rank_m5p_prob_1278_view` (`view_32`)
+ Union `view_23`, `view_24` and `view_31`, save as `chao_draft.union_all_ranks_view` (referred as `view_33`).

### Step 15: Calculate Spearman Rank Correlation
+ The following link is a guide to calculating Spearman rank correlation: https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php
+ Because we have ties in ranking sum_7yr_GP/TOI & lmt_probability, the corresponding equation for ties were used in our calculation.
+ Results are saved in: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/tree/master/Weka_Decision_Tree/Spearman_rank_correlation

