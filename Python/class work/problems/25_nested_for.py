# *****
# *****
# *****
# *****
# *****

for i in range(5):
    for j in range(5):
        print("*",end='')
    print()


print()
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# 5 5 5 5

for i in range(1,6):
    for j in range(1,6):
        print(i, end=' ')
    print()


print()
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(5):
    for j in range(1,6):
        print(j, end=' ')
    print()


print()
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()


print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()


print()
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()


print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10

var = 1
for i in range(1,5):
    for j in range(i):
        print(var, end=" ")
        var += 1
    print()


print()
# * * * * *
# * * * * 
# * * * 
# * * 
# * 

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


print()
# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

for i in range(1,6):
    for j in range(i,6):
        print(j, end=" ")
    print()


print()
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

var = 1
for i in range(1,6):
    for j in range(1,6):
        print(max(i,j), end=" ")
    print()


print()
#     *
#    * *
#   * * * 
#  * * * *
# * * * * *

s = 5 
for i in range(1,6):
    print(" "*s, end="")
    s -= 1
    for j in range(i):
        print("*", end=" ")
    print()


print()
#     *
#    * *
#   * * * 
#  * * * *
# * * * * *
#    * *
#    * *

s = 5
for i in range(1,6):
    print(" "*s, end="")
    s -= 1
    for j in range(i):
        print("*", end=" ")
    print()    
s = 3
for i in range(2):
    print(" "*s,"* *")
    

print()
#     *
#    * *
#   * * * 
#  * * * *
# * * * * *
#  * * * *
#   * * * 
#    * *
#     *

s = 5
for i in range(1,6):
    print(" "*s, end="")
    s -= 1
    for j in range(i):
        print("*", end=" ")
    print()

s = 2
for i in range(4,0,-1):
    print(" "*s, end="")
    s += 1
    for j in range(i):
        print("*", end=" ")
    print()