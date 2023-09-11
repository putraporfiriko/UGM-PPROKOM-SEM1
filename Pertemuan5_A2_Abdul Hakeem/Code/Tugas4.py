datact = int(input("How much data you want to input? "))
datalist = []


for i in range (0, datact):
    datainput = int(input("Input the data: "))
    datalist.append(datainput)
    print(datalist)
# datalen = len(datalist) # cant put this early, because it'll register as 0 # don't need this, just use datact

datasum = sum(datalist)


dataavg = datasum / datact
print(dataavg)    
