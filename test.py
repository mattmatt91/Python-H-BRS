import pandas 
from pandas import DataFrame

data = {'time':[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'current': [100, 77, 29, 0, 17, 64, 98, 87, 42, 4],
        'voltage': [50, 92, 95, 57, 12, 2, 36, 82, 99, 70]}


my_df = pandas.DataFrame(data) 

print(my_df)

# get colums and index
print(my_df.columns) # attribute

myIndex = my_df.index # save return in variable
print(myIndex)

print(my_df['voltage']) 



my_df.set_index('time', inplace=True)#  arguments and keywords - arguments first, order of keywords doesnt matter
print(my_df)

# assign new # assign new cols
my_df['power'] = my_df['voltage'] *my_df['current']
print(my_df)

my_df['not_power'] = my_df['voltage'] / my_df['current']

my_df.drop('not_power', axis=1, inplace=True) # 

print(my_df.info())
print(my_df.head())
print(my_df.corr())
print(my_df.describe())# new function
# print(my_df.stack())
print(my_df.shape) # attribute