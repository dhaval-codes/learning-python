#format strings

age = 36
# we can't combine two data types
# txt = "My name is John, I am" + age

#f-string: it's simple used to format strings

txt = f"My name is John, I am {age}"
print(txt)

# yet another example
price = 59
txt2 = f"The price is {price} dollars"
print(txt2)

txt3 = f"The price is {price:.2f} dollars" # adds 2 decimal places
print(txt3)

# placeholder can have codes for math problems or returning value func
txt4 = f"The price is {20 * 56} dollars"
print(txt4)