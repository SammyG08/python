# learning about types of paramters in python
# *args converts the argument into a tuple and operates on it
# it uses a tuple because tuples are immutable
# it is like function overloading in c++ where by one function
# can operate on different number of arguments passed
# with args, you can not pass in key value pair items with changing number of arguments
# in that case, we use the **kwargs (key word argument)
# function parameters follow a certain order that is:
# normal argument that is positional or key word
# then arbitrary that is *args before **kwargs
def add(name, *args):
    summation = 0
    for number in args:
        summation += number
    print(summation)
    print(name)


# add(3,1,4,5, name = 'Michelle') # error cos the compiler is treating the 3145 as the value for the name parameter
# add(10,11,20,10,23,2,4,5,9,'Kwesi') #error cos the function treats the kwesi as part of the tuple
# add(name = "kwesi", 1,2,3,) #error cos positional arguments must come before key word arguments
# a simple way to avoid all these errors is to bring the positional or keyword argument before the arbitrary argument
# in the declaration of the function
add("Michelle", 10, 15, 20, 25)


def personalInfo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


personalInfo(Ann=54891009, Quist=789182089)

# the title() function is mostly used for names when you want to capitalize the first letter of every word

# dictionaries syntax is the same as the syntax for sets
# the only difference is that with dictionaries the elements are stored in the form of key value pairs
# the syntax is key:value
# the key of the dictionary is immutable hence it can be anything except for lists
# the value however is mutable so it can be anything lists included
# we can have nested dictionaries that is dictionaries within dictionaries
# we can also have dictionaries within lists or lists within dictionaries
# we use the for loop to get the keys.
# the keys are used to access the values
# there can not be duplicate keys in the dictionary
# it is always assumed the key with the last value is the final value intended for that particular key
# we have some built in functions that we can perform on functions
# dictionaries are ordered that it they are not printed randomly but in the form that they were created
# syntax= dictionary_name {key : value,  key:value, ...}
# if you want to add an element to a dictionary you just have to give the key in the already existing dictionary
# and make it equals the value
# example: dictionary_name[key] = value_to_be_added


# functions can be nested in python unlike in c and c++
# you can also return multiple items in python unlike in other programming languages
# the returned values are stored in the form of a tuple
# however you can changed them to be stored in any form you like that is lists etc
# or even give every returned value it's own variable

# classes in python are declared as such: class ClassName:statements
# PascalCase variable naming convention is preferred for the class name
# the constructor is created similar to the way a normal function is created in python only
# difference is the __innit__ and self keywords
# example def __init__(self): statements
# the class attributes are then named there in the statement side
# the self keyword assigns the attribute to the particular object instantiated at that time
# every method in the class has to use this self keyword as a parameter
# attributes of a class are accessed by using the self.attribute_name

# you can use the import keyword followed by the file_name
# to import any file or module in order to access some things in the particular file
# the round function always starts from the first argument passed but ends right before the last argument
# so take note

# in the for else and the while else syntax, the else block is only printed once when the loop exits successfully
# the end = 0 used in the print function makes the next print appear on the same line
