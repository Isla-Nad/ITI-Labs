
# def generateList(length, start):
#     lst = []
#     for num in range(start, start + length):
#         lst.append(num)
#     return lst
# while True:
#     start=input("please enter the start of the list you want to generate: ")
#     length=input("Please enter the length of the list you want to generate: ")
#     if start.isdigit() and length.isdigit():
#         start=int(start)
#         length=int(length)
#         break
#     else:
#         print("please enter a valid integer")

# print(generateList(length, start))

# # ================================================================

# def fizzBuzz(num):
#     if num % 3 == 0 and num % 5 == 0 :
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "buzz"
#     elif num % 3 == 0:
#         return "Fizz"
    
# print(fizzBuzz(30))

# # ================================================================

# def reverseStr(string):
#     return string[::-1]

# str=input("Please enter a string to reverse: ")

# print(reverseStr(str))

# # ================================================================

# import re

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email)

# while True:
#     user_name = input("Enter your name: ").strip()
#     if user_name.isalpha():
#         break
#     else:
#         print("Please enter a valid name.")

# while True:
#     user_email = input("Enter your email: ").strip()
#     if is_valid_email(user_email):
#         break
#     else:
#         print("Please enter a valid email address.")

# print(f"Name: {user_name}")
# print(f"Email: {user_email}")

# # ================================================================

# def longest_str(str):
#     longest_substr = ''
#     current_substr = str[0]

#     for i in range(1, len(str)):
#         if str[i] >= str[i - 1]:
#             current_substr += str[i]
#         else:
#             if len(current_substr) > len(longest_substr):
#                 longest_substr = current_substr
#             current_substr = str[i]

#     if len(current_substr) > len(longest_substr):
#         longest_substr = current_substr

#     return longest_substr

# print(longest_str("1234124561"))

# # ================================================================

# total = 0
# count = 0

# while True:

#     num=input("please enter a num (enter 'done' to show results): ")

#     if num.lower() == "done":
#         break

#     if num.isdigit():
#         num = int(num)
#         total+=num
#         count+=1
#     else:
#         print("Invalid input. Please enter a valid number or 'done'.")

# if count > 0:
#     average = total / count
#     print(f"Total: {total}")
#     print(f"Count: {count}")
#     print(f"Average: {average}")
# else:
#     print("No valid numbers entered.")

# # ================================================================

# import random

# words = ["islam","ahmed","eman","glal","noha","hamed","mohamed"]
# random_word = random.choice(words)

# guessed_letters = []
# word_guessed = ["_"] * len(random_word)

# player_name = input("Enter your name: ")
# print(f"Hello, {player_name}! Let's play Hangman.")

# i=0
# while i<7:
#     print(" ".join(word_guessed))
#     guess = input("Guess a letter: ").lower()

#     if len(guess) != 1 or not guess.isalpha():
#         print("Invalid input. Please enter a single letter.")
#         continue
#     if guess in guessed_letters:
#         print("You already guessed that letter.")
#         continue

#     guessed_letters.append(guess)

#     if guess in random_word:
#         print("Correct!")
#         for i in range(len(random_word)):
#             if random_word[i] == guess:
#                 word_guessed[i] = guess
#     else:
#         print("Incorrect guess.")
#         i+=1

#     if "_" not in word_guessed:
#         print(f"Congratulations, {player_name}! You guessed the word: {random_word}")
#         break

# if i == 7:
#     print(f"Sorry, {player_name}. You ran out of turns. The word was: {random_word}")
