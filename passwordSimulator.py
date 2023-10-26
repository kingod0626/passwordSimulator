import random




letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

print("歡迎使用密碼產生器")
upLetters = int(input("請輸入要多少個大寫字母"))
lowLetters = int(input("請輸入要多少個小寫字母"))
num = int(input("請輸入要多少個數字"))
sym = int(input("請輸入要多少個符號"))

password = ""
for i in range(0, upLetters):
    password += letters_upper[random.randint(0, 25)]
for i in range(0, lowLetters):
    password += letters_lower[random.randint(0, 25)]
for i in range(0, num):
    password += numbers[random.randint(0, 9)]
for i in range(0, sym):
    password += symbols[random.randint(0, 9)]


passwordList = list(password)
random.shuffle(passwordList)
newpassword = ""
for char in passwordList:
    newpassword += char

print(newpassword)


# a = "123456"
# b = list(a)
# random.shuffle(b)
# new_str= ""
# for char in b:
#     new_str += char
# print(b)
# print(new_str)