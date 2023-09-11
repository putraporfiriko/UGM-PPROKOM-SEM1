data_count = int(input("How much data you want to input? "))
data_sum = 0

for i in range (0, data_count):
    data_input = int(input("Input the data: "))
    data_sum += data_input

data_avg = data_sum/data_count
print(data_avg)