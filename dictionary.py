#dictionary storing data using key-value pairs, Ordered, Mutable, No duplicates

student_BSU = {
    101 : {"name" : "gian", "year" : "first year", "course" : "BSCS"},
    102 : {"name" : "renzo", "year" : "first year", "course" : "BSCS"},
    103 : {"name" : "anthony", "year" : "first year", "course" : "BSCS"}
}
student_BSU[104] = {"name" : "renzo", "year" : "first year", "course" : "BSCS"} # this is how to add in dictionaris
del studen_BSU[102] # use to delete key in dictiona ry
print(104 in student_BSU) # this will check if the key value pairs of 104 is in dictionary
print(student_BSU.keys()) # this will print all the keys in the dictionary
print(student_BSU[101]) # this will print the value of the specific key in the dictionary
