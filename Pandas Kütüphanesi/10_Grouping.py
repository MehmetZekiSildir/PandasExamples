import pandas as pd 
import seaborn as sns
df=pd.DataFrame({'gruplar':["a","b","c","a","b","c"],'veriler':[3,8,15,29,45,62]},columns=['gruplar','veriler'])
print(df)
print("--------------")
a=df.groupby('gruplar').mean()#Verilen kolon için gruplandırma yapar.
print(a)
print("--------------")


df_2=sns.load_dataset("planets")
ilk_bes=df_2.head()
print(ilk_bes)
print("--------------")
c=df_2.groupby('method').mean().describe().T#Açıklaması ile verir describe() metodu.T ise transpose alır.
print(c)