tup = 'Hello'
print(len(tup))
print(tup.__class__)
#No trailing comma so tup defaults to string
tup = 'Hello',
print(len(tup))
print(tup.__class__)
#Trailing comma makes tup a tuple
#Unpacking to wildcard