#                                                    DAY 1
#                                               <--------------> 

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

#                                                day 2 
#                                          <--------------->

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

#                                                DAY 3 
#                                           <------------->

# Operators and there types

# an oprator is an symbol that perform a certain operations b/w opratents 

# there are total 4 oprators 
#1) Arthematic oprator 
#2) Relation oprator 
#3) assingment oprator 
#4) logic oprator 

# Arthematic Oprator -> Arthematic oprators are all the oprators avalable in mathamatics For eg ->{+, -, /, *, **} 

a = 10;
b = 13;
sum = (a+b);
sub = (a-b);
mul = (a*b);
div = (a/b);
power = (a**b);

print(sum) # 23
print(sub) # -3
print(mul) # 130
print(div) # 0.7692307692307693
print(power) # 10000000000000

# inputs in python ->
# inputs are used to take inputs from the user any value, integer, string, float, none or boolean values :

#Inputs are used to accept value from the users through Keyboard, for example ->

a = input("enter your name: ")
b = input("enter your age: ")

print(a) # enter your name: 
print(b) # enter your age: 


# practice question : 2) write a program to take users input and then make there sum and find its avarage 

a = int(input("enter any number : "))
b = int(input("enter any other number: "))
c = int(input("enter any 3rd number: "))

sum = a+b+c;
avg = (a+b+c)/3

print(sum)
print(avg)

# Strings 
# string is a data type that stores sequence of character and word 
#* in string if any user needs to change time or jump to next line we use (\n)
#* and if any user needs some space between text then user will use (\t)

# Concatanation ->
# Concatination can be defined as the addition of two strings value for eg->
# "hello" + " " + "world" = "hello world"

str1 = "naman"
str2 = " "
str3 = "pandey"

print(str1+str2+str3) # naman pandey

# Length of string 
# the length of string can be defined as the number of length in the string, for eg->

str1 = "HELLO WORLD"
# the length -> H E L L O  W O R L D
#               1 2 3 4 5 6 7 8 9 10 11

# the length of the string is 11 
# symntax = print(len(str1))
print(len(str1)) # 11

#                                             DAY 4 
#                                        <------------->

# string functions 
# string functoins can be defined that string functions helps to find the value, the count, the letters and also it helps to capatilise the letters and also replace some of the words or letters 

# there are total 5 types of string functions 

str = "i am a coder"

# str is a string in which all the functions will be followed 

# 1) str.endswith() -> endswith is used to check that the string ends with the provided letter or provided word, eg->

str.endswith("coder") # true

# 2) str.capatilizer -> capatalizer is used to make the first letter of any string capatial in the string for eg->

str.capitalize() # "I am a coder"

# 3) str.replace -> replace is used to either replace a letter or any word in a stirng for eg->

str.replace("coder", "programmer") # "i am a programmer"

# 4) str.find -> find is used to find if the letter or word is avalable in that sting or not if yes then it will print true and if no then it will print false, for eg->

str.find("coder") # true
str.find("he") # false 

#5) str.count -> count is used to count the number of occurence of the letter or word in that string, for eg->

str.count("a") # 2, 2 because in the sentence "i am a coder" "a" comes 2 time 

# Indexing 
# --------

# indexing can be defined as the location and the position of the string or the alphabet of that string, for eg->

str2 = "naman pandey"

# n a m a n   p a n d e y 
# - - - - - - - - - - - -
# 0 1 2 3 4 5 6 7 8 9 0 10
# -------------------------->


# indexing strts from 0 and can go till any number of character including space 

# to print the character of a spacific index number soo we do ->
print(str2[4]) # n " "n" will be printed because "n" is on the 4th place of "str2" "

# **** we can not and never change the index value of any string ****

# Conditional startment ->
# -----------------------
# condition startment are those startment in which the user apply some conditions like (if , elif, else)

# conditional startents are used to check the conditions and privide results on the basis of the conditions for eg->

my_name = "naman"

if(my_name == "naman"): # this line says that if the name is true that the name is naman 
    print("its true") # and this line says that if the above line is true then print "ts true"
elif(my_name == "aman"): # this line says if the "my_name" is not "naman" then check if its "pandey" or not 
    print("its true too") # this line says if "my_name" is "pandey" the print "its true too"
else:  # this line says that is nothing is true than use me 
    print("false") # and this line says that if the else condition will have to work thenprint "false"
    
    
#                                             DAY - 5
#                                         <------------->

# day 5 will be start with an example of conditional startment, eg-> 

colour = "green" # this line means that the colour variable stores "green" value

if(colour == "red"): # this line represents that if the colour is "red" then perform the below activity
    print("the colour is red, you need to stop") # this line says that if the colour is "red" then print the startment 
elif(colour == "yellow"): # this line says that if the colour is "yellow" the perform the following activity
    print("the colour is yellow, be ready to move") # this line says that if the colour is "yellow" then print the startment
elif(colour == "green"): # this line says that if the colour is green then do the following step
    print("the colour is green, you can go now") # this line says that if the colour is "green" then print the given startment
else:
    print("the colour dont exist") # this line says if no colour match then print this startment
    
#       nestsed conditional startment
#     ----------------------------------

# nested conditional startments are used when they are more then 1 condition applied in a startment eg->

name = "rahul" # this line means that the name variable stores "rahul" value
surname = "singh" #  # this line means that the surname variable stores "singh" value

if(name == "singh"): # this line says that if the name is "singh" then you can chekc the next startment
    if(surname == "rahul"): # this line says that if the surname is "rahul" then you cna check the next line 
        print("unsuscess") # this line says that if both the above lines are true then print "unsuscess"
