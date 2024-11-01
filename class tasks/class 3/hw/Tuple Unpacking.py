#Tuple Unpacking

my_tuple = (2,9,7,4,12)
a,b,c,d,e = my_tuple
print(a,b,c,e)

my_tuple2 = ('john', 20, 5.5,'asif', True)
name, age, *others = my_tuple2

print(name)
print(age)
print(others)

print("==================")

my_tuple3 = ('john', 20, 5.5,'asif', True)
name, *others, age = my_tuple2

print(name)
print(age)
print(others)