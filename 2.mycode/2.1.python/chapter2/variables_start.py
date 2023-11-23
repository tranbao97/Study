# basic data type in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "this is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one": 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring the variables
myint = "abc"
print(myint)

# to access the member of sequence type, use []
print(mylist[2])
print(mytuple[1])

# use slides get part of sequences
print(mylist[1:5])
print(mylist[1:5:3]) #start_idx:end_idx:step

# use slides to reverse sequence
print(mylist[::-1]) # the start_idx and end_idx: empty => use default
                    # the step: -1 => reverse sequence

# use key in dictionaries (same as map in C++)
print(mydict["one"])

# ERROR: cannot combined variables not has same type
print("The lucky number: " + str(1234))

# Global and local variable

# local variable
def someFunction():
    mystr = "ahihi"
    print(mystr)

someFunction()
print(mystr)

# global variable
def someFunction2():
    global mystr #global var
    mystr = "ahihi"
    print(mystr)

someFunction2()
print(mystr)

del mystr #delete mystr variable
print(mystr) # error because that value is removed