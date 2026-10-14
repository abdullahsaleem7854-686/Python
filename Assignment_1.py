# #Question 1: The Bill Splitter
totalBillAmount = float(input("Enter the total restaurant bill amount: "))
tip_percentage = float(input("Enter the tip percentage you want to leave: "))
No_of_People = int(input("Enter the number of people splitting the bill: "))
total_tip = (tip_percentage*totalBillAmount)/100
billAndTip = total_tip+totalBillAmount
per_person = billAndTip/No_of_People
print(f"total tip is: {total_tip}")
print(f"bill including Tip is: {billAndTip}")
print(f"each person has to pay: {per_person}")

#Question 2: Password Strength Checker
password = input("Enter a password: ")
if ((len(password)) >= 8) and (password.isupper() == True) and (password.islower() ==True) and (password.isdigit() == True):
    print("Password is Strong.")
elif ((len(password)) >= 6) and ((password.isdigit() == False) or (password.isupper() == False)):
    print("Password is Moderate.")
else:
    print("Password is Weak.")

#Question 3: The Guessing Game
Secret_no = 67
attemps = 0
while attemps < 5:
    guess = int(input("Guess the Number: "))
    if guess < 1 or guess > 100:
        print("The number should be greater than 1 and less than 100!")
        continue
    elif guess == Secret_no:
        print("Correct! You won!")
        break
    attemps += 1
else:
        print("Game Over! You lost.")

#Question 4: String Slicer & Manipulator
name = input("Enter full name: ")
j = 0
for i in name:
    if i == " ":
        break
    else:
        j +=1
        str1 = name[:j]
print(f"First name: {str1}")
k=1
for i in name:
    if i != " ":
        k += 1
        continue
    else:
        str2= name[k:]
total_length = len(name)
print(f"First name: {str2}")
print(f"The initials: {str1[0]}.{str2[0]}")
print(name.upper())
print(name[::-1])

#Question 5: Global vs. Local Bank
bank_balance = 5000
def deposit(amount):
    global bank_balance
    bank_balance += amount

def withdraw(amount):
    global bank_balance
    if amount > bank_balance:
        print("bank balance low.")
        return
    bank_balance -= amount

deposit(5000)
withdraw(1000)
print(f"Bank balance: {bank_balance}")

#Question 6: Unique Character Counter
long_sentence = input("Enter a long sentence: ")
total_count = len(long_sentence)
set = {*long_sentence}
unique_char = len(set)
print(f"No of unique characters: {unique_char}")
print(f"Set of unique characters: {set}")
print(f"Total count: {total_count}")

#Question 7: The Student Grading System
dict1 = {"Abdullah" : 85, "Umar" : 91 , "Ahmad" : 60 , "Babar" : 73}
for name,marks in dict1.items():
    if marks >= 90:
        print(f"{name} got A grade.")
    elif marks >= 80:
        print(f"{name} got B grade.")
    elif marks >= 70:
        print(f"{name} got C grade.")
    else:
        print(f"{name} got F grade.")

