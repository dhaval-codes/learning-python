# valid variable name casing
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(my_var, myvar2)

#  invalid variable name casing

2myvar = "John"
my-var = "John"
my var = "John"

# bellow line throws the error
print(2myvar)