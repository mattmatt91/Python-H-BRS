# set variables
velocity = 100
mass = 10

#calculate ekin
ekin = 0.5*mass*(velocity**2)
print(f'the kinetic energy is {ekin} Joule')


# define a function 
def calc_ekin(mass, velocity): # define arguments
    ekin = 0.5*mass*(velocity**2) # do calculations
    ekin_string = f'the kinetic energy is {ekin} Joule' # create string 
    return ekin_string

# call function with varaibles as arguments
my_ekin = calc_ekin(mass, velocity) 

# with numbers as arguments
my_ekin = calc_ekin(23, 100) 
print(my_ekin)

# function with several returns
def calc_ekin(mass, velocity): # define arguments
    ekin = 0.5*mass*(velocity**2) # do calculations
    ekin_string = f'the kinetic energy is {ekin} Joule' # create string 
    return ekin, ekin_string # retrun result and string

# set variables to return values
my_ekin, my_ekin_string = calc_ekin(mass, velocity)
print(my_ekin)
print(my_ekin_string)

# EXERCISE 1 ########################################################################

# define a function that calulates the volume of a substance with mass and density

#####################################################################################

# for loop
fruits = ['Banane', 'Apfel', 'Zitrone', 'Orange']
for fruit in fruits: # explain for loop
    print(fruit)

# in range()
for i in range(3):
    print(10*i)

# zip values to tuple
numbers = [2,6,8,2]
listOfStrings = [] # empty list
for fruis, number in zip(fruits, numbers): # arguments as tuple 
    listOfStrings.append(f'you need {number} pcs of {fruit}') # apend nubers to list in for loop
print(listOfStrings)

# inline function
myList = [4*i for i in range(9)] # short function for lists
print(myList)

# while loop
i = 0
while i <= 10:
    print(i)
    i +=1 # ++ is equal to +1

# if function
i = int(input('enter integer between 0 and 9')) # convert input to integer
if i >= 10:
    print('i is greater or equals 10')
elif i <= 0:
    print('i is smaller or equals 0')
else:
    print('i is between 0 and 10')

 # example with bool
myBool = True
if myBool:
    print('bool is True')

myString =  'red'
if myString == 'red': # exaplme with string
    print('the color is red')
    
# EXERCISE #####################################################################
                                                                          
# write a fucntio that only prints the color if the number is a multiple of two
colors = {1:'green',2:'red', 3:'blue',4:'black'}

###############################################################################