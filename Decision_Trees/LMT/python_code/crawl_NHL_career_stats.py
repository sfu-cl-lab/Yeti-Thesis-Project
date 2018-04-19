import csv
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unicodedata
import time
import os
import sys
import os.path


def find_chrome():
    chromedriver = "/home/cla315/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    return driver


def record_dict_value(dict_record, key, value):
    try:
        if value == "":
            dict_record.update({key: "Null"})
        else:
            dict_record.update({key: value})
    except ValueError:
        print "empty value"
        dict_record.update({key: "Null"})
    return dict_record


def jump2search(driver, gametype, season):
	if gametype == 2:
		gametype_str = "Regular Season"
	elif gametype == 3:
		gametype_str = "Playoffs"
	print "Now start crawling for Season " + str(season) + "-" + str(season + 1) + " " + gametype_str
	season_str = str(season)+str(season+1)
	player_search_url = "http://www.nhl.com/stats/player?aggregate=0&gameType=" + str(gametype) + "&report=skatersummary&pos=S&reportType=season&seasonFrom=" + season_str + "&seasonTo=" + season_str + "&filter=gamesPlayed,gte,0&sort=playerName"
	driver.get(player_search_url)
	time.sleep(3)
	return driver


def get_store_directory(season, gametype):
	gametype_str=""
	if gametype == 2:
		gametype_str = "RegularSeason"
	elif gametype == 3:
		gametype_str = "Playoffs"
		
	data_directory = "/home/cla315/work_yeti/NHL_player_stats_season_by_season/" + str(season) +"_" + str(season+1) + "_" + gametype_str + ".txt"
	return data_directory


