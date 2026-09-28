import matplotlib as plt
#HISTOGRAM

year = [2000, 2010, 2020, 2030, 2040]

#SYNTAX FOR HISTOGRAM

plt.hist(year, bins=3) # the graph of this is like ----+-----+-----+ there are 3 bins/space for datas
plt.show()
