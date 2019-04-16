from tkinter import *
import os
import glob

gui=Tk()
mb=  Menubutton ( gui, text="Courses", relief=RAISED )
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu


def print_courses(*args):
   values = [(file_name, var.get()) for file_name, var in courses.items()]
   print (values)


course_path=os.path.join(os.getcwd(),'..','Courses\\')
courses={}
for excel_file in glob.glob(course_path+"*.xlsx"):
	#print(excel_file)
	file_name=os.path.splitext(os.path.basename(excel_file))[0] #First we extract name of the file from path. Then we remove the .xlsx extension
	#print(file_name)
	var=IntVar()
	mb.menu.add_checkbutton(label=file_name, variable=var)
	courses[file_name]=var

btn = Button(gui, text="Print", command=print_courses)
btn.pack()

mb.pack()

gui.mainloop()