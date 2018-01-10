### Drafting NBA Players Based on Their College Performance

+ Data is crawled from https://www.basketball-reference.com/draft/NBA_[1985-2011].html
+ Python scripts can be found here: https://github.com/HaoPatrick/NBA_draft_crawler
+ Predictors: NCAA college stats

Field | Explanation|
--------- | ----------- |
Height | * |
Weight | * |
Position| * |
Age| age in the Draft Year|
G_total | games played in the draft year|
MP_total | Minutes Played in the draft year|
FG_total | Field Goals in the draft year|
FGA_total | Field Goal Attempts in the draft year|
3P_total | 3-Point Field Goals in the draft year|
3PA_total | 3-Point Field Goals Attempt in the draft year|
FT_total | Free Throws in the draft year|
FTA_total |Free Throws Attempt in the draft year|
ORB_total | Offensive Rebouds in the draft year|
TRB_total | Total Rebounds in the draft year|
AST_total | Assits in the draft year|
STL_total | Steals in the draft year|
BLK_total | Blocks in the draft year|
TOV_total | Turnovers in the draft year|
PF_total | Personal Fouls in the draft year|
PTS_total | Points in the draft year|
FG% | Field Goal Percentage in the draft year|
3P% | 3-Point Field Goal Percentage in the draft year|
FT% | Free Throw Percentage in the draft year|
MP_perGame | Minutes Played per game in the draft year|
PTS_perGame |Points per game in college|
TRB_perGame | Total Rebounds per game in college|
ASB_perGame | Assist per game in college|
Amature_honor | NCAA all_American(1, 0)|

+ Evaluation Metrics: Overall Pick(pk)

***The datasets are stored in nba_patricks_draft.info_1985_2011 and nba_patricks_draft.college_1985_2011 under cs-oschulte-01.cs.sfu.ca***

+ Response Variables: NBA stats

Field | Explanation|
--------- | ----------- |
Career PER | A measure for player's per-minute performance, while adjusting for pace. A league-average PER is always 15.00, which permits comparisons of player performance across seasons.|
WinShare(WS) |  an estimate of the number of wins contributed by a player|
Career_WS/48 | an estimate of the number of wins contributed by a player per 48 minutes |

***The datasets are stored in nba_patricks_draft.career_1985_2011 under cs-oschulte-01.cs.sfu.ca***

+ Reference Paper:












