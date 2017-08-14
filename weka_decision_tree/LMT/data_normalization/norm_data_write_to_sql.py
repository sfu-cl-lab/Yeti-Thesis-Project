import csv
import mysql.connector
import os
import shutil
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(('rcg-linux-ts1.rcg.sfu.ca', 22),
                        ssh_username = "cla315",
                        ssh_password="Life5uck5!",
                        remote_bind_address=('cs-oschulte-01.cs.sfu.ca', 3306)) as server:

    #connect to database server
    mydb = mysql.connector.connect(host='127.0.0.1',
                                   port = server.local_bind_port,
                                   user='root', passwd='joinbayes',
                                   db='chao_draft')
    cursor = mydb.cursor()

    # comment the following statements if table has been created

    cursor.execute("Drop table if exists chao_draft.join_skater_and_season_stats_10_years_CSS_null_norm;")

    mydb.commit()

    cursor.execute("""Create table chao_draft.join_skater_and_season_stats_10_years_CSS_null_norm
    (id INT, PlayerName VARCHAR(50), DraftAge_norm double, country_group VARCHAR(10), Height_norm double, 
    Weight_norm double, Position VARCHAR(5), DraftYear INT, Overall INT, CSS_rank_norm double, 
    rs_GP_norm double, rs_G_norm double, rs_A_norm double, rs_P_norm double, rs_PIM_norm double,
    rs_PlusMinus_norm double, po_GP_norm double, po_G_norm double, po_A_norm double, po_P_norm double, 
    po_PIM_norm double, po_PlusMinus_norm double, sum_7yr_GP INT, sum_7yr_TOI INT, GP_greater_than_0 VARCHAR(10));""")

    mydb.commit()

    # where unimported csv files are stored
    inputDir = "/Users/chao/GoogleDrive/2017-08-10-weka-data"
    # csv files will be moved to hear after being imported to database
    moveToDir = "/Users/chao/GoogleDrive/2017-08-10-weka-data"

    fileNameList = []
    for file in os.listdir(inputDir):
        if file.endswith("5_year_norm.csv"):
                    fileNameList.append(file)
    print "THe following csv files will be imported to the database."
    print(fileNameList)


    for fileName in fileNameList:
        with open(inputDir + "/" + fileName,'r')  as inputFile:
            csv_data = csv.reader(inputFile)
            #the following code avoids importing headers/1st row in each csv file
            firstLine = True
            for row in csv_data:
                if firstLine:
                    firstLine = False
                    continue
                cursor.execute("""INSERT INTO chao_draft.join_skater_and_season_stats_10_years_CSS_null_norm
                (id, PlayerName, DraftAge_norm, country_group, Height_norm, Weight_norm, Position, DraftYear, Overall, CSS_rank_norm,
                rs_GP_norm, rs_G_norm, rs_A_norm, rs_P_norm, rs_PIM_norm, rs_PlusMinus_norm, po_GP_norm, po_G_norm, po_A_norm, po_P_norm,
                 po_PIM_norm, po_PlusMinus_norm, sum_7yr_GP, sum_7yr_TOI, GP_greater_than_0) VALUES(%s, %s, %s, %s, %s,
                                        %s, %s, %s, %s, %s,
                                        %s, %s, %s, %s, %s,
                                        %s, %s, %s, %s, %s, 
                                        %s, %s, %s, %s, %s)""", row)
                mydb.commit()
                # now move the imported file to another folder
        shutil.move(inputDir + "/" + fileName, moveToDir + "/" + fileName)

    cursor.close()
    print "ALL CSV files in folder has been written to database."