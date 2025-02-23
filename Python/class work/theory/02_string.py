
str1="Hello world"
# slicing
print(str1[0:5]) #Hello
print(str1[:5]) #Hello
print(str1[5:]) #world
print(str1[-5:]) #world
print(str1[::2]) #Hlo wrd

print(len(str1)) #11

str1="Hello"
# string methods
print(str1.upper()) #HELLO
print(str1.lower()) #hello
print(str1.capitalize()) #Hello
print(str1.swapcase()) #hELLO

str1="Hello world!"
print(str1.split()) #['Hello', 'world!']
print(str1.split("o")) #['Hell', ' w', 'rld!']

list1=[1,2,3]
print(len(str1)) #length

list1=["Hello", "python", "world"]
str1=" ".join(list1) #convert to string
print(list1)
print(str1)

str1="  Hello world!  "
str2=str1.strip() #remove spaces from start and end
print(str1)
print(str2)
str1="###Hello world!###"
str2=str1.strip("#") #remove # from start and end
print(str1)
print(str2)

str1="Hello world!"
str2=str1.replace("world","python")  #replace first word with second
print(str2)

str1="Hello world"
str2=str1.upper() 
var1="123"
var2="123abc"
print(str1.islower())
print(str2.isupper())
print(str1.isalpha())
print(var1.isnumeric())
print(var2.isalnum())
print(var1.startswith("12"))
print(var1.endswith("bc"))