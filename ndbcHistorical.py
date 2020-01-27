# Download all the NDBC buoy data (historical/stdmet format) for the years selected below
# https://www.ndbc.noaa.gov/rsa.shtml
# https://www.ndbc.noaa.gov/measdes.shtml
import urllib.request
import numpy as np

# lndbc = open('NDBC_historical_stdmet_list.txt')
lndbc = open('NDBC_historical_stdmet_list2.txt')
content = lndbc.readlines()

for st in range(0,len(content)):

	namest = str(content[st]).split()[0].lower()

	for year in range(1970,2019+1):

		url = 'http://www.ndbc.noaa.gov/view_text_file.php?filename='+namest+'h'+repr(year)+'.txt.gz&dir=data/historical/stdmet/'

		try:
			response = urllib.request.urlopen(url) 
		except :
			print(url+"   does not exist")
		else:

			data = response.read() 
			text = data.decode('utf-8')
			del data, response, url

			if len(text.splitlines()) >10:

				# text_file = open('NDBC_historical_stdmet_'+namest.upper()+'.txt', "a")
				text_file = open('NDBC_historical_stdmet_'+namest.upper()+'_'+repr(year)+'.txt', "a")
				text_file.write(text)
				text_file.close()

			del text