def crawl_data(txt_file, driver):

	row_path = '//*[@id="stats-page-body"]/div[3]/div/div/div/div/table/tbody[1]'
	num_pages_text =driver.find_element_by_xpath('//*[@id="stats-page-body"]/div[3]/div[2]/div/div[2]/span[2]/span').text
	num_pages_text = unicodedata.normalize('NFKD', num_pages_text).encode('ascii', 'ignore')
	total_num_pages = int(num_pages_text)
	print "Total number of pages to be crawled is " + str(total_num_pages)
	lastPage = True
	print 'check point 1'
	for page_num in range(0, total_num_pages):
		print 'check point 2'
	#go to that page
		data_record = []
		if lastPage:
			lastPage = False
		else:
			page_pointer = driver.find_element_by_xpath('//*[@id="stats-page-body"]/div[3]/div[2]/div/div[1]/button').click()
		curr_page_num = driver.find_element_by_xpath(
			'//*[@id="stats-page-body"]/div[3]/div[2]/div/div[2]/span[2]/div/input').get_attribute("value")
		curr_page_num = unicodedata.normalize('NFKD', curr_page_num).encode('ascii', 'ignore')
		print "Currently crawling page # " + curr_page_num

		total_num_rows = len(driver.find_elements_by_class_name('rt-tr-group'))
		print "Total number of rows on page # " + curr_page_num + " is " + str(total_num_rows)         # including blank rows

		row_path = '//*[@id="stats-page-body"]/div[3]/div[1]/div[3]'
		for row_num in range(1, total_num_rows + 1):
			data_record_dict = {}
			current_row_path = row_path + "/div[" + str(row_num) + "]"

			try:
				id_url_xpath = current_row_path + "/div/div[2]/div/a"
				id_url = driver.find_element_by_xpath(id_url_xpath).get_attribute("href")
			except:
				print "row number is " + str(row_num)
				break

			id_url = unicodedata.normalize('NFKD', id_url).encode('ascii', 'ignore')
			player_id = id_url[(len(id_url)-7):]
			print "player id is " + player_id
			data_record_dict = record_dict_value(data_record_dict, "PlayerID", player_id)

			player_name_xpath = current_row_path + "/div/div[2]/div/a"
			player_name = driver.find_element_by_xpath(player_name_xpath).text
			player_name = unicodedata.normalize('NFKD', player_name).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "PlayerName", player_name)

			season_xpath =  current_row_path + "/div/div[3]/div"
			season = driver.find_element_by_xpath(season_xpath).text
			season = unicodedata.normalize('NFKD', season).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "Season", season)

			team_xpath = current_row_path + "/div/div[4]"
			team = driver.find_element_by_xpath(team_xpath).text
			team = unicodedata.normalize('NFKD', team).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "Team", team)

			pos_xpath = current_row_path + "/div/div[5]"
			pos = driver.find_element_by_xpath(pos_xpath).text
			pos = unicodedata.normalize('NFKD', pos).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "Position",pos)

			gp_xpath = current_row_path + "/div/div[6]"
			gp = driver.find_element_by_xpath(gp_xpath).text
			gp = unicodedata.normalize('NFKD', gp).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "GP", gp)

			g_xpath =  current_row_path + "/div/div[7]"
			g = driver.find_element_by_xpath(g_xpath).text
			g = unicodedata.normalize('NFKD', g).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "G", g)

			a_xpath = current_row_path + "/div/div[8]"
			a = driver.find_element_by_xpath(a_xpath).text
			a = unicodedata.normalize('NFKD', a).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "A", a)

			p_xpath = current_row_path + "/div/div[9]"
			p = driver.find_element_by_xpath(p_xpath).text
			p = unicodedata.normalize('NFKD', p).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "P", p)

			pm_xpath = current_row_path + "/div/div[10]"
			pm = driver.find_element_by_xpath(pm_xpath).text
			pm = unicodedata.normalize('NFKD', pm).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "+/-", pm)

			pim_xpath = current_row_path + "/div/div[11]"
			pim = driver.find_element_by_xpath(pim_xpath).text
			pim = unicodedata.normalize('NFKD', pim).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "PIM", pim)

			pgp_xpath = current_row_path + "/div/div[12]/div"
			pgp = driver.find_element_by_xpath(pgp_xpath).text
			pgp = unicodedata.normalize('NFKD', pgp).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "P/GP", pgp)

			ppg_xpath =  current_row_path + "/div/div[13]"
			ppg = driver.find_element_by_xpath(ppg_xpath).text
			ppg = unicodedata.normalize('NFKD', ppg).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "PPG", ppg)

			ppp_xpath =  current_row_path + "/div/div[14]"
			ppp = driver.find_element_by_xpath(ppp_xpath).text
			ppp = unicodedata.normalize('NFKD', ppp).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "PPP", ppp)

			shg_xpath =  current_row_path + "/div/div[15]"
			shg = driver.find_element_by_xpath(shg_xpath).text
			shg = unicodedata.normalize('NFKD', shg).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "SHG", shg)

			shp_xpath =  current_row_path + "/div/div[16]"
			shp = driver.find_element_by_xpath(shp_xpath).text
			shp= unicodedata.normalize('NFKD', shp).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "SHP", shp)

			gwg_xpath =  current_row_path + "/div/div[17]"
			gwg = driver.find_element_by_xpath(gwg_xpath).text
			gwg = unicodedata.normalize('NFKD', gwg).encode('ascii', 'ignore')
			data_record_dict = record_dict_value(data_record_dict, "GWG", gwg)

			otg_xpath =  current_row_path + "/div/div[18]"
			otg = driver.find_element_by_xpath(otg_xpath).text
			otg = unicodedata.normalize('NFKD', otg).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "OTG", otg)

			s_xpath =  current_row_path + "/div/div[19]"
			s = driver.find_element_by_xpath(s_xpath).text
			s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')	
			data_record_dict =  record_dict_value(data_record_dict, "S", s)

			spercentage_xpath =  current_row_path + "/div/div[20]/div"
			spercentage = driver.find_element_by_xpath(spercentage_xpath).text
			spercentage = unicodedata.normalize('NFKD', spercentage).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "S%", spercentage)

			toigp_xpath =  current_row_path + "/div/div[21]/div"
			toigp = driver.find_element_by_xpath(toigp_xpath).text
			toigp = unicodedata.normalize('NFKD', toigp).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "TOI/GP", toigp)

			shifts_xpath =  current_row_path + "/div/div[22]/div"
			shifts = driver.find_element_by_xpath(shifts_xpath).text
			shifts = unicodedata.normalize('NFKD', shifts).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "Shifts/GP", shifts)

			fow_xpath =  current_row_path + "/div/div[23]/div"
			fow = driver.find_element_by_xpath(fow_xpath).text
			fow = unicodedata.normalize('NFKD', fow).encode('ascii', 'ignore')
			data_record_dict =  record_dict_value(data_record_dict, "FOW%", fow)

			data_record.append(data_record_dict)
			
		for data_record_line in data_record:
			txt_file.write(str(data_record_line))
			txt_file.write("\n")


def start_crawl(gameType, season):
	chrome_driver = find_chrome()
	search_page_driver = jump2search(chrome_driver, gameType, season)
			# jump2search(driver, gameType, season_num)
			# gameType = 2 for regular seasons, = 3 for playoffs
	data_directory = get_store_directory(season, gameType )
	if os.path.exists(data_directory):
		with open(data_directory, "a") as txt_file:
			crawl_data(txt_file, search_page_driver)
	else:
		with open(data_directory, "w") as txt_file:
			crawl_data(txt_file, search_page_driver)
	chrome_driver.close()

           

if __name__ == '__main__':
	for season in range (2014, 2015):
		for gameType in range (3,4):
			start_crawl(gameType, season)