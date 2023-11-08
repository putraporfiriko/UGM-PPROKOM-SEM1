numlist = str(input())
separatornum = int(input())
sum = 0
numlist = numlist.split(" ")
    
for i in numlist:
    if int(i) % separatornum == 0:
        sum += int(i)

print(sum)