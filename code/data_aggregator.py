import os
import requests
import csv
from urllib import parse
import urllib
import xlrd
import pprint
import datetime

#Getting Api Key
key_path = os.path.join( os.getcwd(), '..', 'key.txt' )
print(key_path)
keyfile= open(key_path,'r')
api_key=keyfile.read()
print("Api Key: ",api_key)

d=datetime.datetime.today()


output_path=os.path.join(os.getcwd(),'..','outputs\\')

#URL of the API
base_url="https://api.newsriver.io/v2/search?query=" 

def getSingularLink(text,link_query):
	raw='language:EN AND title:"'+text+'"'  #Middle part of query
	query=raw+link_query			#Full query without encoding
	#print(query)
	enc=parse.quote(query)
	url=base_url+enc+"&sortBy=discoverDate&sortOrder=DESC&sortBy=_score&sortOrder=DESC&limit=5"
	result=requests.get(url,headers={
				"Authorization":api_key
				})
	return result


def getLinks(excel_file,file_name,link_query):
	output_file=file_name+d.strftime('%d_%m_%Y')+".csv"
	print(output_file)
	# To open Workbook 
	wb=xlrd.open_workbook(excel_file)
	sheet = wb.sheet_by_index(0)
	# For row 0 and column 0 
	sheet.cell_value(0,0)
	file=output_path+output_file
	if os.path.isfile(file):
		print(file," Exists")
		return
	else:
		out_csv= open(file,'w')

		
		file_writer=csv.writer(out_csv,delimiter=',')

		try:
			for i in range(sheet.nrows):
				print(sheet.cell_value(i,0))
				field=sheet.cell_value(i,0)
				result=getSingularLink(field,link_query)
				jsonfile=result.json()
				for data_items in jsonfile:
					row_to_add=[]
					row_to_add.append(field)
					row_to_add.append(data_items['title'])
					row_to_add.append(data_items['url'])
					file_writer.writerow(row_to_add)
					#file_writer.writerow("")
					print(field)
					print(row_to_add)

				file_writer.writerow("")
		except Error:
			print(Error)
			pass


		return


if __name__ == '__main__':
	getLinks("C:\\Users\\Arpit\\Desktop\\Collegepond\\code\\..\\Courses\\Software Engineering.xlsx","Software Engineering"," OR website.domainName:www.sciencedaily.com OR website.domainName:www.nature.com OR website.domainName:interestingengineering.com OR website.domainName:www.theengineer.co.uk OR website.domainName:www.bbc.com OR website.domainName:www.cnet.com OR website.domainName:www.cnn.com OR website.domainName:www.engadget.com OR website.domainName:www.extremetech.com OR website.domainName:www.livescience.com OR website.domainName:www.nytimes.com OR website.domainName:news.slashdot.org OR website.domainName:techcrunch.com OR website.domainName:www.wsj.com OR website.domainName:www.forbes.com OR website.domainName:www.pcmag.com OR website.domainName:www.wired.com OR website.domainName:www.ice.com OR website.domainName:news.mit.edu OR website.domainName:www.dnaindia.com OR website.domainName:www.chemengonline.com OR website.domainName:acme.com OR website.domainName:cen.acs.org OR website.domainName:advertise.engineering.com OR website.domainName:aerospaceengineering.aero")