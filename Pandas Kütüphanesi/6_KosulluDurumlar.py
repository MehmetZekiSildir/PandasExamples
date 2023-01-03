import numpy as np
import pandas as pd 


a=np.random.randint(1,30, size=(10,3))
b=pd.DataFrame(a,columns=["col1","col2","col3"])
print(a)
print("---------------------------------------")
print(b)
print("---------------------------------------")
print(b["col2"])
print("---------------------------------------")
print(b["col2"][0:2])
print("---------------------------------------")

#Koşullu durum yazarsak 

print(b[b.col2 > 20])
print("--------------------------------------")
print(b[(b.col2 < 20) & (b.col1 >10)] )
