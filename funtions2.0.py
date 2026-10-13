# def even_odd(num):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")

# num = int(input("Enter a number"))
# even_odd(num)

# def check_string(str):
#     if "A" or "a" or "E" or "e" or "I" or "i" or "O" or "o" or "U" or "u" in str:
#         print("There is a vowel")
#     else:
#         print("There is no vowel")

# string = str(input("Enter a string"))
# check_string(string)
def Avg(marks):
    sum = 0
    for i in marks:
        sum += i

    if len(marks) > 0:
       avg =  sum / len(marks)
    else:
        print("list is empty")
    return avg

marks = [90,50,20,80]
print(Avg(marks))