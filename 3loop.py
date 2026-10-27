'''Print 1 to 100'''
# for i in range(1, 100):
#     print(i)

'''Print even numbers'''
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

'''Sum of N numbers'''
# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print("Total Sum:", total)

'''Multiplication table'''
# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

'''Reverse string'''
# text = input("Enter a word: ")
# reverse_text = text[::-1]
# print("Reversed String:", reverse_text)

'''Count vowels'''
# text = input("Enter a word: ")
# count = 0
# for char in text.lower():
#     if char in "aeiou":
#         count = count + 1
# print("Total Vowels:", count)

'''Prime number'''
# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Not a Prime Number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")

'''Fibonacci series'''
# n = int(input("How many terms? "))
# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b

'''Pattern printing'''
# for i in range(1, 6):
#     print("*" * i)