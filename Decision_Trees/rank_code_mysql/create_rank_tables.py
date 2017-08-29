
import mysql.connector
import os

from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(('rcg-linux-ts1.rcg.sfu.ca', 22),
                        ssh_username = "cla315",
                        ssh_password = "******",
                        remote_bind_address=('cs-oschulte-01.cs.sfu.ca', 3306)) as server:

    #connect to database server
    mydb = mysql.connector.connect(host='127.0.0.1',
                                   port = server.local_bind_port,
                                   user='root', passwd='joinbayes',
                                   db='chao_draft')
    cursor = mydb.cursor()

    for year in [2001, 2002, 2007, 2008]:
        cursor.execute("""Drop table if exists chao_draft.rank_sum_7yr_GP_%s;""" % str(year))
        mydb.commit()
        cursor.execute("""create table chao_draft.rank_sum_7yr_GP_%s as
                        select id, PlayerName, DraftYear, sum_7yr_GP,
                        @prev := @curr,
                        @curr := sum_7yr_GP,
                        @rank := if(@prev = @curr, @rank, @rank + @i) AS rank_sum_7yr_GP,
                        if(@prev <> sum_7yr_GP, @i:=1, @i:=@i+1) AS counter
                        from chao_draft.join_skater_and_season_stats_10_years_CSS_null,
                        (select @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                        where DraftYear = %s
                        order by sum_7yr_GP DESC;""" % (str(year), str(year)))

        cursor.execute("""Drop table if exists chao_draft.rank_sum_7yr_TOI_%s;""" % str(year))
        mydb.commit()
        cursor.execute("""create table chao_draft.rank_sum_7yr_TOI_%s as
                        select id, PlayerName, DraftYear, sum_7yr_TOI,
                        @prev := @curr,
                        @curr := sum_7yr_TOI,
                        @rank := if(@prev = @curr, @rank, @rank + @i) AS rank_sum_7yr_TOI,
                        if(@prev <> sum_7yr_TOI, @i:=1, @i:=@i+1) AS counter
                        from chao_draft.join_skater_and_season_stats_10_years_CSS_null,
                        (select @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                        where DraftYear = %s
                        order by sum_7yr_TOI DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rerank_overall_%s;""" % str(year))
        mydb.commit()

        cursor.execute("""create table chao_draft.rerank_overall_%s as
                        select id, PlayerName, DraftYear, Overall as original_overall,
                        @prev := @curr,
                        @curr := Overall,
                        @rank := if(@prev = @curr, @rank, @rank + @i) AS skaters_overall,
                        if(@prev <> Overall, @i:=1, @i:=@i+1) AS counter
                        from chao_draft.join_skater_and_season_stats_10_years_CSS_null,
                        (select @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                        where DraftYear = %s
                        order by Overall ASC""" % (str(year), str(year)))
        mydb.commit()

    cursor.close()
    print "Rank tables have been created."
