### Step 1: crawl season-by-season statistics for all skaters who played games in NHL between season 1998-1999 to season 2016-2017. 
+ Data is crawled from NHL.com, under "STATS" --> "PLAYERS". i.e. link here: http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=S&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,1&sort=points,goals,assists
+ Python scripts and sample data files can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_NHL_season_stats
+ The data is written to database as table "`chao_draft.NHL_season_stats_1998_2016_original`" (referred as `table_1` in this context for convenience).
+ Note: this dataset also includes skaters who got drafted before 1998 and after 2008 which is outside of the range of our intest.
   
### Step 2: screen players in table_1; crawl the player statistics for skaters who got drafted between year 1998-2008.
+ With player id (e.g. PlayerId = 8473593) obtained from `table_1`, crawl player stats for skaters for got drafted between 1998-2008 from NHL.com using url = "http://www.nhl.com/player/" + player_id
+ Python scripts and sample data files can be found here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_NHL_player_stats
+ Record each players demographic info, draft info as well as his season stats for the last season he played before he got drafted into NHL.
+ The data is written to database as table "`chao_draft.NHL_skaters_stats_1998_2008_original`" (referred as `table_2`).
+ Total number of distinct skaters in `talbe_2` is 1106.
+ Note that skaters in `table_1` and `table_2` have played greater than zero game in NHL. NHL.com does not have statistics for players who got drafted into NHL but didn't play any games in NHL, which is available in Step 3.
+ Based on PlayerId, eliminate season stats for skaters who got drafted outside the draft year range of 1998-2008 in `table_1`, save the season stats of our interest as 
view "`chao_draft.NHL_season_stats_for_skaters_drafted_1998_2008_view`" (referred as `view_3`) and table "`chao_draft.NHL_season_stats_for_skaters_drafted_1998_2008`" (referred as `table_3`).
+ Note: `table_3` contains skaters who got drafted within the draft year range of our interest BUT DID NOT PLAY games in their first 7 seasons in NHL. To be exact, there are 28 of them didn't play games in NHL until their 8th season or later on.
 
### Step 3: get player stats for skaters who got drafted into NHL but never played games in NHL.
+ Crawl player stats for all skaters who got drafted between 1998-2008 from eliteprospects.com whether these skaters ended up playing gmaes in NHL or not.
+ Data is crawled from eliteprospects.com, under "DRAFTS" --> select draft year between 1998-2008.
+ Python scripts and sample data files can be find here: https://github.com/chaostewart/summer_research_2017/tree/master/crawl_elite_prospects
+ Only skaters' stats are recorded. Goalies are ommitted.
+ The data is written to database as table "`chao_draft.elite_prospects_skaters_stats_1998_2008_original`" (referred as `table_4`).
+ Total number of distinct skaters in `talbe_4` is 2480.
+ Find all 1106 players from `table_2` in `table_4`, saved as "`chao_draft.elite_nhl_duplicated_skaters_view`" (referred as `view_4`).
      
      create view chao_draft.elite_nhl_duplicated_skaters_view as
      select distinct eliteId, t1.PlayerName as elite_name, t2.PlayerName as nhl_name, PlayerId, t2.DraftYear, t2.Overall
      from chao_draft.elite_prospects_skaters_stats_1998_2008_original as t1,
      chao_draft.NHL_skaters_stats_1998_2008_original as t2
      where t1.DraftYear = t2.DraftYear and t1.Overall = t2.Overall
      order by t2.DraftYear, t2.Overall;
         
+ Excluding players appeared in `table_2` from `table_4`, are the skaters who got drafted but never played in NHL. Saved as
view "`chao_draft.elite_zerogames_skaters_find_CSSrank`"(referred as `view_5`) and table "`chao_draft.elite_zerogames_skaters_find_CSSrank`" (referred as `table_5`)
      
      create table chao_draft.elite_zerogames_skaters_find_CSSrank as
      select distinct eliteId, PlayerName, BirthDate, Birthplace, DraftYear, Overall
      from chao_draft.elite_prospects_skaters_stats_1998_2008_original
      where eliteId not in
      (select eliteId from chao_draft.elite_nhl_duplicated_skaters_view);
+ Total number of distinct skaters in `talbe_5` is 2480 - 1106 = 1374.
+ Note: some skaters got drafted twice by NHL, only the stats of their second draft is recorded. Therefore, in the dataset there are players who got drafted later than year 2008. 
 
