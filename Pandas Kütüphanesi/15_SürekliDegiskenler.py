import seaborn as sns

df=sns.load_dataset("planets")
print(df)
print("---------------------")
print(df.head())
print("---------------------")
con_df=df.select_dtypes(include=["float64","int64"])
print(con_df)
print("---------------------")
print(con_df.describe().T)