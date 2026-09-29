#dictionary storing data using key-value pairs, Ordered, Mutable, No duplicates

student_BSU = {
    101 : {"name" : "gian", "year" : "first year", "course" : "BSCS"},
    102 : {"name" : "renzo", "year" : "first year", "course" : "BSCS"},
    103 : {"name" : "anthony", "year" : "first year", "course" : "BSCS"}
}
print(student_BSU.keys()) # this will print all the keys in the dictionary
print(student_BSU[101]) # this will print the value of the specific key in the dictionary
