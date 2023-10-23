x = str(input())
y = str(input())

x_list = list(x)

# replace the vocals with y
for i in range(len(x_list)):
    if x_list[i] in ['a', 'i', 'u', 'e', 'o']:
        x_list[i] = y

for i in x_list:
    print(i, end="")