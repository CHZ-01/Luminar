# print function has 2 arguments end & sep
# \n end by default
#  (space) sep by default

greet="hello " #variable
name=input("Enter your name: ") #input function
print(greet + name) #output function

print()

list1=["hello",1,0.5,True] #list
print(list1)

tuple1=("hello",1,0.5,True) #tuple
print(tuple1) 

print("\ngreet: ",type(greet),"\nname: ",type(name),"\nlist1: ",type(list1),"\ntuple1: ",type(tuple1)) #type function

print()

# range(start,end,step)

# set are unordered & mutable datatypes that can contain heterogenous immutable data 
set1={1,1.5,(1,2,3),"hello"} #set
print(set1)
print(type(set1))

print()

# dictionaries comes in key value pair, they are ordered & have a unique key
dict1={"Name":"Vaisakh","Age":20,"Course":"Data Science"} #dictionary
print(dict1)
print(type(dict1))

print()

Null=None #null
print(type(Null))

print()

# in function to check if the data is present 
# not in function to check if the data is not present 
list1=["hello",1,0.5,True] #list
print("hello" in list1) #True
print(1 in list1) #True
print(0.5 in list1) #True
print(True in list1) #True
print("world" in list1) #False

print()

var1=6 #assignment operator
print(var1)
var1+=5 #short hand assignment operator
print(var1)

var1=(1,2)
var2=(1,2) 
print(var1 is var2) #checks the location of the variables

# and, or, not

n1="10"
n2="10"
n3=n1+n2
print(n3)

# f string or formatted string
name="Vaisakh"
age=20
course="Data Science"
greet=f"Hello {name}, you are {age} years old and studying {course}."
print(greet)

# multiplication table
num = int(input("Enter a number: "))
# using f string
for i in range(1,num+1):
    print(f"{i}X{num}={i*num}") 
print()
# normal way
for i in range(1,num+1):
    print(i,"X",num,"=",i*num)
