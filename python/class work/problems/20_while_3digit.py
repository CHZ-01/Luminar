lst = [123,235,5523,123,23123,323,12345,12779,999]
i = 0
new_lst = []
while i < len(lst):
    str1 = len(str(lst[i]))
    if str1 == 3:
        new_lst.append(lst[i])
    i += 1
print(new_lst)