# import numpy as np
# import csv
#
# file_path = 'path/to/your/SalaryGender.csv'
# data = np.genfromtxt(file_path, delimiter=',', names=True, dtype=None, encoding=None)
#
# salary_array = data['Salary']
# gender_array = data['Gender']
# age_array = data['Age']
# phd_array = data['PHD']
#
#
# print("Salary Array:", salary_array)
# print("Gender Array:", gender_array)
# print("Gender Array:", age_array)
# print("Gender Array:", phd_array)

# QUESTION 2 CONTINUATION FROM QUESTION 1
# men_with_phd = data[(data['Gender'] == 1) & (data['PhD'] == 1)]
# women_with_phd = data[(data['Gender'] == 0) & (data['PhD'] == 1)]
#
# num_men_with_phd = len(men_with_phd)
# num_women_with_phd = len(women_with_phd)
#
# print("Number of men with a PhD:", num_men_with_phd)
# print("Number of women with a PhD:", num_women_with_phd)

# QUESTION 3
# import pandas as pd
#
# file_path = 'path/to/your/SalaryGender.csv'
#
# df = pd.read_csv(file_path)
#
# print("Original DataFrame:")
# print(df)
#
# age_phd_with_phd_df = df[df['PhD'] == 1][['Age', 'PhD']]
#
# print("\nDataFrame with 'Age' and 'PhD' columns for people with a PhD:")
# print(age_phd_with_phd_df)

# QUESTION 4
# import pandas as pd
# file_path = 'path/to/your/SalaryGender.csv'
# df = pd.read_csv(file_path)
# total_people_with_phd = df[df['PhD'] == 1].shape[0]
# print("Total number of people with a PhD:", total_people_with_phd)

# QUESTION 5
# import numpy as np
# arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
# counts = np.bincount(arr)
# print(counts[1:])

# QUESTION 6
# import numpy as np
# array_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# filtered_array = array_2d[array_2d > 5]
# print(filtered_array)

# QUESTION 7
# import numpy as np
# nan_array = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])
# filtered_array = nan_array[~np.isnan(nan_array)]
# print(filtered_array)

# QUESTION 8
# import numpy as np
# random_array = np.random.random((10, 10))
# min_value = np.min(random_array)
# max_value = np.max(random_array)
# print("Minimum value:", min_value)
# print("Maximum value:", max_value)

# QUESTION 9
# import numpy as np
# random_vector = np.random.random(30)
# mean_value = np.mean(random_vector)
# print("Mean value:", mean_value)


# QUESTION 10
# import numpy as np
# original_array = np.arange(11)
# original_array[(original_array >= 3) & (original_array <= 9)] *= -1
# print("Modified Array:", original_array)


# QUESTION 11
# import numpy as np
# random_array = np.random.random((3, 3))
# print("Original Array:")
# print(random_array)
# sorted_by_first_column = random_array[random_array[:, 0].argsort()]
# print("\nSorted by 1st column:")
# print(sorted_by_first_column)
# sorted_by_second_column = random_array[random_array[:, 1].argsort()]
# print("\nSorted by 2nd column:")
# print(sorted_by_second_column)
# sorted_by_third_column = random_array[random_array[:, 2].argsort()]
# print("\nSorted by 3rd column:")
# print(sorted_by_third_column)

# QUESTION 12
# import numpy as np
# four_dimensional_array = np.random.random((4, 3, 2, 5))
# print("Original Array:")
# print(four_dimensional_array)
# sum_over_last_two_axes = np.sum(four_dimensional_array, axis=(-2, -1))
# print("\nSum over the last two axes:")
# print(sum_over_last_two_axes)

# QUESTION 13
# import numpy as np
# random_array = np.random.random((3, 4))
# print("Original Array:")
# print(random_array)
# row_to_swap_1 = 0
# row_to_swap_2 = 2
# random_array[[row_to_swap_1, row_to_swap_2]] = random_array[[row_to_swap_2, row_to_swap_1]]
# print("\nArray after swapping rows:")
# print(random_array)

# QUESTION 14
# import numpy as np
# random_matrix = np.random.random((3, 3))
# print("Original Matrix:")
# print(random_matrix)
# matrix_rank = np.linalg.matrix_rank(random_matrix)
# print("\nMatrix Rank:", matrix_rank)

# QUESTION 15
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# file_path = 'your_data.csv'
# df = pd.read_csv(file_path)
#
# data_description = df.describe()
# print("Data Description:")
# print(data_description)
#
# grouped_data = df.groupby('school_rating')['reduced_lunch'].describe()
#
# correlation = df['reduced_lunch'].corr(df['school_rating'])
# print("\nCorrelation between 'reduced_lunch' and 'school_rating':", correlation)
#
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='reduced_lunch', y='school_rating', data=df)
# plt.title('Scatter Plot of school_rating vs. reduced_lunch')
# plt.xlabel('Percentage of Students on Reduced Lunch')
# plt.ylabel('School Rating')
# plt.show()
#
# correlation_matrix = df.corr()
# plt.figure(figsize=(12, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Correlation Matrix')
# plt.show()





