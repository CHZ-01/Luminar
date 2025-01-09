lst=[1,24,5,6,783,5]
temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp
print(lst)

var1 = lst.copy() #creates a copy of the list
lst.append(12) #adds to the last
lst.insert(3,"hello") #adds to the given index
lst.remove(5) #removes first occurrence of the given data
lst.pop(5) #removes the data according to the given index
lst.pop() #removes the last index when left blank
lst.clear() #clears the full list data 

print(var1) 
print(lst)


lst=[]
for i in range(1,1001):
    if i % 4 == 0 and i % 9 == 0:
        lst.append(i)
print(lst)        