### Step 4: obtain final Cental Scouting Services(CSS) rank for all skaters.
+ The final CSS rank is available only on draftanalyst.com --> under "Rankings" --> "Year-to-Year Central Scouting Final Rankings".
+ Scrape the rankings for skaters only from both North America or Europe between 1998-2008.
+ The data is written to database as table "`chao_draft.draft_analyst_CSS_rank`" (referred as `table_6`)
+ Note: Draft year 2003 has the least number of CSS ranks available. There are only 55 ranks available skaters from north America and Europe in total. 


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


### Step 5: find corresponding CSS ranks from table_6 for skaters in talbe_2 and table_5.
+ Firstly, many skaters' CSS ranks can be matched by simply joining `table_2` (or `table_5`) with `table_6` on same DraftYear and same PlayerName.
+ However, due to misspelling or the use of nicknames, many skaters' ranks need to be matched painfully in a manual way.
+ Updated `table_6` with corresponding PlayerId from `table_2` and eliteId from `table_5`.
+ Note: many PlayerNames in `table_6` have been modified according to `table_2` and `table_5`.

### Step 6: create seven-season stats tables that are equivalent to Wilson's table.
+ Depending on including playoffs in NHL or not, two views are created as 
"`chao_draft.season_sums_with_playoffs_1998_2008_view`" (referred as `view_7`) and "`chao_draft.season_sums_regular_season_only_1998_2008_view`" (referred as `view_8`).
These two views sum number of GP and TOI in minutes for each season for each player.
+ Based on `view_7` and `view_8`, repectively, two tables that contain skaters first seven-season stats in NHL are created as
"`chao_draft.seven_season_sums_with_playoffs_1998_2008`" (referred as `table_7`) and "`chao_draft.seven_season_sums_regular_season_only_1998_2008`" (referred as `table_8`)
+ Note: there are 28 players among the 1106 players who got drafted between 1998 and 2008 and did play games in NHL. However, they did not play any games in their first seven seasons in NHL. 
+ Based on `table_8`, eliminate players who got drafted in year 2003 (as a large number of them have no CSS ranks) as well as players who played games in their frist seven seasons in NHL, we get `table_9` as "`chao_draft.seven_season_sums_regular_season_only_10_years_view`".
+ There are 964 distinct players in `table_9`.

### Step 7: skater stats with CSS rank for year 1998-2002 and 2004-2008.
+ Player stats for skaters in `table_2` including their CSS ranks is saved as view "`chao_draft.nhl_nonzerogames_skaters_stats_1998_2008_view`"(referred as `view_10`).
+ There are 1106 distinct players in `view_10`; 778 of them have CSS ranks.
+ Excluding year 2003, player stats for skaters in `table_9` including their CSS ranks is saved as view "`chao_draft.nhl_nonzerogames_skaters_stats_10_years_view`"(referred as `view_11`).
+ There are 964 distinct players in `view_11`; 722 of them have CSS ranks.
+ Player stats for skaters in `table_4` including their CSS ranks is saved as view "`chao_draft.elite_zerogames_skaters_stats_1998_2008_with_view`"(referred as `view_12`).
+ There are 1373 distinct players in `view_12`; 832 of them have CSS ranks.
+ Excluding year 2003, player stats for skaters in `table_4` including their CSS ranks is saved as view "`chao_draft.elite_zerogames_skaters_stats_10_years_view`"(referred as `view_13`).
+ There are 1236 distinct players in `view_13`; 817 of them have CSS ranks.
+ Union `view_11` and `view_13` to include player stats for all skater, whether player for NHL or not, in one view as "`chao_draft.all_skaters_stats_10_years_view`" (referred as `view_14`)
+ There are 2200 distinct players in `view_14`; 1539 of them have CSS ranks.


### Step 8: summerize all players' and seasons' statisticts in one row.
+ Summerize each skater's demographic info, the stats (such as GP, G, A, P, etc.) of his regular season and playoffs in the last season before he got drafted into NHL, as well as his first seven season's performance in NHL, into one row.
+ Based on `view_14`, sum each skaters' regular seasons stats in view "`chao_draft.all_skaters_stats_regularseason_sum_10_years_view`" (referred as `view_15`).
+ Based on `view_14`, sum each skaters' playoffs stats in view "`chao_draft.all_skaters_stats_playoffs_sum_10_years_view`" (referred as `view_16`).
+ Join skaters stats with seasons stats in one row, saved as view"`chao_draft.join_skater_and_season_stats_10_years_view`" (referred as `view_17`).
+ Materialize `view_17` as table "`chao_draft.join_skater_and_season_stats_10_years`" (referred as `table_17`). Add 'couutry_group' column (i.e. 'CAN', 'USA' or 'EURO') and 'GP_greater_than_0' column (i.e. 'yes' or 'no'). 


