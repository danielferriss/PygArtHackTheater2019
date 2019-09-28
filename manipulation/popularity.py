import pandas as pd


df = pd.read_csv('../datasets/gross_revenue_by_event.csv')
df['Revenue Num'] = df['Gross Revenue'].replace('[^.0-9]', '', regex=True).astype(float)

revenue = df['Revenue Num'].sum()
df['Portion of Total'] = df['Revenue Num'] / revenue
df['Popularity Score'] = 1 + pd.cut(df['Portion of Total'],bins=100, labels=False)

df.to_csv('test.csv')