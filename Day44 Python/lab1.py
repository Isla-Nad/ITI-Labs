
# vowels=["a", "e", "i", "o","u"]
# accum=0
# str="hello world"
# for item in str:
#     if item in vowels:
#         accum+=1
# print(accum)

# # ================================================================

# lst=[]

# for i in range(5):
#     x=input(f'Enter element {i+1}: ')
#     lst.append(x)

# lst.sort()
# print("ascending order: ",lst)
# lst.sort(reverse=True)
# print("descending order: ", lst)

# # ================================================================

# str = "iti is not close to itianother itiiti"
# accum = 0

# for i in range(len(str)):
#     if str[i:i+3] == "iti":
#         accum += 1

# print(accum)

# # ================================================================

# vowels=["a", "e", "i", "o","u"]
# while True:
#     str=""
#     input_word=input("Please enter a word: ")
#     if input_word.isalpha():
#         for item in input_word:
#             if item in vowels:
#                 item=""
#             str +=item
#     else:
#         print("Please enter a valid string")
#         continue

#     print(str)
#     break

# # ================================================================

# while True:
#     str=input("Please enter a word: ")
#     if str.isalpha():
#         for index , item in enumerate(str):
#             if item == "i":
#                 print(f'index of "i" = {index}')

#         break
#     else:
#         print("Please enter a valid string")


# # ================================================================

# while True:
#     num = input("Enter a number: ")
#     if num.isdigit():
#         num = int(num)
#         result = []
#         for i in range(1, num + 1):
#             row = []
#             for j in range(1, i + 1):
#                 product = i * j
#                 row.append(product)
#             result.append(row)

#         print(result)
#         break
#     else:
#         print("Please enter a valid number.")


# # ================================================================

# for i in range(1, 5):
#     print(" " * (5 - i) + "*" * i)