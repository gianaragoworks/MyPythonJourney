import numpy as np

num = [1,2,3,4,5,6,7,8,9]

np_num = np.array(num) # conver the num into numpy
print(type(np_num)) # print what type of data is the np_num

np_num_m = np_num * 0.0254 #conver the value of the  np_num into meters
print(np_num_m)
