
import mysql.connector
import os

from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(('rcg-linux-ts1.rcg.sfu.ca', 22),
                        ssh_username = "cla315",
                        ssh_password="*******",
                        remote_bind_address=('cs-oschulte-01.cs.sfu.ca', 3306)) as server:

    #connect to database server
    mydb = mysql.connector.connect(host='127.0.0.1',
                                   port = server.local_bind_port,
                                   user='root', passwd='joinbayes',
                                   db='chao_draft')
    cursor = mydb.cursor()

    for year in [2001, 2002, 2007, 2008]:
        cursor.execute("""Drop table if exists chao_draft.rank_lmt_prob_CSS_null_norm_%s_notie;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_lmt_prob_CSS_null_norm_%s_notie as
                    SELECT id, PlayerName, DraftYear, lmt_prob,
                    @prev := @curr,
                    @curr := lmt_prob,
                    @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_lmt,
                    IF(@prev <> lmt_prob, @i:=1, @i:=@i+1) AS counter
                  FROM chao_draft.lmt_10years_CSS_null_norm_prob,
                    (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                  where DraftYear = %s
                  order by lmt_prob DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rank_lmt_prob_CSS_null_norm_%s_tied;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_lmt_prob_CSS_null_norm_%s_tied as
                            SELECT id, PlayerName, DraftYear, lmt_prob, rank_lmt as rank_lmt_tied
                          FROM chao_draft.rank_lmt_prob_CSS_null_norm_%s_notie
                          order by lmt_prob DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""select count(*) 
                        from chao_draft.rank_lmt_prob_CSS_null_norm_%s_tied
                        where lmt_prob >= 0.5;""" % str(year))
        #mydb.commit()
        row = cursor.fetchone()
        bottom_rank = int(row[0]) + 1

        cursor.execute("""update chao_draft.rank_lmt_prob_CSS_null_norm_%s_tied
                          set rank_lmt_tied = %d
                            where rank_lmt_tied > %d;""" % (str(year), bottom_rank, bottom_rank))
        mydb.commit()

        cursor.execute("""Drop view if exists chao_draft.rank_corr_lmt_prob_CSS_null_norm_%s_view;""" % str(year))
        mydb.commit()

    cursor.execute("""Drop view if exists chao_draft.union_lmt_prob_view;""")
    mydb.commit()
    cursor.execute("""Create view chao_draft.union_lmt_prob_view as
    (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.lmt_prob, t1.rank_lmt as rank_lmt_notie, t2.rank_lmt_tied
    FROM chao_draft.rank_lmt_prob_CSS_null_norm_2001_notie as t1,
    chao_draft.rank_lmt_prob_CSS_null_norm_2001_tied as t2
    where t1.id = t2.id 
    order by t1.rank_lmt)
    UNION
    (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.lmt_prob, t1.rank_lmt as rank_lmt_notie, t2.rank_lmt_tied
    FROM chao_draft.rank_lmt_prob_CSS_null_norm_2002_notie as t1,
    chao_draft.rank_lmt_prob_CSS_null_norm_2002_tied as t2
    where t1.id = t2.id 
    order by t1.rank_lmt)
    UNION
    (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.lmt_prob, t1.rank_lmt as rank_lmt_notie, t2.rank_lmt_tied
    FROM chao_draft.rank_lmt_prob_CSS_null_norm_2007_notie as t1,
    chao_draft.rank_lmt_prob_CSS_null_norm_2007_tied as t2
    where t1.id = t2.id 
    order by t1.rank_lmt)
    UNION
    (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.lmt_prob, t1.rank_lmt as rank_lmt_notie, t2.rank_lmt_tied
    FROM chao_draft.rank_lmt_prob_CSS_null_norm_2008_notie as t1,
    chao_draft.rank_lmt_prob_CSS_null_norm_2008_tied as t2
    where t1.id = t2.id 
    order by t1.rank_lmt);""")
    mydb.commit()

    cursor.execute("""Drop view if exists chao_draft.union_all_ranks_with_lmt_view;""")
    mydb.commit()
    cursor.execute("""create view chao_draft.union_all_ranks_with_lmt_view as
    select t1.*, t2.lmt_prob, t2.rank_lmt_notie, t2.rank_lmt_tied
    from chao_draft.union_overall_GP_TOI_1278_VIEW as t1,
    chao_draft.union_lmt_prob_view as t2
    where t1.id = t2.id
    order by t1.DraftYear, t2.rank_lmt_notie;""")
    mydb.commit()

    cursor.close()
    print "Rank table has been created."
