import pandas as pd

df = pd.read_csv('./revenue.csv')
events = {'Events': df.EventName.unique()}

df2 = pd.DataFrame(events)
df2['Quantity'] = 0
df2['Price'] = 0
df2['Merchandise_Sales'] = 0
df2['Concession_Sales'] = 0
for index, row in df2.iterrows():
	rows = df[df.EventName == row['Events']]
	df2.ix[index, 'Quantity'] = rows['Quantity'].sum()
	df2.ix[index, 'Price'] = rows['Price'].sum()
	df2.ix[index, 'Merchandise_Sales'] = rows['Merchandise_Sales'].sum()
	df2.ix[index, 'Concession_Sales'] = rows['Concession_Sales'].sum()

print(df2)

df2.to_csv('sums.csv')

