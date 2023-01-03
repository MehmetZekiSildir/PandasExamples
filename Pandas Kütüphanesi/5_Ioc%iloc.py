import pandas as pd
import numpy as np 
a=np.random.randint(1,30,size=(10,3))
print(a)
print("----------------------------")
b=pd.DataFrame(a,columns=["col1","col2","col3"])
print(b)
print("----------------------------")

#loc:tanımladığı haliyle seçim yapar.Slicing veya indexten farklı olarak son değeri de dahil eder.
c=b.loc[0:5]
print(c)
print("----------------------------")

#iloc:indexleme mantığı ile seçim yapar.
d=b.iloc[0:5]
print(d)
print("----------------------------")



