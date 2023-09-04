x = str(input(""))

x = x.lower()

acount = x.count("a")
icount = x.count("i")
ucount = x.count("u")
ecount = x.count("e")
ocount = x.count("o")


voccount = acount+icount+ucount+ecount+ocount
print(voccount)