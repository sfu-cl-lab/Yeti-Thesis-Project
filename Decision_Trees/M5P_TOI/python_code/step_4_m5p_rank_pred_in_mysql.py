
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
        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_notie;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_notie as
                            SELECT id, PlayerName, DraftYear, m5p_pred,
                            @prev := @curr,
                            @curr := round(m5p_pred, 16),
                            @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_m5p,
                            IF(@prev <> round(m5p_pred, 16), @i:=1, @i:=@i+1) AS counter
                          FROM chao_draft.m5p_10years_CSS_null_norm_TOI_pred,
                            (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                          where DraftYear = %s
                          order by m5p_pred DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp as
                    SELECT t1.id, t1.PlayerName, t1.DraftYear, t2.lmt_prob, m5p_pred, 
                    if((t2.lmt_prob < 0.5), -999, round(m5p_pred)) as m5p_pred_tied
                    FROM rank_m5p_pred_CSS_null_norm_TOI_%s_notie as t1 ,
                    chao_draft.rank_lmt_prob_CSS_null_norm_%s_notie as t2
                    where t1.id = t2.id 
                    order by lmt_prob DESC, m5p_pred DESC;""" % (str(year), str(year), str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_tied;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_tied as
                            SELECT id, PlayerName, DraftYear, lmt_prob, m5p_pred, m5p_pred_tied,
                            @prev := @curr,
                            @curr := m5p_pred_tied,
                            @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_m5p_tied,
                            IF(@prev <> m5p_pred_tied, @i:=1, @i:=@i+1) AS counter
                          FROM chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp,
                            (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                          order by m5p_pred_tied DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp;""" % str(year))
        mydb.commit()

        cursor.execute("""Create table chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp as
                    SELECT id, PlayerName, DraftYear, m5p_pred,
                    @prev := @curr,
                    @curr := m5p_pred,
                    @rank := IF(@prev = @curr, @rank, @rank + @i) AS rank_m5p_nonzero,
                    IF(@prev <> m5p_pred, @i:=1, @i:=@i+1) AS counter
                  FROM chao_draft.m5p_10years_nonzero_CSS_null_norm_TOI_pred,
                    (SELECT @curr := null, @prev := null, @rank:= 1, @i := 0) tmp_tbl
                  where DraftYear = %s
                  order by m5p_pred DESC;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""select max(rank_m5p_nonzero)
                          from chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp;""" % (str(year)))

        row = cursor.fetchone()
        bottom_rank = int(row[0]) + 1

        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_nonzero;""" % str(year))
        mydb.commit()
        cursor.execute("""Create table chao_draft.rank_m5p_pred_CSS_null_norm_TOI_%s_nonzero as
            SELECT t2.id, t2.PlayerName, t2.DraftYear, t2.lmt_prob, m5p_pred as m5p_pred_nonzero,
            if(rank_m5p_nonzero is null, %s, rank_m5p_nonzero) as rank_m5p_nonzero
            FROM chao_draft.rank_lmt_prob_CSS_null_norm_%s_notie as t2
            left join chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp as t1 
            on t1.id = t2.id 
            order by rank_m5p_nonzero ASC, lmt_prob DESC;""" % (str(year), str(bottom_rank), str(year),str(year)))
        mydb.commit()

        cursor.execute("""Drop table if exists chao_draft.rank_m5p_pred_CSS_null_norm_%s_temp;""" % str(year))
        mydb.commit()

    cursor.execute("""Drop view if exists chao_draft.union_m5p_TOI_pred_view;""")
    mydb.commit()
    cursor.execute("""Create view chao_draft.union_m5p_TOI_pred_view as
                (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.m5p_pred as m5p_pred_notie, t1.rank_m5p as rank_m5p_notie,
                t2.lmt_prob, t2.m5p_pred_tied, t2.rank_m5p_tied, t3.m5p_pred_nonzero, t3.rank_m5p_nonzero
                FROM chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2001_notie as t1,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2001_tied as t2,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2001_nonzero as t3
                where t1.id = t2.id and t1.id = t3.id
                order by t3.rank_m5p_nonzero ASC, t2.lmt_prob DESC)
                UNION
                (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.m5p_pred as m5p_pred_notie, t1.rank_m5p as rank_m5p_notie,
                t2.lmt_prob, t2.m5p_pred_tied, t2.rank_m5p_tied, t3.m5p_pred_nonzero, t3.rank_m5p_nonzero
                FROM chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2002_notie as t1,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2002_tied as t2,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2002_nonzero as t3
                where t1.id = t2.id and t1.id = t3.id
                order by t3.rank_m5p_nonzero ASC, t2.lmt_prob DESC)
                UNION
                (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.m5p_pred as m5p_pred_notie, t1.rank_m5p as rank_m5p_notie,
                t2.lmt_prob, t2.m5p_pred_tied, t2.rank_m5p_tied, t3.m5p_pred_nonzero, t3.rank_m5p_nonzero
                FROM chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2007_notie as t1,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2007_tied as t2,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2007_nonzero as t3
                where t1.id = t2.id and t1.id = t3.id
                order by t3.rank_m5p_nonzero ASC, t2.lmt_prob DESC)
                UNION
                (SELECT t1.id, t1.PlayerName, t1.DraftYear, t1.m5p_pred as m5p_pred_notie, t1.rank_m5p as rank_m5p_notie,
                t2.lmt_prob, t2.m5p_pred_tied, t2.rank_m5p_tied, t3.m5p_pred_nonzero, t3.rank_m5p_nonzero
                FROM chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2008_notie as t1,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2008_tied as t2,
                chao_draft.rank_m5p_pred_CSS_null_norm_TOI_2008_nonzero as t3
                where t1.id = t2.id and t1.id = t3.id
                order by t3.rank_m5p_nonzero ASC, t2.lmt_prob DESC);""")
    mydb.commit()

    cursor.execute("""Drop view if exists chao_draft.union_all_ranks_with_m5p_TOI_view;""")
    mydb.commit()
    cursor.execute("""create view chao_draft.union_all_ranks_with_m5p_TOI_view as
                select t1.*, t2.m5p_pred_notie, t2.rank_m5p_notie,t2.lmt_prob, t2.m5p_pred_tied, t2.rank_m5p_tied,
                t2.m5p_pred_nonzero, t2.rank_m5p_nonzero
                from chao_draft.union_overall_GP_TOI_1278_VIEW as t1,
                chao_draft.union_m5p_TOI_pred_view as t2              
                where t1.id = t2.id
                order by t1.DraftYear ASC, t2.rank_m5p_nonzero ASC, t2.lmt_prob DESC;""")
    mydb.commit()


#merge with 4a later


    cursor.close()
    print "Rank tables have been created."
