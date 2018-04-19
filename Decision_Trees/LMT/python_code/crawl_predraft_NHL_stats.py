import csv
import traceback
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unicodedata
import time
import os
import sys
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

# if use linux server
def find_chrome():
	chromedriver = "/home/cla315/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	chrome_options = Options()
	chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2,
													 'profile.managed_default_content_settings.images': 2 })
	driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
	return driver

def jump2search(driver, playerUrl):
	t = time.time()
	try:
		driver.get(playerUrl)
		driver.implicitly_wait(300)
	except TimeoutException:
		print 'Couldn\'t load this page.'
		print "Time consuming: " + str(t)
	print "Time consuming: " + str(t)
	return driver

def get_store_directory(draftYr):
	data_directory = "/home/cla315/work_yeti/elite_prospect/playerstats_txtfiles/players_stats_" + draftYr + ".txt"
	return data_directory

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


def crawl_data(txt_file, driver):
	data_record = []
	demographic_dict = {}
	position_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]'
	position = driver.find_element_by_xpath(position_xpath).text
	position = unicodedata.normalize('NFKD', position).encode('ascii', 'ignore')
	if position == 'G':
		print 'This is a goal tender, jump to the next player.'
		return
	demographic_dict = record_dict_value(demographic_dict, "Position", position)

	elite_id_xpath = '/html/head/meta[6]'
	elite_id = driver.find_element_by_xpath(elite_id_xpath).get_attribute("content")
	elite_id = unicodedata.normalize('NFKD', elite_id).encode('ascii', 'ignore')
	elite_id = elite_id.split('player=')
	elite_id = elite_id[1]
	demographic_dict = record_dict_value(demographic_dict, "eliteId", elite_id)

	name_xpath = '//*[@id="fontHeader"]'
	name = driver.find_element_by_xpath(name_xpath).text
	name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
	print 'Player name is ' + name
	demographic_dict = record_dict_value(demographic_dict, "PlayerName", name)

	born_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/a'
	born = driver.find_element_by_xpath(born_xpath).get_attribute('href')
	born = unicodedata.normalize('NFKD', born).encode('ascii', 'ignore')
	born = born.split('Birthdate=')
	born = born[1].split('&')
	born = born[0]
	demographic_dict = record_dict_value(demographic_dict, "BirthDate", born)

	try:
		birthplace_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td[4]/a'
		birthplace = driver.find_element_by_xpath(birthplace_xpath).text
		birthplace = unicodedata.normalize('NFKD', birthplace).encode('ascii', 'ignore')
	except:
		birthplace = "Null"
		print "Null birthplace found."
	demographic_dict = record_dict_value(demographic_dict, "Birthplace", birthplace)

	nation_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[2]/td[4]/a'
	nation = driver.find_element_by_xpath(nation_xpath).text
	nation = unicodedata.normalize('NFKD', nation).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "Nation", nation)

	shoots_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[3]/td[4]'
	shoots = driver.find_element_by_xpath(shoots_xpath).text
	shoots = unicodedata.normalize('NFKD', shoots).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "Shoots", shoots)

	height_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td[2]'
	height = driver.find_element_by_xpath(height_xpath).text
	height = unicodedata.normalize('NFKD', height).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "Height", height)

	weight_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[4]/td[4]'
	weight = driver.find_element_by_xpath(weight_xpath).text
	weight = unicodedata.normalize('NFKD', weight).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "Weight", weight)

	draftYear_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a'
	draftYear = driver.find_element_by_xpath(draftYear_xpath).text
	draftYear = unicodedata.normalize('NFKD', draftYear).encode('ascii', 'ignore')
	draftYear = draftYear[:4]
	demographic_dict = record_dict_value(demographic_dict, "draftYear", draftYear)

	draftRound_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a/strong[1]'
	draftRound = driver.find_element_by_xpath(draftRound_xpath).text
	draftRound = unicodedata.normalize('NFKD', draftRound).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "draftRound", draftRound)

	overall_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a/strong[2]'
	overall = driver.find_element_by_xpath(overall_xpath).text
	overall = unicodedata.normalize('NFKD', overall).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "Overall", overall)

	overallBy_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[6]/td[2]/a/b'
	overallBy = driver.find_element_by_xpath(overallBy_xpath).text
	overallBy = unicodedata.normalize('NFKD', overallBy).encode('ascii', 'ignore')
	demographic_dict = record_dict_value(demographic_dict, "overallBy", overallBy)


	label_xpath = '//*[@id="fontSmall"]'
	label = driver.find_element_by_xpath(label_xpath).text
	label = unicodedata.normalize('NFKD', label).encode('ascii', 'ignore')
	if label == "YOUTH TEAM":
		youth_team_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/p/table[2]/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/a'
		youth_team = driver.find_element_by_xpath(youth_team_xpath).text
		youth_team = unicodedata.normalize('NFKD', youth_team).encode('ascii', 'ignore')
	else:
		youth_team = 'Null'
	demographic_dict = record_dict_value(demographic_dict, "youthTeam", youth_team)
	print 'Demographic info has been read.'

	# the following code find all field names for a season
	field_name_dict = {1:'Team', 2:'League', 3:'Reg_GP', 4:'Reg_G', 5:'Reg_A', 6:'Reg_TP', 7:'Reg_PIM',
					   8:'Reg_PlusMinus', 10: 'Post', 11:'Play_GP', 12:'Play_G', 13:'Play_A',
					   14:'Play_TP', 15:'Play_PIM', 16:'Play_PlusMinus'}

	table_xpath = '/html/body/div[2]/table[3]/tbody/tr/td[5]/table[1]/tbody'
	table = driver.find_element_by_xpath(table_xpath)
	# find all row elements in the table
	all_rows = table.find_elements_by_tag_name('tr')
	field_name_row = True
	last_season = ""
	for row in all_rows:
		data_record_dict = dict(demographic_dict)
		# skip the first row in the table: the field names
		if field_name_row:
			field_name_row = False
			continue
		# find all columns elements for each row
		cols = row.find_elements_by_tag_name('td')
		season = cols[0].text
		season = unicodedata.normalize('NFKD', season).encode('ascii', 'ignore')
		# print "what's in the blank????????" + season + '????????'
		if season != " ":
			last_season = season
			print "Current season is " + season
		else:
			season = last_season
			print "The season of this row is blank. Set season to be last season " + season

		yearList = season.split("-")
		yearStr = yearList[0]
		if int(yearStr) >= int(draftYear):
			print 'Season is out of range, go to the next player.'
			break
		if int(yearStr) < int(draftYear)-1:
			print 'Not the target year yet, keep moving down.'
			continue
		# now it's the season we want to record
		data_record_dict = record_dict_value(data_record_dict, 'Season', season)
		try:
			for col_num in field_name_dict.keys():
				field_value = cols[col_num].text
				field_value = unicodedata.normalize('NFKD', field_value).encode('ascii', 'ignore')
				data_record_dict = record_dict_value(data_record_dict, field_name_dict[col_num], field_value)
			print "Season record to be saved is: " + str(data_record_dict)
			data_record.append(data_record_dict)
		except IndexError:
			break

	for data_record_line in data_record:
		# print 'Is the record written to txt files????'
		txt_file.write(str(data_record_line))
		txt_file.write("\n")

