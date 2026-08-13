#arithmetic operators
# addition  +
# subtraction -
# multiplication *
# division /
# modulos %
# floor division // 
# exponent **

#Comparison operators this compares the value if it's True or False
# Equal to ==
# Not equal to !=
# Greater than >
# Less than <
# GTOE >=
# LTOE <=

#Logical Operator - combine 2 or more conditions. True or False
# AND operator - true only if both of the conditions are true, else false
# OR operator - true if at least one of the conditions is true, else false
# NOT operator - reverse the value

#Assignment Operator - it's as if the combination of arithmetic and = Operator
# +=
# -=
# *=
# /=
# %=
# //=
# **=

#printing
print("hello world")
input("enter a word: ") #default string input
int(input("enter a number: ")) # converted into a specific data type

#connectng 2 variables
name = "Gian"
lastname = "Arago"
answer = name + " " + lastname # using the + sign to connect 2 variables
print(answer)

pangalan = "Gian"
apelyido = f"Arago, {pangalan}" #f string
print(apelyido)

student = ["gian", "carlo"]
info = " ".join(student) # using .join to connect the value inside the box bracket
print(info)

#example ni luan getting area of the rectangle
length = float(input("enter the length: "))
width = float(input("enter the width: "))
area = length * width
print("the answer is: ", area)

#getting the length/count of the letters
word = input("Enter word: ")
print("The count of the word is: ", len(word)) #using len() to count the number of letter 

#upper and lowercase
word2 = input("Enter word: ")
print( word2.upper() )
word3 = input("enter again: ")
print( word3.lower() )

#conversion from string - other data types
number = input("enter a number: ")
converted = int(number)
print(converted)

#list variable - ORDERED, MUTABLE, ALLOW DUPLICATES CAN STORE DIFFERENT DATA TYPES
fruit = ["apple", "oranges", "banana"] #similar to array this has indexing and accessing
fruit.append("coconut") #.append is used in list variable to add value always at the end
fruit.insert(2, "cocomartin") # this add a data at sepecific place
fruit.remove("apple") #.remove is used to remove value 
fruit.pop() # remove the last item in the list
fruit.pop(-1) #,pop with indexnum inside remove the specific data in the list
del fruit[1] # delete data in the list if u use [1:2]
fruit[1] = "hatdog" # use to update the list data
fruit[1:2] = ["hehe", "huhu"] # use tot update multiple data in the list

myList = [2, 1, 4, 3, 5]
myList.sort() # use to arrange the  list from low - high
print(myList)
myList.sort(reverse=True) # reversed the list from high - low
print(myList)



#set variable - UNORDERED, MUTABLE, NO DUPLICATES, CAN CONTAIN DIFFERENT TYPES OF DATA TYPES
family = {"father", 37, "son", 18 }
family.update(["daughter"]) # updating/add to the existing set
print("father" in family) # in is used to access the set

#tuples variable - ORDERED, IMMUTABLE, ALLOW DUPLICATES
things = ("toys", "coffee")
print(things)
# tuples are more safer than list
# slightly faster than list in operation
# can be used as the dictionary list

#dictionaries variable - storing data using key-value pairs MUTABLE, NO DUPLICATES, ORDERED
student = {
    #key      value
    "name" : "gian",
    "age"  : 18,
    "gender" : "male"
    
}
print(student["name"])

student_BSU = {
    101 : {"name" : "Gian", "age" : 18, "sex" : "Male", "course" : "BSCS"}
    
    
    
}


#IF, IF-ELSE, ELSE IF STATEMENT- similar logic to c++. structure - statement > condition > block of code
grades = int(input("enter grades: "))
if grades >= 75 :
    print("galing")
    
else :
    print("nice try")

#elif - multiple conditions and conditions should from highest to lowest

score = int(input("enter score: "))
if score >= 95 :
    print("galing mo kupal")
elif score >= 90 :
    print("shet mamaw")
elif score >= 85 :
    print("galing")
elif score >= 75 :
    print("galing mo parin")

print("today", "is", "monday", sep = "...") # using sep for insirting character in between
print("shet hahahaha", end =" ") # using end to connect this line and the another line below
print("gian carlo")































