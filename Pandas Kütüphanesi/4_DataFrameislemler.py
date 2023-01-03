import numpy as np
import pandas as pd
n1=np.random.randint(10,size=5)
n2=np.random.randint(10,size=5)
n3=np.random.randint(10,size=5)

dictionary={"a":n1,"b":n2,"c":n3}
ps=pd.DataFrame(dictionary)
print(ps)
print("------------------------")
print(ps.index)
print("------------------------")
ps.index=["q","w","e","r","t"]
print("------------------------")
print(ps)
print("------------------------")
a=ps.drop("q", axis=0)
print(a)
print("------------------------")
print("a" in ps)
print("------------------------")

f=["a","b","e"]

for i in f:
    print(i in ps)

ps["d"]=np.array([1,2,3,4,5])#ps dataframe e bir array eklemesi yaptık ve sütunu d olarak adlandırdık.
print(ps)


