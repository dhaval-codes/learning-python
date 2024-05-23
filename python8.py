#Build-in Data Types

# text-type: str
# Numeric type: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types : set, frozenset
# Boolean type: bool
# Binary Type: bytes, bytearray, memoryview
# none type: NoneType

x = 5
print(type(x))

a = "hello world"
print(type(a))

b = 20.5
print(type(b))

c = 1j #not sure how this represents complex no
print(type(c))

d = ["apple", "banana", "cherry"] #list
print(type(d))

e = ("apple", "banana", "cherry") #tuple
print(type(e))

f = range(6) # range from 0 to 6
print(type(f))

g = {
    "name": "Dhaval",
    "age": 19,
    "university": "IIT Madras",
    "degree": "Data Science and AI"
} #object / dictioanry
print(type(g))

h = {"apple", "banana", "cherry"} #set
print(type(h))

i = frozenset({"apple", "banana", "cherry"}) #frozenset
print(type(i))

j = True
print(type(j))

k = b"hello" #bytes idk how
print(type(k))

l = bytearray(5)
print(type(l))

m = memoryview(bytes(5)) #gives memory address
print(type(m))

n = None
print(type(n))




