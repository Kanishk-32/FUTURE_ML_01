import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
df = pd.read_excel("data.xlsx")
print(df.head())
print(df.info())
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df = df.dropna()
df['year'] = df['InvoiceDate'].dt.year
df['month'] = df['InvoiceDate'].dt.month
df['day'] = df['InvoiceDate'].dt.day
df['dayofweek'] = df['InvoiceDate'].dt.dayofweek
df['hour'] = df['InvoiceDate'].dt.hour
df['Sales'] = df['Quantity'] * df['UnitPrice']
daily_sales = df.groupby(df['InvoiceDate'].dt.date)['Sales'].sum().reset_index()
daily_sales.columns = ['Date', 'Sales']
plt.figure(figsize=(10,5))
plt.plot(daily_sales['Date'], daily_sales['Sales'])
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
daily_sales['time_index'] = range(len(daily_sales))
daily_sales['month'] = pd.to_datetime(daily_sales['Date']).dt.month
daily_sales['dayofweek'] = pd.to_datetime(daily_sales['Date']).dt.dayofweek
X = daily_sales[['time_index', 'month', 'dayofweek']]
y = daily_sales['Sales']
model = LinearRegression()
model.fit(X, y)
try:
    future_days = int(input("Enter days (default 30): ") or 30)
except:
    future_days = 30
last_date = pd.to_datetime(daily_sales['Date']).max()
future_dates = pd.date_range(start=last_date, periods=future_days+1)[1:]
future_df = pd.DataFrame()
future_df['Date'] = future_dates
future_df['time_index'] = range(len(daily_sales), len(daily_sales) + future_days)
future_df['month'] = future_df['Date'].dt.month
future_df['dayofweek'] = future_df['Date'].dt.dayofweek
predictions = model.predict(future_df[['time_index', 'month', 'dayofweek']])
plt.figure(figsize=(10,5))
plt.plot(daily_sales['time_index'], y, label="Actual Sales")
plt.plot(range(len(daily_sales), len(daily_sales)+future_days), predictions, label="Forecast", linestyle='dashed')
plt.legend()
plt.title("Sales Forecast")
plt.show()
