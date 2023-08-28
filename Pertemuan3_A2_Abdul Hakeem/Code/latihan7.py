z = [1, 3, 2, 4, 'Alice', 'Bob']
#z.sort()
#print(z)
# ^this errors out the script. to fix it, change the int into str by putting it between a "" or an ''.

print("Hello there!\nHow are you?\nI'm doing fine.")

multi_line = """Hello there!
How are you?
I'm fine."""
print(multi_line)

spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))