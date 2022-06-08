
from unicodedata import decimal
import pandas as pd
from matplotlib import pyplot as plt
import os
from pathlib import Path

def read_df(path):
    Path("/data").mkdir(parents=True, exist_ok=True)
    print(path)
    name = path[path.rfind('\\')+1:path.rfind('_Sensoren')] # cut out the name
    this_df = pd.read_csv(path, delimiter='\t', decimal='.') # initialize the
    this_df.set_index('time', inplace=True) # set index time
    this_df.columns = pd.MultiIndex.from_product([[name], this_df.columns]) # multiindexing 
    this_df.columns.names = ('measurement', 'sensor') # set col index name
    return this_df 

def read_files(path_data): #iterate over path list
    my_dfs = [] #create empty list for dfs
    for root, dirs, files in os.walk(path_data):
        if files:  # check is there are files
            for file in files: # iterate over files
                path = os.path.join(root,file) # build path for measurement
                if path.find('Sensoren')>=0: # check if file is a sensor file
                    df = read_df(path) #call a nested function
                    my_dfs.append(df) # reading files 
    return my_dfs
    

def plot_measurement(df):
    for measurement in df.columns.unique(level=0): #iterate over uniques from index 0 (which ist measurements)
        # plot df --> explian keywords and where to find them
        df[measurement].plot(title=measurement,grid=True, colormap='summer',subplots =True) # plot df
        plt.savefig(os.path.join('results', f'{measurement}.png')) #save fig
        plt.close()


def plot_sensor(df):
    for sensor in df.columns.unique(level=1): #iterate over uniques from index 0 (which ist measurements)
        # plot df --> explian keywords and where to find them
        this_df = df.xs(sensor, level='sensor', axis=1) 
        this_df.plot(title=sensor,grid=True, colormap='summer',subplots =True) # plot df
        plt.savefig(os.path.join('results', f'{sensor}.png'))
        plt.close()


def do_statistics(df):
    results = []
    for sensor in df.columns.unique(level=1): # create a new dataframe from all measurements with each sensor
        print(sensor)
        df_sensor = new_df.xs(sensor, level='sensor', axis=1) # index df with level sensor
        mean = df_sensor.max().mean() # calculate mean and std and append  dictionary to list
        std = df_sensor.max().std() 
        this_dict = {'sensor': sensor, 'mean': mean, 'std': std} # create dict with results
        results.append(this_dict)  # append dict to list

    df_result = pd.DataFrame(results) # create df with results
    df_result.set_index('sensor', inplace=True) #set sensor as index
    print(df_result)
    df_result.plot(kind="barh", y="mean", legend=False, # create barplot with std as errorbar
                title="mean of max values of all sensors", xerr="std", colormap='summer',grid=True, figsize=(8,4))
                
    plt.savefig(os.path.join('data', f'statistics.png'))
    plt.close()
    return df_result

def save_df(df, name): # save df 
    df.to_csv(os.path.join('results',(name + '.csv')), sep='\t',decimal='.')



if __name__ == '__main__': # code ist only executed if program is main and not imported

    dfs_list = read_files('data') #call a function

    new_df = pd.concat(dfs_list, axis=1) #  concat dfs --> mind axis=1
    print(new_df.head())

    plot_measurement(new_df)

    plot_sensor(new_df)

    df_statictic = do_statistics(new_df)
    save_df(new_df, 'statistics')


