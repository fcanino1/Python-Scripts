import sys
import Tkinter
import tkFileDialog
import pandas as pd

def DataGrabber():

	i = 0

	filetypes = {1: "df = pd.read_csv(filename)", 2: "df = pd.read_excel(filename,sheet)",3: "df = pd.read_html(filename)"}
	
	while i <= 0:
	
		quit_choice = 4
	
		print "Choose the number that corresponds to the file type that you will be opening: "
		print """
		1: CSV File 
		2: Excel 2003 File (XLS / XLSX)
		3: Webpage Table (HTML)
		4: Exit FileGrabber
		"""
		choice = int(raw_input("> "))
		if choice == quit_choice:
			quit()
		else:
			for typ in filetypes:
				if choice == typ:
					check = True
					break
				else:
					check = False
			if check == True:
				i += 1
			else:
				print "Invalid choice selected.  Please enter a valid option."
	
	root = Tkinter.Tk() ; root.withdraw()

	filename = tkFileDialog.askopenfilename(parent=root,title="DataGrabber v0.1")
	exec_str = filetypes[choice]
	exec exec_str

	return df

df = DataGrabber()

print df
print type(df)

