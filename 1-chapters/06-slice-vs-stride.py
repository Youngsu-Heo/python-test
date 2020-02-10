a = ['a', 'b','c','d','e','f','g','h']

# Test deep copy
print('\nd is shallow copy of a. so, both d and a reference the same address')
d = a
print(d == a, d is a)

d = a[:]
print(d == a, d is a)

# Test slice
print('\nb and c are new instances respectively, but each elements in them are shallow copys of a')
b = a[:3]
c = a[:3]

print(b)
print(c)
print(b == c, b is c)
print(b[0] is a[0], b[1] is a[1], b[2] is a[2])
print(b[0] is c[0], b[1] is c[1], b[2] is c[2])


# Test stride
print('\ntest stride')
x = a[::2]
y = a[::2]
print(x)
print(x==y, x is y)
print(x[0] is a[0], x[1] is a[2], x[2] is a[4])
print(x[0] is y[0], x[1] is y[1], x[2] is y[2])


