
# MODULE 1 QUESTION 1
number = int(input("enter the number you want to look for its factor\n"))
num_list = []
for num in range(1, number + 1):
    if number % num == 0:
        num_list.append(num)
        if num % 2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
print(f"The factors of {number} = {num_list}")


# MODULE 1 QUESTION 2
word = list(input("enter a word\n"))
sortedWord = sorted(word)
finalWord = ""
for i in sortedWord:
    finalWord += i
print(finalWord)


# MODULE 1 QUESTION 3
my_list = []
for number in range(1000, 3001):
    even_digits = all(int(digit) % 2 == 0 for digit in str(number))

    if even_digits:
        my_list.append(str(number))

number1 = ",".join(my_list)
print(number1)

# MODULE 1 QUESTION 4
enteredText = input("Enter a word mixed with numbers\n")
textList = []
numberList = []
for i in enteredText:
    if i.isdigit():
        numberList.append(i)
    else:
        textList.append(i)
print(f"LETTERS: {len(textList)}")
print(f"DIGITS: {len(numberList)}")

# MODULE 1 QUESTION 5
numEntered = input("Enter the number you want to test if it is a Palindromic number\n")
newNumber = ""
for i in numEntered:
    newNumber = i + newNumber

if newNumber == numEntered:
    print(f"{numEntered} is Palindromic")
else:
    print(f"{numEntered} is not Palindromic")



#     BY ASUE DERICK















