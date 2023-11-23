# QUESTION 1
# import pandas as pd
# import matplotlib.pyplot as plt
# file_path = 'hurricanes_data.csv'
# df = pd.read_csv(file_path)
# x_values = df['Year']
# y_values = df['Number of Hurricanes']
# plt.figure(figsize=(10, 6))
# plt.bar(x_values, y_values, color='blue')
# plt.title('Number of Hurricanes in the United States (Atlantic Coast)')
# plt.xlabel('Year')
# plt.ylabel('Number of Hurricanes')
# plt.grid(axis='y')
# plt.show()

# QUESTION 2
# import pandas as pd
# import matplotlib.pyplot as plt
#
# file_path = 'your_dataset.csv'
# df = pd.read_csv(file_path)
#
# sf_data = df[df['City'] == 'San Francisco']['Temperature']
# moscow_data = df[df['City'] == 'Moscow']['Temperature']
#
# plt.figure(figsize=(10, 6))
# plt.hist(sf_data, bins=20, alpha=0.5, label='San Francisco', color='blue')
# plt.hist(moscow_data, bins=20, alpha=0.5, label='Moscow', color='green')
#
# plt.title('Temperature Histogram for San Francisco and Moscow (2014-2015)')
# plt.xlabel('Temperature (°C)')
# plt.ylabel('Frequency')
# plt.legend()
# plt.show()

# QUESTION 3
# import pandas as pd
# import matplotlib.pyplot as plt
#
# file_path = 'your_dataset.csv'
# df = pd.read_csv(file_path)
#
# manufacturer_counts = df['Manufacturer'].value_counts()
#
# plt.figure(figsize=(8, 8))
# plt.pie(manufacturer_counts, labels=manufacturer_counts.index, autopct='%1.1f%%', startangle=90)
# plt.title('Number of Models Released by Manufacturer')
# plt.axis('equal')
# largest_manufacturer = manufacturer_counts.idxmax()
# print(f"The manufacturer with the largest releases is: {largest_manufacturer}")
# plt.show()

# QUESTION 4
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("assignment.csv")
#
# description = df.describe()
# print(description)
#
# new_df = df[['name', 'net_price', 'date']].groupby('name').sum().reset_index()
#
# plt.bar(new_df['name'], new_df['net_price'])
# plt.xlabel('Customer Name')
# plt.ylabel('Total Sales')
# plt.title('Total Sales by Customer')
# plt.show()

# QUESTION 5
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# X = [1, 2, 3, 4]
# y = [20, 21, 20.5, 20.8]
# plt.plot(X, y)
# plt.show()
#
# plt.plot(X, y, marker='o', linestyle='--', color='r')
# plt.show()
#
# plt.plot(X, y, marker='o', linestyle='--', color='r')
# plt.axis([0, 5, 19, 22])
# plt.show()
#
# plt.plot(X, y, marker='o', linestyle='--', color='r')
# plt.title('Simple Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#
# y_error = [0.12, 0.13, 0.2, 0.1]
# plt.errorbar(X, y, yerr=y_error, fmt='o-', color='g')
# plt.title('Plot with Error Bars')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#
# plt.figure(figsize=(4, 5), dpi=100)
# plt.plot(X, y, marker='o', linestyle='--', color='r')
# plt.title('Adjusted Plot DPI')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#
# plt.figure(figsize=(4, 5), dpi=100)
# plt.plot(X, y, marker='o', linestyle='--', color='r')
# plt.title('Adjusted Plot DPI', fontsize=14)
# plt.xlabel('X-axis', fontsize=12)
# plt.ylabel('Y-axis', fontsize=12)
# plt.show()
#
# np.random.seed(42)
# random_x = np.random.rand(50)
# random_y = np.random.rand(50)
# plt.scatter(random_x, random_y)
# plt.title('Scatter Plot of 50 Random Values')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#
# data = {
#     'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#     'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
#     'female': [0, 1, 1, 0, 1],
#     'age': [42, 52, 36, 24, 73],
#     'preTestScore': [4, 24, 31, 2, 3],
#     'postTestScore': [25, 94, 57, 62, 70]
# }
# df = pd.DataFrame(data)
#
# plt.scatter(df['preTestScore'], df['postTestScore'], s=df['age'])
# plt.title('Scatter Plot with Size Determined by Age')
# plt.xlabel('preTestScore')
# plt.ylabel('postTestScore')
# plt.show()
#
# colors = df['female'].map({0: 'blue', 1: 'red'})
# plt.scatter(df['preTestScore'], df['postTestScore'], s=300, c=colors)
# plt.title('Scatter Plot with Size and Color Determined by Gender')
# plt.xlabel('preTestScore')
# plt.ylabel('postTestScore')
# plt.show()



