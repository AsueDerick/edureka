# import csv
# import re
#
# class CustomerNotAllowedException(Exception):
#     pass
#
#
# class Customer:
#     def __init__(self, title, first_name, last_name, email, phone):
#         self.title = title
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#
# class Order:
#     def __init__(self, customer, product_name, product_code):
#         self.customer = customer
#         self.product_name = product_name
#         self.product_code = product_code
#
#
# def create_order(customer, product_name, product_code):
#     if customer.blacklisted == 1:
#         raise CustomerNotAllowedException("Customer is not allowed to create an order.")
#
#     order = Order(customer, product_name, product_code)
#     return order
#
#
# def read_and_convert_data(file_path):
#     customers = []
#     with open(file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#
#             match = re.match(r'(?P<title>\w+)\.\s(?P<first_name>\w+)\s(?P<last_name>\w+)', row['Name'])
#             if match:
#                 title = match.group('title')
#                 first_name = match.group('first_name')
#                 last_name = match.group('last_name')
#             else:
#                 title = first_name = last_name = None
#
#             customer = Customer(title, first_name, last_name, row['Email'], row['Phone'])
#
#             customer.blacklisted = int(row['Blacklisted'])
#
#             customers.append(customer)
#
#     return customers
#
# file_path = 'FairDealCustomerData.csv'
# goodskart_customers = read_and_convert_data(file_path)
#
# try:
#     order = create_order(goodskart_customers[0], "Sample Product", "123")
#     print("Order created successfully.")
# except CustomerNotAllowedException as e:
#     print(f"Exception: {e}")
message = "Hello,\n\tWorld!\v\tHow are you?\n\a\a\a"

print(message)