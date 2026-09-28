import matplotlib.pyplot as plt

year = [2000, 2010, 2020, 2030, 2040]
pop = [1.2, 2.3, 3.4, 4.5, 5.6]

print(year[-1])
print(pop[-1])

plt.plot(year, pop) # the first argument is horizontal and second is vertical
plt.show() # printing the plot

# Change the line plot below to a scatter plot
plt.scatter(year, pop) #scatter is just similar to plot but the data is scattered 
# Put the x-axis on a logarithmic scale
plt.xscale('log') 
# Show plot
plt.show()
