datact = int(input("How much data you want to input? "))
datalist = []

for i in range (0, datact):
    datainput = int(input("Input the data: "))
    datalist.append(datainput)

datasum = sum(datalist)

dataavg = datasum / datact
print(dataavg)    
