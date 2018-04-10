'''
# First Python programme to print message

print("My First Python Programme")

# Two number addition

print(5+5)

# Concatenation of two number

print("5"+"6")

# Covert number into integer

Add_No = int("5") + int("6")
print(Add_No)

# Different string programme

print('He said "I want this"')

print('He said "Don\'t do that"')

print("The cost "+str(11+5)+" Rupees")

print("Hello:Dilesh".split(":"))

print("My country is "+"India:US:UK".split(":")[1])

# Boolean operator
No_boolean = (5 == 5)
print(No_boolean)

No_boolean1 =(5 == 8)
print(No_boolean1)

No_boolean2 =(5 is not 8)
print(No_boolean2)

No_boolean3 =(5 is 5)
print(No_boolean3)

No_boolean4 =("This" is "This")
print(No_boolean4)

No_boolean5 =(True is False)
print(No_boolean5)

No_boolean6 =("True" is True)
print(No_boolean6)

No_boolean7 =("True" is str(True))
print(No_boolean7)



# Array

array_list = ["Movie","Game","Python"]
print(array_list[0])

print("I like " + array_list[1])



# Dictionaries

Dict_1= {"Name":"Nick","Age":28,"hobby":"game"}['Name']
print(Dict_1)



# Variable
str1 = "Hello world"
print(str1)
str1 = str1.split(" ")[0]
print(str1)
print(str1 + " Friends")



# Built in function
var = int("5")
print(var)

var1 =len("Hello")
print(var1)


var2 =len([1,2,3,4,5,6,7,8])
print(var2)

var3 =len(["Hello","world"])
print(var3)

var4 = sorted([1,233,32,41,5,66,7,88])
print(var4)

var5 = sorted(["D","I","l","e"])
print(var5)

var6 = sorted(["D","I","l","e","3","5.55"])
print(var6)



# User Defined Function


def my_function():
    print("My first Function")
    print("My second String")


my_function()


def sec_function(str1,str2):
    print(str1)
    print(str2)


sec_function("Hello","World")



# Default Arguments


def print_something(name,age):
    print("My name is "+ name +" and my age is "+ str(age))


print_something("Nike",27)


def print_something_new(name="", age="28"):
    print("My name is ", name, "and my age is " , age)


print_something_new("Mike")



# Keyword Arguments


def print_something_keyword(name="unknown", age="28"):
    print("My name is ", name, "and my age is " , age)


print_something_keyword(age=36,name="Mike")



# Infinite Arguments


def print_people(*people):
    for item in people:
        print("This Person like",item)


print_people("Ice-cream" , "Fruits" ," juice")




# Return values from functions


def do_math(sum1, sum2):
    return sum1 + sum2


math1 = do_math(10, 20)
math2 = do_math(5, 5)

print("First sum result ", math1, "Second math sum ", math2)


# If else statement(Conditional statement)
check = True

if check == False:
    print("It is False")
elif check == "not mentioned":
    print("It is not mentioned")
elif check == "Mentioned":
    print("It is Mentioned")
else:
    print("It is True")



# For/while Loops

#For loop

Numbers = ["first","Second","Third",4,5]
for items in Numbers:
    print(items)

# While Loop
run = True
items = 1

while run:
  if items == 10:
    run =False
  else:
    print(items)
    items += 1

'''

# Import libraries into scripts
import re
string = "I AM HAPPY PERSON,/ if everyone is happy: "
print(string)
new = re.sub('[A-Z]', '', string)
print(new)
new = re.sub('[a-z]', '', string)
print(new)
new = re.sub('[,/:]', '', string)
print(new)
new = re.sub('[A-Za-z,/:]', '', string)
print(new)
new = re.sub('[A-Z,/:+" "]', '', string)
print(new)

string = string + "6 365-98"
print(string)
new = re.sub('[^0-9]', '', string)
print(new)