
# EXERCISE 1
def calc_volumme(mass, density): # define arguments
    factor = 19.6133
    volume = mass*density # do calculations
    volume_string = f'the kinetic energy is {volume} Newton' # create string 
    return volume_string

print(calc_volumme(1, 4))

# EXERCISE 2
colors = {1:'green',2:'red', 3:'blue',4:'black'}

for i in colors:
    if i%2 == 0:
        print(colors[i])

# EXERCISE 3
import pandas as pd
from matplotlib import pyplot as plt
absolute_path = 'F:\\Python Kurs\\data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Sensoren.txt'
df = pd.read_csv(absolute_path, decimal='.', sep='\t') 
df.set_index('time', inplace=True)
df_sub = df[['IRdiode', 'microphone']].iloc[30000:40000]
df_sub.to_csv('df_sub.csv', sep='\t', decimal='.')
print(df_sub)
df_sub.plot()
plt.savefig('df_sub.png')

# EXERCISE 4
import pandas as pd
from matplotlib import pyplot as plt
path1 = "data\\Pbtrizinat_50_11_30-06-2021-13-50-56\\Pbtrizinat_50_11_Spektrometer.txt"
path2 = "data\\Pbtrizinat_50_12_30-06-2021-13-52-30\\Pbtrizinat_50_12_Spektrometer.txt"
path3 = "data\\Pbtrizinat_50_13_30-06-2021-13-54-17\\Pbtrizinat_50_13_Spektrometer.txt"
path_list = [path1, path2, path3]
df_list = []
for path in path_list:
    name = path[path.rfind('\\')+1:path.rfind('.')]
    df = pd.read_csv(path, decimal='.', sep='\t') 
    df.rename(columns={"counts" : name}, inplace=True)
    df.set_index('wavelength', inplace=True)
    df_list.append(df)
df_new = pd.concat(df_list, axis=1)
print(df_new)
df_new.plot()
plt.savefig('spectra.png')
plt.close()