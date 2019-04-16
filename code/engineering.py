import csv
from urllib import parse
import datetime
import requests    
import os
import glob
import xlrd
import data_aggregator as da

#Getting path to Courses folder
course_path=os.path.join(os.getcwd(),'..','Courses\\')
print(course_path)


#Path of news websites
news_path=os.path.join(os.getcwd(),'..','publishers\\','engineering.csv')
links=[]
with open(news_path,encoding='utf8') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for name,link in readCSV:
		links.append(link)

link_query=""
for link in links:
	link_query=link_query+" OR "+"website.domainName:"+link



#Getting Excel Files for Engineering
for excel_file in glob.glob(course_path+"*Engineering*.xlsx"):
	file_name=os.path.splitext(os.path.basename(excel_file))[0] #First we extract name of the file from path. Then we remove the .xlsx extension
	da.getLinks(excel_file,file_name)