import pandas as pd
df=pd.DataFrame({'aileler':["a","b","c","a","b","c"],
                 'yas':[10,25,64,13,72,44],
                 'para':[53,261,355,488,153,611]},
                 columns=['aileler','yas','para'])
print(df)
print("-----------------------------------------")
a=df.iloc[0:3,1:3]
print(a)
print("-----------------------------------------")
b=a.transform(lambda x: x-x.mean())
print(b)

