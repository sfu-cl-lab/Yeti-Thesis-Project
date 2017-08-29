import csv
import mysql.connector
import os
import shutil
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

    # comment the following statements if table has been created


    # where unimported csv files are stored
    inputDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'
    # csv files will be moved to hear after being imported to database
    moveToDir = '/Users/chao/GoogleDrive/2017-08-10_lmt'

    output_list = []

    for year in [2001, 2002, 2007, 2008]:
        cursor.execute("""select count(*)
        from chao_draft.lmt_10years_CSS_null_norm_prob
        where DraftYear = %s and (
        (GP_greater_than_0 = 'yes' and lmt_prob >= 0.5) or
        (GP_greater_than_0 = 'no' and lmt_prob < 0.5) 
        );""" % str(year))
        row = cursor.fetchone()
        correct_num = float(row[0])
        cursor.execute("""select count(*)
                from chao_draft.lmt_10years_CSS_null_norm_prob
                where DraftYear = %s ;""" % str(year))
        row = cursor.fetchone()
        total_num = float(row[0])
        accuracy = correct_num/total_num
        print str(year) + " accuracy is " + str(accuracy)

        output_dict = {'DraftYear': year, 'correct_num': correct_num,
                       'total_num': total_num, 'accuracy': accuracy}
        output_list.append(output_dict)

    fieldNames = ['DraftYear', 'correct_num', 'total_num', 'accuracy']

    with open("lmt_accuracy_calculation.csv", 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldNames)
        dict_writer.writeheader()
        dict_writer.writerows(output_list)

    cursor.close()
    print "Accuracy has been calculated."