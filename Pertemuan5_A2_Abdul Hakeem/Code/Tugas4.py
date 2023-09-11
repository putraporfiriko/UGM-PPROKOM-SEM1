data_act = int(input("How much data you want to input? "))
datalist = []

for i in range (0, data_act):
    datainput = int(input("Input the data: "))
    datalist.append(datainput)

datasum = sum(datalist)

dataavg = datasum / data_act
print(dataavg)