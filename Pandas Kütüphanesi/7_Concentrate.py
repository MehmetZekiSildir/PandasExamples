import numpy as np
import pandas as pd

a=np.random.randint(1,30,size=(10,3))
b=pd.DataFrame(a,columns=["col1","col2","col3"])
print(a)
print("---------------------------------------")
print(b)
print("---------------------------------------")

c=b+50
print(c)
print("---------------------------------------")
d=pd.concat([b,c])
print(d)
print("---------------------------------------")