import pandas as pd

data=[1,2,3,4,5]
series=pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# print(series)

data1={
    'Name': ['Alice', None, 'Charlie'],
    'Age': [24, 84, 64],
    'City':['NY', "LA", None]
}
df=pd.DataFrame(data1)
# print(df.drop('Name', axis=1))

filter=df[df['Age']>30]

drop=df.fillna('fuck')
print(drop)

