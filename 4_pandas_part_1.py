# install libary
# in console:
# for installation: pip install 'libaryname'
# for version controll: show Jinja2 'libaryname'
# for uninstallation: pip uninstall 'libaryname'
# show all installed packages: pip freeze

# different possibilities of importing
import pandas as pd
import matplotlib.pyplot as plt # abkürzung zum importieren


data = {'time':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'current': [100, 77, 29, 0, 17, 64, 98, 87, 42, 4],
        'voltage': [50, 92, 95, 57, 12, 2, 36, 82, 99, 70]}
print(data)

# DataFrames
# call the constructor with arguments
# what is an instance
my_df = pd.DataFrame(data) 
print(my_df)


# get colums and index
print(my_df.columns) # attribute
myIndex = my_df.index # save return in variable
print(myIndex)

# indexing df
print(my_df['voltage']) # index with columnname

# set index
# once initiated functions can be called with the instance
print(my_df.set_index('time'))
print(my_df) # mind the replace keyword
my_df.set_index('time', inplace=True)#  arguments and keywords - arguments first, order of keywords doesnt matter
print(my_df) 

# assign new cols
my_df['power'] = my_df['voltage'] *my_df['current']
print(my_df)

# remove cols
my_df['not_power'] = my_df['voltage'] / my_df['current']
my_df.drop('not_power', axis=1, inplace=True) # axis is important to assign x axis

# pandas : https://pandas.pydata.org/docs/reference/frame.html

# useful functions
print(my_df.info())
print(my_df.head())
print(my_df.corr())
print(my_df.describe())# new function
print(my_df.stack())
print(my_df.shape) # attribute


# EXERCISE ################################################

#  search in the cheat sheet how to get means of all cols

###########################################################


# reading csv files
# reltive or absolute path
absolute_path = 'F:\\Python Kurs\\data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Sensoren.txt'#  point out to seperators
relative_path = 'data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Sensoren.txt'

my_df = pd.read_csv(relative_path, decimal='.', sep='\t') 
my_df.set_index('time', inplace=True)
print(my_df)

# indexing df 2
print(my_df['VISdiode'])
print(my_df.iloc[3,:]) # fourth row, all cols
print(my_df.iloc[3:6,2]) # fourth row, all cols


# filtering
# only returns values ​​that meet a certain condition
print(my_df[my_df['VISdiode'] > 0.1])
print(my_df['VISdiode'] > 0.1)

# saving
my_df_new = my_df.iloc[3:6,2]
my_df_new.to_csv('new2_Df.csv', sep='\t', decimal='.') # not delimiter


# Plotting dfs
#build on matplotlib
my_df.plot() # creates a plot
# plt.show() #shows it and sleeps until plot is open

# keywords
# kind="barh"
# legend=False,
# xerr="std"
# colormap='summer' -->https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html
# grid=True
# figsize=(8,4)
# subplots =True

my_df.plot(grid=True, subplots=True, colormap='viridis') # creates a plot
plt.show() #shows it and sleeps until plot is open

# other possible plots are:
# https://pandas.pydata.org/docs/user_guide/visualization.html


# saving a plot

my_df.plot(grid=True, subplots=True, colormap='viridis')
my_df.iloc[30000:40000,2:].plot(grid=True, subplots=True, colormap='viridis')

plt.savefig('test_plot.png') #save the last opended plot
plt.show()
plt.close() 


# ECERSICE 3 #############################################################
# read a file (sensor) and init an pd.DataFrame
# index the IR and microphone and plot 1 relevant second
# save the sub Dataframe to csv
##########################################################################


# merge, join, concat
# creating some data
df1 = pd.DataFrame({'time':[0,1,2,3,4], 'sensor1':[34,44,32,45,13],  'sensor2':[334,454,382,545,413]})
df2 = pd.DataFrame({'time':[0,1,2,3,4], 'sensor3':[3244,4424,3432,4435,433],  'sensor4':[3.34,4.54,3.82,5.45,4.13]})
df3 = pd.DataFrame({'time':[5,6,7,8,9], 'sensor1':[36,44,42,75,23],  'sensor2':[534,654,362,555,213]})
df4 = pd.DataFrame({'time':[5,6,7,8,10], 'sensor1':[36,44,42,75,23],  'sensor4':[5334,6554,3162,1555,1213]})

# set index 
df1.set_index('time',inplace=True)
df2.set_index('time',inplace=True)
df3.set_index('time',inplace=True)
df4.set_index('time',inplace=True)

print(df1.head())
print(df2.head())
print(df3.head())
print(df4.head())

# append --> dfs should have the same columns
print(df1.append(df3)) 

# concatdfs should have the same index
print(pd.concat([df1, df2], axis=1))

# multi indexing

# reading dfs
path1 = 'F:\\Python Kurs\\data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Sensoren.txt'
path2 = 'F:\\Python Kurs\\data\\Pbtrizinat_50_14_30-06-2021-13-55-46\\Pbtrizinat_50_14_Sensoren.txt'
name1 = path1[path1.rfind('\\')+1:path1.rfind('.')]
name2 = path2[path2.rfind('\\')+1:path2.rfind('.')]
df2 = pd.read_csv(path2, decimal='.', sep='\t') 
df2.set_index('time', inplace=True)

df1 = pd.read_csv(path1, decimal='.', sep='\t') 
df1.set_index('time', inplace=True)

# set the multi columns
# different functions to add mutliindex
# here: with string and oold columns
df1.columns = pd.MultiIndex.from_product([[name1], df1.columns]) 
df1.columns.names = ('measurement', 'sensor')

df2.columns = pd.MultiIndex.from_product([[name2], df2.columns])
df2.columns.names = ('measurement', 'sensor')
print(df2.head())

df3 = pd.concat([df1, df2], axis=1) #conccat dfs
print(df3.head())

# print all unique values on a specific columns level
print(df3.columns.unique(level=1))
print(df3.columns.unique(level=0))

print(df3.xs('VISdiode', level='sensor', axis=1)) # index multiindex with xs() --> explain

print(df3.xs('Pbtrizinat_50_14_Sensoren', level='measurement', axis=1)) # index multiindex with xs() --> explain

# EXERCISE ########################################################
# read the files and concat them to a df. use wavelength as index 
# search in cheat sheet how to rename columns
# make a plot with all three measurments
# look in the pandas plot cheat shet or google how to set grid in plot (with keyword)
path1 = "data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Spektrometer.txt"
path2 = "data\\Pbtrizinat_50_12_30-06-2021-13-52-30\\Pbtrizinat_50_12_Spektrometer.txt"
path3 = "data\\Pbtrizinat_50_13_30-06-2021-13-54-17\\Pbtrizinat_50_13_Spektrometer.txt"
###################################################################




