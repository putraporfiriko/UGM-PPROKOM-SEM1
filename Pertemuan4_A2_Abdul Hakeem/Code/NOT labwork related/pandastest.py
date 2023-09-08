from pandas import *
from sys import *

xls = sys.argv[1]
df = xls.parse(xls.sheet_names[0])
dfdict = df.to_dict(df)

print(dfdict)   
