#Python - Global Variables

x = "awesome" #it's by default global variabe

def myfunc():
    x = "fantastic" #since x is defined inside a func, it's not gloabally accessable
    print("python is " + x)

myfunc()

print("python is " + x)

def merafunc():
    global y
    y = "cool"

merafunc()

print("python is " + y)#pics variable y from inside a function