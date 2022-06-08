import os
from os import listdir
from os.path import isfile, join
from pathlib import Path



# path is a string
path = 'F:\\Python Kurs\\data_test_dir\\day0\\measurement0\\sensor0.txt'

# STRING OPERATIONS
path = 'F:\\Python Kurs\\data_test_dir\\day0\\measurement0\\sensor0.txt'

# split stirng to list
path_to_list = path.split('\\')
print(path_to_list)

# get index of first occourence
print(path.find('\\'))

# get index of last occourence
print(path.rfind('\\'))

# index strings
print(path[2:9])

index = path.rfind('\\')
print(path[index:])

index1 = path.rfind('\\') +1
index2 = path.rfind('.')
print(path[index1:index2])

path1 = 'F:\\Python Kurs\\data_test_dir\\day0\\measurement0\\sensor0.txt'
path2 = 'F:\\Python Kurs\\data_test_dir\\day0\\measurement0\\sensor1.txt'

# check if string occours for if statement
bool1 = path1.rfind('sensor1') >=0
bool2 = path2.rfind('sensor1') >=0
print(bool1, bool2)

# directory stuff
#get current working directory
print(os.getcwd())

# list all subdirectories and files
print(os.listdir())

# cerate directory
# doesnt work if dir already exists
try:
    os.mkdir('testdir')
except:
    pass

# change directory
# print(os.chdir('results'))

# get all directorys and files nested
for root, dirs, files in os.walk(os.getcwd()):
    print(root, '\n', dirs, '\n',files, '\n')   

#create path if not exists
Path("/results").mkdir(parents=True, exist_ok=True)



# EXAMPLE
# iteratively loop over all the folders and add their data to the list
for root, dirs, files in os.walk('data_test_dir'):
    if files:  
        for file in files:
            path = os.path.join(root,file)
            if path.find('sensor1')>=0:
                print(path)




