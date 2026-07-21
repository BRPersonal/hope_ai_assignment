import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salary.csv")
independent = data[["YearsExperience"]] #list of input columns (independent variables)
dependent = data[["Salary"]] #list of ouput columns (dependent variables)

#scatter plot to visualize data , so that we can confirm that linear algorithm would work
plt.scatter(independent,dependent) #x-axis data points, y-axis data points
plt.xlabel("YearsOfExperience",fontsize=20)
plt.ylabel("Salary",fontsize=20)
plt.show()