# #QUESTION 1
# # we can use the pythagoreans theorem \[ d = \sqrt{{x^2 + y^2}} \]
#
# import math
#
# def calculate_distance(movements):
#     x, y = 0, 0
#
#     for move in movements:
#         direction, steps = move.split()
#         steps = int(steps)
#
#         if direction == "UP":
#             y += steps
#         elif direction == "DOWN":
#             y -= steps
#         elif direction == "LEFT":
#             x -= steps
#         elif direction == "RIGHT":
#             x += steps
#
#     distance = math.sqrt( x**2 + y** 2)
#     return distance
#
#
# # Example usage
# movements = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
# result = calculate_distance(movements)
# print("The distance from the origin is:", result)
#
#
# #QUESTION 2
#
# def binary_search(sorted_list, target):
#     low, high = 0, len(sorted_list) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         mid_value = sorted_list[mid]
#
#         if mid_value == target:
#             return mid
#         elif mid_value < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
# # Example usage
# xyz_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# target_value = 60
#
# result = binary_search(xyz_data, target_value)
#
# if result != -1:
#     print(f"The data {target_value} is found at index {result}.")
# else:
#     print(f"The data {target_value} is not found in the list.")
#
#
# #QUESTION 3
#
# import time
#
# def is_dark_outside():
#     current_time = time.localtime()
#     current_hour = current_time.tm_hour
#
#     night_start = 19
#     night_end = 6
#
#     if night_start <= current_hour or current_hour <= night_end:
#         return True
#     else:
#         return False
#
# # Example usage
# if is_dark_outside():
#     print("It is currently dark outside.")
# else:
#     print("It is currently not dark outside.")
#
#
# #QUESTION 4
#
# import math
#
# def haversine(lat1, lon1, lat2, lon2):
#
#     R = 6371.0
#
#
#     lat1_rad = math.radians(lat1)
#     lon1_rad = math.radians(lon1)
#     lat2_rad = math.radians(lat2)
#     lon2_rad = math.radians(lon2)
#
#
#     dlat = lat2_rad - lat1_rad
#     dlon = lon2_rad - lon1_rad
#
#     # Haversine formula
#     a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#
#
#     distance = R * c
#
#     return distance
#
# # Example usage
# latitude1, longitude1 = 37.7749, -122.4194
# latitude2, longitude2 = 34.0522, -118.2437
#
# distance = haversine(latitude1, longitude1, latitude2, longitude2)
# print(f"The distance between the two locations is approximately {distance:.2f} kilometers.")
#
#
# #QUESTION 5
#
# class BankAccount:
#     def __init__(self, balance, password):
#         self.balance = balance
#         self.password = password
#
#     def display_menu(self):
#         print("1. Cash Withdrawal")
#         print("2. Cash Credit")
#         print("3. Change Password")
#         print("4. Exit")
#
#     def withdraw_cash(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawal successful. Remaining balance: {self.balance}")
#         else:
#             print("Invalid amount or insufficient balance.")
#
#     def credit_cash(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Credit successful. Updated balance: {self.balance}")
#         else:
#             print("Invalid amount for credit.")
#
#     def change_password(self, new_password):
#         self.password = new_password
#         print("Password changed successfully.")
#
# # Example usage
# def main():
#     # Initialize bank account with balance and password
#     account = BankAccount(balance=1000, password="pass123")
#
#     while True:
#         account.display_menu()
#         choice = input("Enter your choice (1-4): ")
#
#         if choice == "1":
#             amount = float(input("Enter the withdrawal amount: "))
#             account.withdraw_cash(amount)
#         elif choice == "2":
#             amount = float(input("Enter the credit amount: "))
#             account.credit_cash(amount)
#         elif choice == "3":
#             new_password = input("Enter the new password: ")
#             account.change_password(new_password)
#         elif choice == "4":
#             print("Exiting the bank system. Thank you!")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")
#
# if __name__ == "__main__":
#     main()
#
#
# #QUESTION 6
#
# result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
# print(','.join(result))


#QUESTION 7

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# number = int(input("Enter a number to calculate its factorial: "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")


#QUESTION 8

# import math
#
# def calculate_q_values(input_sequence):
#
#     C = 50
#     H = 30
#
#     input_values = [int(value) for value in input_sequence.split(',')]
#     result = [int(math.sqrt((2 * C * value) / H)) for value in input_values]
#
#     return result
#
# input_sequence = input("Enter a comma-separated sequence of D values: ")
# output_values = calculate_q_values(input_sequence)

# print("Output:", ','.join(map(str, output_values)))

#QUESTION 9

# def generate_2d_array(X, Y):
#     # Use list comprehension to generate the 2-dimensional array
#     result = [[i * j for j in range(Y)] for i in range(X)]
#
#     return result
#
# X, Y = map(int, input("Enter two digits (comma-separated): ").split(','))
# output_array = generate_2d_array(X, Y)
#
# row1 = []
# print("Output:")
# for row in output_array:
#     row1.append(row)
# print(row1)


#QUESTION 10

# input_sequence = input("Enter a comma-separated sequence of words: ")
#
# words = input_sequence.split(',')
#
# sorted_words = sorted(words)
#
# output_sequence = ','.join(sorted_words)
# print("Output:", output_sequence)

#QUESTION 11

# input_lines = input("Enter a sequence of lines (press Enter after each line, and type 'end' to finish):\n")
#
# lines = []
# while input_lines.lower() != 'end':
#     lines.append(input_lines)
#     input_lines = input()
#
# capitalized_lines = [line.upper() for line in lines]
#
# print("Output:")
# for line in capitalized_lines:
#     print(line)

#QUESTION 12
# input_words = input("Enter a sequence of whitespace-separated words: ")
# words = input_words.split()
# unique_sorted_words = sorted(set(words))
# print("Output:", ' '.join(unique_sorted_words))

#QUESTION 13
# def check_divisibility_by_5(binary_sequence):
#     binary_numbers = binary_sequence.split(',')
#
#     divisible_by_5 = []
#
#     for binary_number in binary_numbers:
#         decimal_number = int(binary_number, 2)
#
#         if decimal_number % 5 == 0:
#             divisible_by_5.append(binary_number)
#
#     result_sequence = ','.join(divisible_by_5)
#     print("Output:", result_sequence)
#
# input_sequence = input("Enter a sequence of whitespace-separated words:")
# check_divisibility_by_5(input_sequence)


#QUESTION 14

# def count_upper_lower(sentence):
#     upper_count = 0
#     lower_count = 0
#
#     for char in sentence:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
#     print("UPPER CASE", upper_count)
#     print("LOWER CASE", lower_count)
# input_sentence = input("Enter a sequence of words:")
# count_upper_lower(input_sentence)

#QUESTION 16

# import math
#
# numbers = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# result_fsum = math.fsum(numbers)
#
# result_sum = sum(numbers)
#
# print("Using math.fsum:", result_fsum)
# print("Using built-in sum:", result_sum)

