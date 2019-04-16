from flask import Flask, render_template,url_for,request,session,redirect
import os
import glob
import data_aggregator as da

courses={}
to_update={}

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def options():
	course_path=os.path.join(os.getcwd(),'..','Courses\\')
	for excel_file in glob.glob(course_path+"*.xlsx"):
		file_name=os.path.splitext(os.path.basename(excel_file))[0] #First we extract name of the file from path. Then we remove the .xlsx extension
		courses[file_name]=excel_file
	return render_template('courses.html',courses=courses)

@app.route('/parse_data',methods=['GET','POST'])
def parse_data():
	print("parse data called")
	selected=request.args.getlist('course_box')
	for option in selected:
		if option in courses:
			to_update[option]=courses[option]
	print(to_update)
	for file_name in to_update:
		excel_file=to_update[file_name]
		da.getLinks(excel_file,file_name)

	return 'Done'
if __name__ == '__main__':
	app.secret_key='mysecret'
	app.run(debug=True)
