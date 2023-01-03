import seaborn as sns
#aggregation:count(),first(),last(),mean(),median(),min(),max(),std(),var(),sum()
df=sns.load_dataset("planets")
a=df.head()#İlk beş veriyi gösterir.
b=df.shape
print(df)
print("---------------------")
print(a)
print("---------------------")
print(b)
print("---------------------")
c=df.mean()#Ortalamasını alır.
print(c)
d=df["year"].mean()#Ortalamasını alır.
print("Year Mean:",d)
print("---------------------")
e=df.count()#adetini verir.
print(e)
print("---------------------")
#Diğer fonksiyonları da bu şekilde kullanabiliriz.