a = ['a','b','c','d','e','f','g','h']

print(a[2:-2:2])     # ['c', 'e']

print('\nstride-slice:')
b = a[::2]
c = b[1:-1]
print(b)
print(c)


print('\nslice-stride:')
b = a[2:-2]
c = b[::2]

print(b)
print(c)
