import numpy as np

students = (
    [170, 60],
    [165, 55],
    [180, 75],
    [172, 68],
    [160, 52],
    [175, 70],
    [168, 58],
    [182, 80]
)

np_student = np.array(students)

np_data = np_student[4]
print(np_data)

np_height = np_student[6,0]
print(np_height)

np_weigth = np_student[:,1]
print(np_weigth)

height = np_student[:,0]
print(height)

np_thirdStudent = np_student[2]
print(np_thirdStudent)

np_last = np_student[1:5, 0] # 1:5 means take all the data in row index 1 to 4, cause 5 is not included, and 0 is the index of column 1
print(np_last)
