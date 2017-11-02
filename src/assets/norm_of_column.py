# Author: Hao Xiangpeng
# Email: haoxiangpeng@hotmail.com
#
# Some tips about MySQL Workbench:
# after update database, don't forget add SQL_NO_CACHE key word to your query,
# for example:
# select SQL_NO_CACHE * from ...
# Shame on MySQL Workbench, they don't have fresh test.


# Usage:
# Edit the config_sample.py and rename to config.py
# Change the table name, columns to calculate.
# Then run!

import pymysql.cursors
from sshtunnel import SSHTunnelForwarder

try:
  from config import tokens, DB_NAME, TABLE_NAME, NORMALIZE_COLUMNS
except:
  print("No config file")


def normalize(column_name: str, cursor):
  sql_min_max = 'select min(`{column}`) as mmin, max(`{column}`) mmax from {table_name};'.format(
    column=column_name, table_name=TABLE_NAME)
  cursor.execute(sql_min_max)
  result = cursor.fetchone()
  max_value = result['mmax']
  min_value = result['mmin']
  interval = max_value - min_value
  sql_update_norm = 'update `{table_name}` set `{column}`=((`{column}`-{min})/{interval});'.format(
    column=column_name, min=min_value, interval=interval, table_name=TABLE_NAME
  )
  cursor.execute(sql_update_norm)
  # print(max_value, min_value)


def change_name(column_name: str, cursor):
  sql_change_name = 'ALTER TABLE `{table}` CHANGE COLUMN `{column_old}` `{column_new}` DOUBLE NULL DEFAULT NULL;'.format(
    table=TABLE_NAME, column_old=column_name, column_new=column_name.replace("sum(", "norm(")
  )
  cursor.execute(sql_change_name)


def normalize_all(cursor):
  for column in NORMALIZE_COLUMNS:
    normalize(column, cursor)
    # change_name(column, cursor)
  print("done")


def connect():
  with SSHTunnelForwarder(
      (tokens['ssh_host_name'], tokens['ssh_port']),
      ssh_username=tokens['ssh_user_name'],
      ssh_password=tokens['ssh_pass_word'],
      remote_bind_address=(tokens['mysql_host_name'], tokens['mysql_server_port']),
      local_bind_address=('127.0.0.1', 2333)
  ) as tunnel:
    mysql_conn = pymysql.connect(host='127.0.0.1',
                                 user=tokens['mysql_user_name'],
                                 password=tokens['mysql_pass_word'],
                                 port=2333,
                                 db=DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    cursor = mysql_conn.cursor()
    normalize_all(cursor)
    cursor.close()
    mysql_conn.commit()


def test_query(cursor):
  sql = "SELECT max(`sum(p)`) FROM chao_draft.AHL_NHL_norm_1;"
  cursor.execute(sql)
  result = cursor.fetchall()
  print(result)


if __name__ == '__main__':
  cursor = connect()
