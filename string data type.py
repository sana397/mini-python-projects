print("\n string data type")
s = "i am anjani" #create a string
print(s)
print(s[0]) #indexing printing
print(s[1:3]) #slicing 
s2 = s.upper() #conversion of the string  to the capital letter
r = "I LIKE PYTHON"
print(r)
u = r.lower() #conversion of the string to the small letter
print(u)
print(s2)
s3 = s.replace("anjani","the world") #replacing string with another string
print(s3)
words = s.split(" ") #splitting the string
print(words)
print("\n numeric datatypes(int , float , complex)")
s = 10 #creating int datatype
e = 10.545 #creating float datatype
t = 3 + 4j #creating complex datatype
print(s , e , t)
print("\n the datatype of s is:",type(s)) #konwing the type of datatype
print("\n the datatype of e is:",type(e))
print("\n the datatype of t is:",type(t))
print(s + e , s - e, s *e,s/e)
print(s//e , s%e , s**2)
print(s==10 , e>3)
print("\n sequence datatypes(list,tuple,range)")
print("\n the list")
y = [1,2,3] #creating a list
print(y)
print(y[0]) #printing from the index
y[1] = 40 #changing element
print(y)
y.append(56) # adding element to the list
print(y)
y.insert(0,5) #inserting an element at index
print(y)
x = y.pop(3) #removing an element at index
print(y)
i = [66,7,85]
y.extend(i) #extending the list
print(y)
y.sort() #sorting the elements
print(y)
y.reverse(y) #reversing the elements
print(y)
print("\n the tuple")



