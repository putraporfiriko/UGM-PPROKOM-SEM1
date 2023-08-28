print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))

print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))

print('Hello world!'.startswith('Hello World!'))
print('Hello World!'.endswith('Hello World!'))

print('Hello'.rjust(10))
print('Hello'.rjust(20))

print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.ljust(20, '*'))
print('Hello'.ljust(20, '-'))

print('Hello'.center(20))
print('Hello'.center(20, '='))