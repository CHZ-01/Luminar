# hw04 Armstrong number or not
num = int(input("Enter a number: "))
str_num = str(num)
str_len = len(str_num)
str_sum = 0

for i in str_num:
    str_sum += int(i)**str_len

if num == str_sum:
    print(f"{num} is Armstrong")
else:
    print(f"{num} is not Armstrong")