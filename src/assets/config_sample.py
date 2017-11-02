tokens = {
  'ssh_user_name': 'patrick',
  'ssh_pass_word': 'patrick password',
  'ssh_host_name': 'ssh host',
  'ssh_port': 22,
  'mysql_host_name': 'mysql host',
  'mysql_server_port': 3306,
  'mysql_user_name': 'username',
  'mysql_pass_word': 'password'
}
DB_NAME = 'chao_draft'
TABLE_NAME = 'AHL_NHL_norm_2'
NORMALIZE_COLUMNS = [
  'sum(G)',
  'sum(A)',
  'sum(P)',
  'sum(PlusMinus)',
  'sum(PIM)',
  'sum(PointPerGame)',
  'sum(PPG)',
  'sum(PPP)',
  'sum(SHG)',
  'sum(SHP)',
  'sum(GWG)',
  'sum(OTG)',
  'sum(S)',
  'sum(ShootingPercentage)',
  'sum(NHL_TOIPerGame_sec)',
  'sum(ShiftsPerGame)',
  'sum(FaceoffWinPercentage)']
