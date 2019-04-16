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
today=datetime.datetime.date(datetime.datetime.now())


output_path=os.path.join(os.getcwd(),'..','outputs\\',str(today)+'\\')
if not os.path.exists(output_path):
	os.makedirs(output_path)

print(output_path)

#URL of the API
url="https://newsapi.org/v2/everything?"

def getSingularLink(text):
	#print("Called")
	params={'q':text,'sortBy':'popularity','language':'en','apiKey':'78360a231a534cf78fbb2b234b68e333','pageSize':'10'}
	results=requests.get(url,params=params)
	#print(results.url)
	#pprint.pprint(results.json())
	return results
	

def getLinks(excel_file,file_name):
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
		
		if(1):
			out_csv= open(file,'w')

			
			file_writer=csv.writer(out_csv,delimiter=',')

			try:
				for i in range(sheet.nrows):
					print(sheet.cell_value(i,0))
					field=sheet.cell_value(i,0)
					result=getSingularLink(field)
					jsonfile=result.json()
					#pprint.pprint(jsonfile,indent=4)
					jsonfile=jsonfile['articles']
					#pprint.pprint(jsonfile,indent=4)
					for data_items in jsonfile:
						url=data_items['url']
						r=requests.get(url)
						if (r.status_code == requests.codes.ok):
							row_to_add=[]
							row_to_add.append(field)
							row_to_add.append(data_items['title'])
							row_to_add.append(data_items['url'])
							row_to_add.append(data_items['description'])
							file_writer.writerow(row_to_add)
							#file_writer.writerow("")
							print(field)
							print(row_to_add)

						else:
							print("DEAD URL", url)

					file_writer.writerow("")
			except:
				print('Error')
				pass

			return


if __name__ == '__main__':
	getLinks("C:\\Users\\Arpit\\Desktop\\Collegepond\\code\\..\\Courses\\Software Engineering.xlsx","Software Engineering")