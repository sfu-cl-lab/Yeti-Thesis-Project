
### NHL(season 2016-2017) -> AHL(season 2016-2017):

+ Datasets: 
    ```
    select AHL_playerID, NHL_playerId, PlayerName, NHL_season, NHL_team, Position, sum(GP), sum(G), sum(A), sum(P), 
    sum(PlusMinus), sum(PIM), sum(PointPerGame), sum(PPG), sum(PPP), sum(SHG), sum(SHP), 
    sum(GWG), sum(OTG), sum(S), sum(ShootingPercentage),
    sum(NHL_TOIPerGame_sec), sum(ShiftsPerGame), sum(FaceoffWinPercentage), AHL_GP, AHL_total_TOI, AHL_goals, AHL_shots
    from chao_draft.AHL_NHL_16_17_unique_players group by PlayerName;
    ```

+ Preprocessing:
  <ul>
  <li>convert AHL_total_TOI to seconds</li>
  <li>normalize fields sum(GP), sum(G), sum(A), sum(P), 
      sum(PlusMinus), sum(PIM), sum(PointPerGame), sum(PPG), sum(PPP), sum(SHG), sum(SHP), sum(GWG), sum(OTG), sum(S), sum(ShootingPercentage), sum(NHL_TOIPerGame_sec), sum(ShiftsPerGame), sum(FaceoffWinPercentage)
 </li>
 </ul>

+ Result table stored in **chao_draft.AHL_NHL_norm_0**, also saved in folder **AHL_NHL_16_17/norm_16_17_NHL_to_16_17_AHL.csv**. 

### AHL(season 2016_2017) -> NHL(season 2016_2017):

[OS?? do you mean AHL(season 2016_2017) -> NHL(season 2016_2017) yes, sorry]
+ Datasets:
  ```
  SELECT AHL_playerID, NHL_playerId, PlayerName, NHL_season, AHL_GP, AHL_total_TOI, ev_icetime, AHL_goals, primary_assists, secondary_assists, ev_goals, ev_primary_assists, ev_secondary_assists, AHL_shots, ev_shots, passes, ev_passes, ze_controlled_entry, ze_uncontrolled_entry, ze_controlled_exit, ze_uncontrolled_exit, penalties_taken, penalties_drawn, team_ev_shots_for, team_ev_shots_against, sum(GP), sum(G), sum(A), sum(P), sum(S), sum(NHL_TOIPerGame_sec)
  FROM chao_draft.AHL_NHL_16_17_unique_players
  group by PlayerName;
  ```

+ Preprocessing:
  <ul>
  <li>convert AHL_total_TOI to seconds</li>
  <li>normalize fields AHL_GP, AHL_total_TOI, ev_icetime, AHL_goals, primary_assists, secondary_assists, ev_goals, ev_primary_assists, ev_secondary_assists, AHL_shots, ev_shots, passes, ev_passes, ze_controlled_entry, ze_uncontrolled_entry, ze_controlled_exit, ze_uncontrolled_exit, penalties_taken, penalties_drawn, team_ev_shots_for, team_ev_shots_against
  </li>
  </ul>
  
+ Result table stored in **chao_draft.AHL_NHL_norm_1**, also saved in folder **AHL_NHL_16_17/norm_16_17_AHL_to_16_17_NHL.csv**. [OS: I don't see it. Do you mean [this file](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/AHL_seasons_players/AHL_NHL_16_17/norm_16_17_AHL_to_16_17_NHL.csv)? yes]

### NHL(season 2007_2008 - season 2016_2017, sum all seasons) -> AHL(season 2016_2017)
+ Datasets:
    ```
    select AHL_playerID, NHL_playerId, PlayerName, Position, sum(GP), sum(G), sum(A), sum(P), sum(PlusMinus), sum(PIM), 
    sum(PointPerGame), sum(PPG), sum(PPP), sum(SHG), sum(SHP), sum(GWG), sum(OTG), sum(S), 
    sum(ShootingPercentage), sum(NHL_TOIPerGame_sec), sum(ShiftsPerGame), sum(FaceoffWinPercentage),
    AHL_GP, AHL_total_TOI, AHL_goals, AHL_shots
    from chao_draft.AHL_NHL_player_new group by PlayerName;
    ```

+ Preprocessing:
  <ul>
  <li>convert AHL_total_TOI to seconds</li>
  <li>normalize fields sum(GP), sum(G), sum(A), sum(P), sum(PlusMinus), sum(PIM), sum(PointPerGame), sum(PPG), sum(PPP), sum(SHG), sum(SHP), sum(GWG), sum(OTG), sum(S), sum(ShootingPercentage), sum(NHL_TOIPerGame_sec), sum(ShiftsPerGame), sum(FaceoffWinPercentage)</li>
  </ul>
  
+ Result table stored in **chao_draft.AHL_NHL_norm_2**, also saved in folder **AHL_NHL_16_17/norm_all_NHL_to_16_17_AHL.csv**

### Dataset used for Bayesian Network is stored in: ###
https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/AHL_seasons_players/AHL_NHL_16_17/AHL_NHL_BN.csv

### Sloan-Paper: NHL datasets with League information ###
+ NHL dataset with League information is stored in database: ### chao_draft.chao_draft.join_skaters_with_League_98_08_norm ### under 'cs-oschulte-01.sfu.ca' 
+ The dataset to produce the 2nd_cohort tree is got through
    ```
    select * from chao_draft.chao_draft.join_skaters_with_League_98_08_norm where DraftYear in (2004, 2005, 2006);
    ```
    Then we run it in weka, choosing excluding the po/rs_PlusMinus or not.











                  




            
                       


