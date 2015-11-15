import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_bn_data():

	pieces = []
	columns = ['name','sex','births']
	years = range(1880,2011)

	for year in years:
		path = 'names\yob%d.txt' % year
		frame = pd.read_csv(path, names = columns)
		
		frame['year'] = year
		pieces.append(frame)

	data = pd.concat(pieces,ignore_index=True)
	return data

def add_prop(group):
	# Integer division floors
	births = group.births.astype(float)
	group['prop'] = births/ births.sum()
	return group

def pull_col_names(group):
	new_cols = []
	cols = group.dtypes.index
	for col in range(0,len(cols)-1):
		new_col = cols[col].lstrip("u'")
		new_cols.append(new_col)
	return new_cols

def get_top1000(group):
		return group.sort_index(by='births',ascending=False)[:1000]

names = create_bn_data()
names = names.groupby(['year','sex']).apply(add_prop)

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

#Analyzing Naming Trends
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table(values='births',index='year',columns='name',aggfunc=sum)
subset = total_births[['John','Harry','Mary','Marilyn']]
subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of Births per Year")
draw()
show(block=False)
show()