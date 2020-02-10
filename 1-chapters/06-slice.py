
a = ['a', 'b','c','d','e','f','g','h']

print('first four:', a[:4])
print('last four:', a[-4:])
print('middle two:', a[3:-3])

b = a[:]    # deep copy
print('b == a:', b == a)
print('b is a:', b is a)

b = a       # shallow copy
print('b == a:', b == a)
print('b is a:', b is a)


c = a[:4]
print(c)
print('c == a:', c == a)
print('c is a:', c is a)
