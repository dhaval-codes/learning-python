# python numbers
import random #to generate random no

# there are 3 number types in python

x = 1 #int
y = 2.3 #float
z = 1j #complex

a = 23
print(type(a))
b = 2348342387642387483
print(type(b))
c = -334923
print(type(c))

# a,b,c all are int types

d = 1.23
print(type(d))
e = 1.0
print(type(e))
f = - 34.23
print(type(f))
g = 35e24
print(type(g))
h = 12E4 # no idea if E = e or it's different
print(type(h))

# d,e,f,g,h all are float types

i = 3+5j
print(type(i))
j = 5j
print(type(j))
k = -23j
print(type(k))

# i,j,k are all complex types

#type conversion

#convert from init to float
a = float(x)
print(a)

#convert from float to int
b = int(y)
print(b)

#convert from int to complex
c = complex(x)
print(c)

print(random.randrange(1,100))