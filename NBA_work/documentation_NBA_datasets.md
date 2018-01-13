### Drafting NBA Players Based on Their College Performance

+ Data is crawled from https://www.basketball-reference.com/draft/NBA_[1985-2011].html
+ Python scripts can be found here: https://github.com/HaoPatrick/NBA_draft_crawler
+ Predictors: NCAA college stats

Field | Explanation|
--------- | ----------- |
height | * |
weight | * |
position| * |
shoots | shoots made in the draft year |
draft_g | games played in the draft year|
mp | Minutes Played in the draft year|
draft_fg | Field Goals in the draft year|
dga | Field Goal Attempts in the draft year|
3p | 3-Point Field Goals in the draft year|
3pa | 3-Point Field Goals Attempt in the draft year|
draft_ft | Free Throws in the draft year|
fta |Free Throws Attempt in the draft year|
orb | Offensive Rebouds in the draft year|
draft_trb | Total Rebounds in the draft year|
draft_ast | Assits in the draft year|
draft_stl | Steals in the draft year|
draft_blk | Blocks in the draft year|
draft_tov | Turnovers in the draft year|
draft_pf | Personal Fouls in the draft year|
draft_pts | Points in the draft year|
mp_per | Minutes Played per game in the draft year|
pts_per |Points per game in college|
trb_per | Total Rebounds per game in college|
asb_per | Assist per game in college|
amature_honor | NCAA all_American(1, 0)|
raw_data | If the player college stats exists, the value is 1, otherwise, is 0 |

+ Evaluation Metrics: Overall Pick(pk)

+ Response Variables: NBA stats

Field | Explanation|
--------- | ----------- |
career_g | games played in player's NBA career|
Career PER | A measure for player's per-minute performance, while adjusting for pace. A league-average PER is always 15.00, which permits comparisons of player performance across seasons.|
WinShare(WS) |  an estimate of the number of wins contributed by a player|
Career_WS/48 | an estimate of the number of wins contributed by a player per 48 minutes |


+ Reference Paper: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/The%20Success%20of%20NBA%20Draft%20Picks-%20Can%20College%20Careers%20Predict%20NBA%20W.pdf

Full original datasets: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/NBA_original_datasets.csv
Full normalized datasets: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/joined_norm_drafted_NBA_player.csv
Nomalized datasets after exclusing players whose college stats is not available: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/joined_norm_drafted_NBA_player_having_NCAA.csv















