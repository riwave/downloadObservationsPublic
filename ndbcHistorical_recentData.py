# Download all the NDBC buoy data (historical/stdmet format) for the recent months (double-check the url links below). Usually goes until current last month
import urllib.request
import requests
import numpy as np
import os 
# to be run inside wave dir
nmonth=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# lndbc = open('list.txt')
lndbc = open('NDBC_historical_stdmet_list2.txt')
content = lndbc.readlines()
year=2019; lmo=10 # starting month available at http://www.ndbc.noaa.gov/data/stdmet/ , usually current month -3

for st in range(0,len(content)):
	# namest = str(content[st]).split('_')[-1].split('.')[0].lower()
	namest = str(content[st])[0:-1]
	# Pay attention the last month is in a different NDBC url format (lmo)!
	for month in range(1,lmo+3):
		if month<lmo:
			url = 'http://www.ndbc.noaa.gov/view_text_file.php?filename='+namest+repr(month)+repr(year)+'.txt.gz&dir=data/stdmet/'+nmonth[month-1]+'/'

			try:
				response = urllib.request.urlopen(url) 
			except :
				print(url+"   does not exist")
			else:

				data = response.read() 
				text = data.decode('utf-8')
				del data, response, url

				if len(text.splitlines()) >10:

					text_file = open('NDBC_historical_stdmet_'+namest.upper()+'_'+repr(year)+'.txt', "a")
					text_file.write(text)
					text_file.close()

				del text

		if month==lmo:
			url = 'http://www.ndbc.noaa.gov/data/stdmet/'+nmonth[month-1]+'/'+namest+'a'+repr(year)+'.txt.gz'
			os.system('wget '+url)
			os.system('gunzip '+namest+'a'+repr(year)+'.txt.gz')
			os.system('mv '+namest+'a'+repr(year)+'.txt NDBC_historical_stdmet_'+namest.upper()+'_'+str(month).zfill(2)+repr(year)+'.txt')

		elif month==lmo+1:
			url = 'http://www.ndbc.noaa.gov/data/stdmet/'+nmonth[month-1]+'/'+namest+'b'+repr(year)+'.txt.gz'
			os.system('wget '+url)
			os.system('gunzip '+namest+'b'+repr(year)+'.txt.gz')
			os.system('mv '+namest+'b'+repr(year)+'.txt NDBC_historical_stdmet_'+namest.upper()+'_'+str(month).zfill(2)+repr(year)+'.txt')

		elif month==lmo+2:
			url = 'https://www.ndbc.noaa.gov/data/stdmet/'+nmonth[month-1]+'/'+namest+'.txt'

			try:
				response = urllib.request.urlopen(url) 
			except :
				print(url+"   does not exist")
			else:

				data = response.read() 
				text = data.decode('utf-8')
				del data, response, url

				if len(text.splitlines()) >10:

					text_file = open('NDBC_historical_stdmet_'+namest.upper()+'_'+str(month).zfill(2)+repr(year)+'.txt', "a")
					text_file.write(text)
					text_file.close()

				del text


