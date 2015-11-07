import sys
import Tkinter
import tkFileDialog
import pandas as pd

i = 0

filetypes = {1: "df = pd.read_csv(filename)", 2: "df = pd.read_excel(filename)",}

while i <= 0:
	
	quit_choice = 3
	
	print "Choose the number that corresponds to the file type that you will be opening: "
	print """
	1: CSV File 
	2: Excel 2003 File (XLS / XLSX)
	3: Exit FileGrabber
	"""
	type_choice = int(raw_input("> "))
	if type_choice == quit_choice:
		quit()
	else:
		for typ in filetypes:
			if type_choice == typ:
				check = True
				break
		if check == True:
			i += 1
		else:
			print "Invalid choice selected.  Please enter a valid option."
	
root = Tkinter.Tk() ; root.withdraw()

filename = tkFileDialog.askopenfilename(parent=root,title="FileGrabber (Beta)")
open_str = filetypes[type_choice]
exec open_str

print df
