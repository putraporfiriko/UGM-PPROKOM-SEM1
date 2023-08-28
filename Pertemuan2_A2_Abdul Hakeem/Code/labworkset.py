# set integer
my_set = {1,2,3}
print(my_set)

#set dengan fungsi set()
my_set = set([1,2,3])
print(my_set)

# set data campuran
my_set = {1,2.0,"Python",(3,4,5)}
print(my_set)

#bila kita mengisi duplikasi, set akan menghilangkan salah satu
#output: {1,2,3}
my_set = {1,2,2,3,3,3}
print(my_set)

#set tidak bisa berisi anggota list
#contoh berikut akan menghasilkan error TypeError
my_set = {1,2,[3,4,5]}