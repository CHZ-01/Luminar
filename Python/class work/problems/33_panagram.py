#####questions##########
# Check if a given string is pangram or not.
# “The quick brown fox jumps over the lazy dog.”

sen1="The quick brown fox jumps over the lazy dog."
set1=set()

for i in sen1:
    if i.isalpha():
        set1.add(i.lower())
        
if len(set1) == 26:
    print("The given sentence is a pangram.")
else:
    print("The given sentence is not a pangram.")