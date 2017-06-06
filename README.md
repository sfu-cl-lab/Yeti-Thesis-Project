a# Yeti-Thesis-Project
 for my thesis--Yejia Liu

# Notes on Data

## David Wilson's dataset 

 + contains boxscores for each player's first seven years.
 + goes from 1998-2011
 + total number of players is 3,076.
 + includes players with 0 NHL games
 + stored in ckm_and_exception_mining.SevenSeasons_wilson on cs-oschulte-01
 
 ## Kurt Routley's dataset
 
 + crawled from web (which site?)
 + originally contained in where?, now copied to draft_master_table1
 + goes from draft year 1998-2008
 + total number of players = 1097 (only players with > 0 NHL games)
 
 The join of Wilson + routley is contained in draft_master_table2 (nice to rename like "Wilson_Routley")
 
## Chao Li's dataset

+ adds central scouting services rank (CSS) for Kurt's 1097 players
+ crawled [draftanalyst.com]
+ eliminated 2 duplicates
+ total number of players 1095
+ contained in two views
  + ckm_and_exception_mining.NHL_playerStats_1998_2008_view (player features only)
  + ckm_and_exception_mining.NHL_playerStats_1998_2008_view
