import pandas as pd 
import numpy as np
df=pd.DataFrame({'aileler':["a","b","c","a","b","c"],
                 'yas':[10,25,64,13,72,44],
                 'para':[53,261,355,488,153,611]},
                 columns=['aileler','yas','para'])
print(df)

print("-------------------------------------------")

a=df.groupby('aileler').mean()
b=df.groupby('aileler').filter(lambda x: x['yas'].mean()>30)
print(a)
print("-------------------------------------------")
print(b)
print("-------------------------------------------")