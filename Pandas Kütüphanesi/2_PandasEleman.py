import numpy as np
import pandas as pd

a=np.array([24,56,321,85,72])
b=pd.Series(a)
print(a)
print("----------------------")
print(b)
print("----------------------")
print(b[0:4])
print("----------------------")


abc=pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print(abc)
print("----------------------")
print(abc.index)
print("----------------------")
print(list(abc.items()))
print("----------------------")
print(abc.keys)
print(abc.values)


print("ali" in abc)
print("----------------------")
print("a" in abc)
print("----------------------")


liste=["a","b","c"]
print(abc[liste])
print("----------------------")
abc["a"]=10
print(abc)
print("----------------------")