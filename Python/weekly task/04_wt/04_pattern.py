# hw04
#       1 
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

s = 6
for i in range(1,5):
    print(" "*s, end="")
    s -= 2
    for j in range(1,i+1):
        print(j, end=" ")
    else:
        for k in range(i-1,0,-1):
            print(k, end=" ")    
    print()