def word_frequency(s):
    dict1 = {}
    for i in s.split():
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

def unique_words(s):
    lst = []
    for i in s.split():
        if i not in lst:
            lst.append(i)
    return lst

def longest_word(s):
    long = ""
    for i in s.split():
        if len(i) > len(long):
            long = i
    return long