if(name == "rahul"):# this line says that if the name is "rahul" then you can chekc the next startment
    if(surname == "singh"): # this line says that if the surname is "singh" then you cna check the next line 
            print("suscess") # this line says that if both the above lines are true then print "suscess"
    else: 
        print("the startment is wrong") # this line says that if non of the thing is matching then print this "the startment is wrong"
        
#       Match Case 
#    <-------------->

# match case are the alternative of the conditional startments and are used very less in python programing, most of the time we will be using conditional startments only

# eg for match case - >

colour = "red" # this line means that the colour variable stores "red" value
match colour: # this startment says that match the colours according to the cases 
    case "red": # this line says thst the colour is red then you cna print the following line
        print("you have to stop") # this line says that of the colour is red then print "you have to stop"
    case "yellow": # this line says thst the colour is yellow then you cna print the following line
        print("you will have to stop now") # this line says that of the colour is yellow then print "you will have to wait"
    case "green": # this line says thst the colour is green then you cna print the following line
        print("you can go now") # this line says that of the colour is green then print "you can go now"
    case _ : 
        print("nothing maches") # this line says that if any colour dont matches then print "nothing matches"
        
#          loops 
#     <------------>

# loops-> loops are used to repet any task for some certain number of time and it also depends on the user 

# loops are classified in 2 types 
# 1) while loop
# 2) for loop

#       While loop
#   <---------------->

# while loop -> while loop are used till the condition is true and once the condition is false the loop will stop 
# ** in while loop if we use "True" as condition then the loop will be an infinite loop and its not preferable to make any loop as infinite loop **

# understanding while loop with an example eg->

i = 0; # here "i" is a iterator which starts the loop and also can be said as "i" starts the loop
while (i <= 10):  # in this sentence, (i<=10) represents that i cannot be grater then 10, i can only be lessthen or equal to 10 and also (i<=10) is an condition
    print(i) # this line says to print the value of "i"
    i += 1 # this line says then how the value of "i" will increase

# everything together ->
   
    i = 0
    while (i <= 10):
        print(i)
    i += 1;

#                                                           DAY - 6
#                                                    <------------------>


# today we will try to revise all the older topics together 

#)        variables 
#      ----------------
x = 12;
y = "naman"

# in these both lines "x", "y" are variables and "12", "naman" are the value which are stored 

#            Data Type
#      ---------------------

# there are total 5 type of data types 
# 1) string
# 2) float
# 3) integer
# 4) boolean
# 5) none

#1) string
name = "naman"

print(type(name)) # string

#2) integer

age = 12;
print(type(age)) # integer

#3) float
marks = 89.4
print(type(marks)) # float

#4) boolean 
name = True;
print(type(name)) # boolean

#5) none 
a = None;
print(type(a)) # none

#      Print sum problem
#    ----------------------

a = 12;
b = 13;
sum = a+b
print(sum);

#          oprators and there type
#      --------------------------------
 
# thre are total 4 oprators 
# 1) arthemetic oprator ->  {+, -, /, *, **, %}
# 2) assingment oprator ->. {+=, -=, /=, *=, %=, **=}
# 3) relation oprator ->  {==, !=, >=, <=, >, <}
# 4) logic oprator -> {and, or, not}

#            conversion and there types 
#        ----------------------------------

# there are 2 types of conversion 
# 1) manual conversion
# 2) automatic conversion 

# automaic conversion ->
a = 12 # integer
b = 13.5 # float
sum = a+b
print(type(sum)) # float

# manual conversion 
a = 12
b = 13.5
c = float(a) # this line change the value of a into float value manually 
print(type(c))
print(c) 

#             Inputs in python
#         -------------------------

# inputs are used to take input from the user, eg->

a = input("write your name")
b = input("enter your age")

#            String Function
#        ----------------------

# 1) str.endswith()
# 2) str.capatilised 
# 3) str.replace("a", "b")
# 4) str.find("a")
# 5) str.count()

# for eg->

str = "i am coder"

str.endswith("coder") # True
str.capitalize() # I am a coder
str.replace("coder", "programer") # i am a programmer
str.find("a") 
str.count("c") # count the occurence of the "c" letter in the "str" sentence

#          Indexing
#      ----------------

# indexing helps to know the couurnt position of any character in the string, for eg

name = "naman pandey"
# so the indexing is -> n a m a n   p a n d e y 
 #                      - - - - - - - - - - - -
 # index values ->      1 2 3 4 5 6 7 8 9 10 11 12
 
 # *** we can not change the index value of any string ***
 
 #              conditional startment
 #          ------------------------------
 
 # conditional startments are used to apply conditions like (if, elif, else) for eg ->
 
i = 12;
if (i == 100):
    print("suscess")
else:
    print("unsecessfull")
    
#                 nested conditional startments 
#          --------------------------------------------


# nested conditional startments are used to write 2 or more then 2 conditions in one go, for eg->
i = 12;
j = 13;

if (i == 12):
    if(j==13):
        print("suscessfull")
    print("true")
else:
    print("not true")

#                 Match Case Revision
#             --------------------------

# match case are an alternative of conditional startments for eg

i = 12;
match i:
    case 12:
        print("suscess")
    case 13:
        print("unsuscessfull")
        
#.                  Loops 
#                -----------

# loops are used to itrate any value, itrate means to repeat anything

# there are two types of loops 
#1) while loop
#2) for loop

#     while loop
#  -----------------

# while loops are used to repet any value till the condition is true, for eg->

i = 12;
while (i<= 100):
    print(i)
    i += 1 #12, 13, 14, 15, 16, 17, 18........ 100
    