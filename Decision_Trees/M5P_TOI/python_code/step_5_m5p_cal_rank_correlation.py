
import mysql.connector
import os
import csv

from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(('rcg-linux-ts1.rcg.sfu.ca', 22),
                        ssh_username = "cla315",
                        ssh_password="******",
                        remote_bind_address=('cs-oschulte-01.cs.sfu.ca', 3306)) as server:

    #connect to database server
    mydb = mysql.connector.connect(host='127.0.0.1',
                                   port = server.local_bind_port,
                                   user='root', passwd='joinbayes',
                                   db='chao_draft')
    cursor = mydb.cursor()

    output_list = []

    for year in [2001, 2002, 2007, 2008]:

        cursor.execute("""Drop view if exists chao_draft.cal_m5p_rank_corr_CSS_null_norm_TOI_%s_view;""" % str(year))
        mydb.commit()
        cursor.execute("""Create view chao_draft.cal_m5p_rank_corr_CSS_null_norm_TOI_%s_view as
                    SELECT id, PlayerName, DraftYear, rank_sum_7yr_TOI, 
                    skaters_overall, pow(skaters_overall-rank_sum_7yr_TOI, 2) as di2_overall,          
                    rank_m5p_notie, pow(rank_m5p_notie - rank_sum_7yr_TOI, 2) as di2_m5p_notie,
                    rank_m5p_tied, pow(rank_m5p_tied - rank_sum_7yr_TOI, 2) as di2_m5p_tied,
                    rank_m5p_nonzero, pow(rank_m5p_nonzero - rank_sum_7yr_TOI, 2) as di2_m5p_nonzero
                  FROM chao_draft.union_all_ranks_with_m5p_TOI_view
                  WHERE DraftYear = %s;""" % (str(year), str(year)))
        mydb.commit()

        cursor.execute("""select count(*), sum(di2_overall), sum(di2_m5p_notie), 
                                                    sum(di2_m5p_tied), sum(di2_m5p_nonzero)
                        from chao_draft.cal_m5p_rank_corr_CSS_null_norm_TOI_%s_view;""" % str(year))
        #mydb.commit()
        print 'Draft year: %s' % str(year)
        row = cursor.fetchone()
        print str(row)
        total_num = int(row[0])
        overall_rank_corr = float(1 - 6 * float(row[1])/(float(total_num) * (pow(total_num, 2) - 1)))
        print 'Overall rank corr. = ' + str(overall_rank_corr)
        m5p_rank_notie_corr = float(1 - 6 * float(row[2]) / (float(total_num) * (pow(total_num, 2) - 1)))
        print 'm5p_rank_notie rank corr. = ' + str(m5p_rank_notie_corr)
        m5p_rank_tied_corr = float(1 - 6 * float(row[3]) / (float(total_num) * (pow(total_num, 2) - 1)))
        print 'm5p_rank_tied corr. = ' + str(m5p_rank_tied_corr)
        m5p_rank_nonzero_corr = float(1 - 6 * float(row[4]) / (float(total_num) * (pow(total_num, 2) - 1)))
        print 'm5p_rank_nonzero corr. = ' + str(m5p_rank_nonzero_corr)

        cursor.execute("""Drop view if exists chao_draft.cal_m5p_rank_corr_CSS_null_norm_TOI_%s_view;""" % str(year))
        mydb.commit()

        output_dict = {'DraftYear': year, 'Overall_rank_corr': overall_rank_corr,
                       'm5p_rank_notie_corr': m5p_rank_notie_corr, 'm5p_rank_tied_corr': m5p_rank_tied_corr,
                       'm5p_rank_nonzero_corr': m5p_rank_nonzero_corr}
        output_list.append(output_dict)

    fieldNames = ['DraftYear','Overall_rank_corr', 'm5p_rank_notie_corr', 'm5p_rank_tied_corr', 'm5p_rank_nonzero_corr']

    with open("m5p_TOI_rank_correlation_calculation.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(output_list)

    cursor.close()
    print "Rank correlation has been calculated."
