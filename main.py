#DAY 1 

#lets start learning python in very simple and easy language so our first line of code looks like this 

print("hello world")

# printing few sentences to understand python more clearely 

print("python is very easy and high level language")
print("python is not a case sensitive language")

# in python we can also print numbers in and those are concidred either integer or floating value according to the value of the number

a = 12; # (an integer value)
print(a)
print(type(a))

# for a floating value with proof of its floating type

b = 12.5;
print(b)
print(type(b))

# variables 

#variables can be defined as a name given to memory located in a program, here are some examples for the variables 
# variable with few steps 
#step 1 -> to use variable first we store the data in memory 

name = "ram" 

# in this sentence the "name" represents the variable and the "ram" represents the value of the variable 

# step 2 -> now give command to print name by given variable 

print(name) #ram

# lets take more examples of 

#eg 1 ->
age = 12;
colour = "green"
hobby = "badminton"

# in these 3 sentences above the "age", "colour" and the "hobby" are the variable and the "12", "green" and "badminton" are the values which are stored in the memory 

# now we can give command to print the variables to check if the values are stored in the memory or not 

print(age) # 12
print(colour) #green
print(hobby) #badminton

# *always keep the variable name short, clean and meaningful

# day 2 

# in day 2 we will start with data types and there types 
# there are 5 types of data type and all the 5 types of data type are as follow :

#1) strng
#2) integer 
#3) float
#4) boolean 
#5) none 

# * String -> string data type contains any letter, word, or any sentence mainly letters for eg ->
name2 = "naman"
print(type(name2)) # string

#eg2 ->
section = "builder 1"
batch = "batch 1"

print(type(section)) # string value will be shown on the screen 
print(type(batch)) # string value will be shown on the screen 

# * integer -> integer data type contains all the integer value that exist in the world for eg->

age = 12;
marks = 98;
percentage = 77;

print(type(age)) # 12, this is an integer value 
print(type(marks)) # 98, this is an integer value 
print(type(percentage)) # 77, this is an integer value 

# * float -> float data type contains all the number which have decimal in it for eg ->

percentage2 = 89.5
price = 35.5 

print(type(percentage2)) # this is a floatin value 
print(type(price)) # this is a floatin value 

# bollean -> boolean data type contains 2 values which are true and false, for eg ->

x = 12
y = 13

print(type(x>y)) # its False and the type is boolean
print(type(y>x)) # its True and the type is boolean 

# none -> the none data type contains nothing in it for eg ->
a = None;
print(type(a)) # none 

#KeyWords 

#* All the key words are reserved innpython and non of the Keywords can be used as Variable, for eg->

# and , else , in , return , as , except , is , True , asset , Finally 
# lambda , try , break , False , non local , with , class, for , none , while 
# continue , from , not , yeald , def , if , pass , elif , import , raiss 


# * Python is a case sensitive language it means that (A and a) both are different variables and have different meaning 

#eg -> Apple and apple both have different meaning in python because python is a case sensitive language 

# Comments ->

# comments are used when the developers dont want any user to see that line of code for eg -> all the colourless lines which are visible in this codebase are called comments 

# practice qurestion -> 1) print the sum of any 2 numbers 

a = 12;
b = 13;
sum = a+b;
print(sum); # 12+13 = 25 

# DAY 3 ->

# Operators and there types

# an oprator is an symbol that perform a certain operations b/w opratents 

# there are total 4 oprators 
#1) Arthematic oprator 
#2) Relation oprator 
#3) assingment oprator 
#4) logic oprator 

# Arthematic Oprator -> Arthematic oprators are all the oprators avalable in mathamatics For eg ->{+, -, /, *, **}

