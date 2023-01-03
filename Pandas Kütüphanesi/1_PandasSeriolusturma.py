import pandas as pd

a=pd.Series([1,2,3,4,5,6,7,8,9])
print(a)
print("------------------------")
print(a.axes)
print("------------------------")
print(a.dtype)
print("------------------------")
print(a.size)
print("------------------------")
print(a.ndim)
print("------------------------")
print(a.values)
print("------------------------")
print(a.head(2))
print("------------------------")
print(a.tail(2))
print("------------------------")


sozluk={"ali":1,"ayse":2,"oya":3,"ahmet":4}
print(sozluk)
print("------------------------")
b=pd.Series(sozluk)
print(b)
print("------------------------")


c=pd.Series([66,77,21,45,92,35,48], index=["ali","ayse","oya",8,10,12,14])
print(c["ali":"oya"])
print("------------------------")

a=pd.Series([1,2,3,4,5,6,7,8,9])
d=pd.concat([a,a])
print(d)
print("------------------------")