def start_crawl(inputDir, moveToDir):
	fileNameList = []
	for file in os.listdir(inputDir):
		if file.endswith(".csv"):
			fileNameList.append(file)
	print "The following csv files will be imported to the database." + fileNameList[0]

	for fileName in fileNameList:
		draftYear = fileName[-8:-4]

		print 'Draft year is ' + draftYear
		data_directory = get_store_directory(draftYear)

		with open(inputDir + "/" + fileName, 'r') as inputFile:
			csv_data = csv.reader(inputFile)
			# the following code avoids importing headers/1st row in each csv file
			firstLine = True
			for row in csv_data:
				if firstLine:
					firstLine = False
					continue
				player_url = row[1]
				chrome_driver = find_chrome()
				driver = jump2search(chrome_driver, player_url)

				if os.path.exists(data_directory):
					with open(data_directory, "a") as txt_file:
						crawl_data(txt_file, driver)
				else:
					with open(data_directory, "w") as txt_file:
						crawl_data(txt_file, driver)
				chrome_driver.close()
		shutil.move(inputDir + "/" + fileName, moveToDir + "/" + fileName)

if __name__ == '__main__':
	input_dir = "/home/cla315/work_yeti/elite_prospect/url_csv_files"
	moveto_dir = "/home/cla315/work_yeti/elite_prospect/url_csv_files_old"
	start_crawl(input_dir, moveto_dir)