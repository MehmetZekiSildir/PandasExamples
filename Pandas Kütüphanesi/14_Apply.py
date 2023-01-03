import pandas as pd
import numpy as np 
df=pd.DataFrame({'aileler':['a','b','c','d','e','f'],
                 'yas':[10,25,64,13,72,44],
                 'para':[53,261,355,488,153,611]},
                 columns=['aileler','yas','para'])
print(df)
print("-----------------------------------------")

a=df.groupby('aileler').apply(np.mean)
print("-----------------------------------------")
