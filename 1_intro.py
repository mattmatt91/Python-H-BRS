# VARIABLES
my_int = 5
print(my_int) # pass argument in function
print(type(my_int)) # nest funtion

myFloat = 2.5
print(myFloat)
print(type(myFloat))

my_list = [0,1.3,3,'test']
print(my_list)
print(type(my_list))
print(my_list[3]) # lists are indexable
print(my_list[2:4]) # index range from list
my_list[2] = 'new value' # change value of list entry
print(my_list)
my_list[2] = [1,5,7] # put a list in a list
print(my_list)
my_list.append('appended value')

my_string = 'this is a string'
print(my_string)
print(type(my_string))
print(my_string[4]) # strings are indexable

my_bool = False # bools sind 1 0 True False
print(my_bool)
print(type(my_bool))
my_bool = 1 >= 4 # returns a bool

myDict = {'value1':1, 'value2':4, 'value3': my_list}
print(myDict)
print(type(myDict))
print(myDict['value1']) # index dict by key
myDict['new value'] = [1,5,7] # add new key to dict, all datatypes are possible

my_tupple = (0,1,5)
print(my_tupple)
print(type(my_tupple))
print(my_tupple[0]) #tumples are indexable

# ERROR EXAMPLE
# my_tupple[2] = 4 # but not changeable

# FIRST CALCULATIONS
number1 = 3
number2 = 4

# valid operators
# plus  +
# minus -
# mal * 
# geteilt mit float /
# geteilt ganzzahlig //
# Modulo %
# zum quadrat **
# zuweisen =

# True False return
# größer >
# kleiner <
# ist gleich  ==
# größer gleich  >=
# kleiner gleich  <=

number3 = number1 + number2
print(number3)
number2 = number2 + number3 # int is changeable
print(number2)

print(number1 - number2) # nest functions

print(number1, number2) # multiple arguments
print(f"number1 is {number1} and number2 is {number2}") #formatstrings

string1 = " this is the first part"
string2 = " this is the secod part"

print(string1 + string2)

# FUNCTIONS
my_string = 'string'
my_int = 3
# print(my_string + my_int) # returns an error with line and type of error

# exercise
# printe einen Formatstring mit den variablen "age" und "name", sodass ausgegeben wird:
# Hallo "name", du bist "age" Jahre alt
name = 'Matthias'
age = 102
print(f'Hallo {name}, du bist {age} Jahre alt')