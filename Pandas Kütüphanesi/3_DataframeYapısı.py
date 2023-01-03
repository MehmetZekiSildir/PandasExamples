import pandas as pd
import numpy as np


liste=[10,20,30,40,50,60,70,80]
a=np.arange(1,10).reshape((3,3))
print(a)
print("------------------------")
b=pd.DataFrame(a,columns=["ilk","ikinci","ücüncü"])
#DataFrame özellikle machine learning,
#data processing ve artificial intelligence alanlarında oldukça
#sık kullanılır.
print(b)
print("------------------------")
b.columns=("first","second","third")
#Burada kolon adlarını değiştirmiş olduk.
print(b)
print("-------------------------")
print(type(b))
print("-------------------------")
print(b.axes)
print("-------------------------")
print(b.shape)
print("-------------------------")
print(b.ndim)
print("-------------------------")
print(b.size)
#values fonksiyonu dönüsüm isleri yapar.
print(type(b.values))
