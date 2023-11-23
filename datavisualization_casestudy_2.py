import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('BigMartSalesData.csv')

sales_data['InvoiceDate'] = pd.to_datetime(sales_data['InvoiceDate'])

sales_data['YearMonth'] = sales_data['InvoiceDate'].dt.to_period('M')

plt.figure(figsize=(10, 6))
plt.plot(sales_data.groupby('YearMonth')['Amount'].sum(), marker='o', linestyle='-', color='b')
plt.title('Total Sales Per Month - 2011')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(sales_data.groupby('YearMonth')['Amount'].sum().index.astype(str),
        sales_data.groupby('YearMonth')['Amount'].sum(), color='g')
plt.title('Total Sales Per Month (Bar Chart) - 2011')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

plt.figure(figsize=(8, 8))
country_sales = sales_data.groupby('Country')['Amount'].sum()
plt.pie(country_sales, labels=country_sales.index, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Sales Distribution by Country - 2011')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(sales_data['InvoiceNo'], sales_data['Amount'], color='r', alpha=0.5)
plt.title('Scatter Plot for Invoice Amounts')
plt.xlabel('Invoice Number')
plt.ylabel('Amount')
plt.show()
