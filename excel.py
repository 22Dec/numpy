import pandas as pd

data=pd.read_excel(r'C:/Users/yhjfl/Desktop/1.xlsx')
print(data)
data.to_csv('1.pickle')