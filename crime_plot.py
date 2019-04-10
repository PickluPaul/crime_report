#!/usr/bin/env python
"""
crime_plot.py: This program is used to plot the graph for different crime rates
"""

__author__ = "Picklu Paul"
__copyright__ = "Copyright 2019"
__credits__ = ["Picklu Paul"]
__version__ = "1.0.0"
__maintainer__ = "Picklu Paul"
__email__ = "picklupaul93@gmail.com"
__status__ = "Development"

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt
plt.figtext(0.50, 0.96, ' Analysing Crime Subcategory of Seattle ',fontweight='extra bold', fontsize='large', color='R', ha ='center')

#Crimes each year
def plot_graph_by_year(crimes):
	plt.plot()
	sns.countplot(x='year',data=crimes,order=crimes['year'].value_counts().index)
	plt.xlabel('Year')
	plt.xticks(rotation=90,fontsize=6)
	plt.ylabel('No of Crimes ')
	plt.title('Crime rates by year')
	plt.savefig('YearWiseReport.png')

def plot_graph_by_month(crimes):
	months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	plt.plot()
	sns.countplot(x='month',data=crimes,order=crimes['month'].value_counts().index)
	plt.xlabel('Month')
	plt.xticks(rotation=30)
	plt.ylabel('No of Crimes ')
	plt.title('Crime rates by month')
	plt.savefig('MonthWiseReport.png')


def plot_graph_by_time(crimes):
	plt.plot()
	sns.countplot(x='Reported Time',data=crimes,order=crimes['Reported Time'].value_counts().iloc[:30].index)
	plt.xlabel('Time')
	plt.xticks(rotation=20)
	plt.ylabel('No of Crimes ')
	plt.title('Crime rates by hours of day -- Top 30')
	plt.savefig('TimwWiseReport.png')


if __name__ == '__main__':
	csv_file=input('Enter full path to the CSV data file: ')
	data=pd.read_csv(csv_file)
	crimes = data.dropna(axis = 0, how ='any')
	crimes['year'] = crimes['Occurred Date'].astype("datetime64").dt.strftime('%Y')
	crimes['month'] = crimes['Occurred Date'].astype("datetime64").dt.strftime('%b')
	plot_graph_by_year(crimes)
	plot_graph_by_month(crimes)
	plot_graph_by_time(crimes)






