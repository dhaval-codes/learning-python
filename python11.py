# strings

print("hello")
print('hello') # double quotes and single quotes are same

print("It's allright")
print('His name is "Dhaval"') # just starting and ending quotes should be same

a = "hello" # single line string
print(a)

b = """Lorem ipsumkjfnn vkfjnvkv knfkvf kdfnvkd kdf vkv ,d kfvk fkvr vkmf k vktr vkf irf krk vkf f vi vk rk v
vk krvk 
vkr vkr
krf vrv
nf vkrgkrgdfvknglnvknkgnrnvkngt""" # works with 3 single quotes

print(b)

# strings are arrays

var = "Hello World"
print(var[1]) # prints 'e'

# looping through string

for x in 'banana':
    print(x)

name = "Dhaval J Prasad"
print(len(name)) # returns string's length, including spaces

#checking a phrase in string

txt = "The best things in life are free!"
print("free" in txt)# returns a bool

if "best" in txt:
    print("yes, 'best' is there in the sentence")

# check if not
print("expensive" not in txt)# return a bool

if "expensive" not in txt:
    print("'expensive' is not in the text")