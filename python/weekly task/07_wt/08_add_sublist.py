# hw08
lst = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
lst[2][1][2].extend(sub_list)
print(lst)