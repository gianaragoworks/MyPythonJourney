# list in pyhon is mutable, allow duplicates, ordered, and can store different data types

fruit = ["apple", "orange", "banana", "pineapple"]
fruit.append("coconut") # .append will always add the coconut to the end of the list
fruit.insert(2, "rambutan") # .insert will add the rambutan as the new fruit in index 2
fruit.remove("apple") # will remove specific fruit
fruit.pop() # will remove the last fruit of the list
fruit.pop(1) # will remove the specific fruit using index
print(fruit)

list2 = ["gian", "renzo", "anthony", "kennard", "xy"]
del list2[2] # can also use to delete data in a list using index
list2[1:2]# means start at index 1 and end it in index 2, but the end will not be incuded
print(list2)

numList = [2,3,5,6,7,1,9,8]
numList.sort() # will organze the number from low-high
print(numList)
numList.sort(reverse=True) #will arrange the num from high-low
print(numList) 
