a# Yeti-Thesis-Project
 for my thesis--Yejia Liu

# Notes on Data

## David Wilson's dataset 

 + contains boxscores for each player's first seven years.
 + goes from 1998-2011
 + total number of players is 3,076.
     + Note: there are two "Sean Collins". Only one of them can be found in Kurt's data.
 + includes players with 0 NHL games
 + stored in ckm_and_exception_mining.SevenSeasons_wilson on cs-oschulte-01
 
 ## Kurt Routley's dataset
 
 + crawled from web (which site?)
 + originally contained in where?, now copied to draft_master_table1
 + goes from draft year 1998-2008
 + total number of players = 1097 (only players with > 0 NHL games)
     + Note: there are two "Alexandre Picard" and two "Mikko Lehtonen". Only one of each can be found in Wilson's data
 
 The join of Wilson + routley is contained in draft_master_table2 (nice to rename like "Wilson_Routley")
 
## Chao Li's dataset

+ adds central scouting services rank (CSS) for Kurt's 1097 players
+ crawled [draftanalyst.com]
+ eliminated 2 duplicates, i.e. PlayerId = 8470678 & 8469714
+ total number of players 1095
+ contained in two views
  + ckm_and_exception_mining.NHL_playerStats_1998_2008_view (player features only)
      + the above view is join of Wilson + Routley on player name and draft number
  + ckm_and_exception_mining.NHL_seasonInfo_1998_2008_view  (2772 rows in total)
+ changed the column names in ckm_and_exception_mining.NHL_seasonInfo_1998_2008_view, such as "CareerGP", "CareerG", etc. into "GP", "G", etc. as these values correspond to a particular seaon type and a particular team for a specific player. With such a name change, a new view is created as    
  + chao_draft.NHL_seasonInfo_1998_2008_duplicates_view
+ deleted columns named "S" and "shotPercentage" as these values are all zeros
+ deleted rows with GP =0, G=0, A=0, P=0, etc. for both season types (i.e. Regualar/Playeroffs)
+ deleted rows with false team names for PlayerId = 8467514 &  8470828
+ modified rows with duplicate Team names for PlayerId = 8468597
  + above changed were made and saved as chao_draft.NHL_seasonInfo_1998_2008 (2644 rows in total)
  
