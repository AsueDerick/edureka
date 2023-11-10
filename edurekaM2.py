# # SEQUENCE AND FILE OPERATION ASSIGNMENT CASE STUDY 1
# # QUESTION 1:
# print("The output is 4")
#
# # QUESTION 2
# list1 = ["john","peter"]
# print(f"The output is the list {list1}")

# QUESTION 3




# QUESTION 4
# a = [4, 7, 3, 2, 5, 9]
# for i in a:
#     print(f"{a.index(i)} is {i}")

# QUESTION 5
# word = []
# list2 = list(input("enter a word \n"))
# for i in list2:
#     if list2.index(i) % 2 ==0 :
#         word.append(i)
# result = "".join(word)
# print(result)

# QUESTION 6
# text = input("Enter a text\n")
# reversed_text = text[::-1]
# print(f"Reversed text: {reversed_text}")

# QUESTION 7
# text = input("enter a text\n")
# set1 = sorted(set(text))
# print(set1)
# for i in set1:
#     print(f"{i}, {text.count(i, 0, len(text))}")

# QUESTION 8
# list1 = [1, 3, 6, 78, 35, 55]
# list2 = [12, 24, 35, 24, 88, 120, 155]
# set1 = set(list1)
# set2 = set(list2)
# combined_list = set1 & set2
# print(combined_list)

# QUESTION 9 set is sorted for better presentation
# original_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# original_set = sorted(set(original_list))
# new_list = list(original_set)
# reversed_list = new_list[::-1]
# print(new_list)
# print(reversed_list)

# QUESTION 10
# list1 = [12, 24, 35, 24, 88, 120, 155]
# list2= []
# for i in list1:
#     if i == 24:
#         del (i)
#     else:
#         list2.append(i)
# print(list2)

# QUESTION 11
# list1 = [12, 24, 35, 70, 88, 120, 155]
# list2 = []
# for i in list1:
#     index1 = list1.index(i)
#     if index1 == 0 or index1 == 4 or index1 == 5:
#         del (i)
#     else:
#         list2.append(i)
# print(list2)

# QUESTION 12, THE QUESTION IS NOT THAT CLEAR "REMOVING DELETE TYPO ERROR" I WENT WITH AFTER REMOVING
# list1 = [12, 24, 35, 70, 88, 120, 155]
# list2 = []
# for i in list1:
#     if i % 5 == 0 and i % 7 == 0:
#         del (i)
#     else:
#         list2.append(i)
# print(list2)

# QUESTION 13
