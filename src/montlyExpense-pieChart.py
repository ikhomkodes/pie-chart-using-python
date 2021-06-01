# Program to create a pie chart 
# to visualize the Monthly Expense

# @khom

import matplotlib.pyplot as plt

items = ["Rent", "Food", "Entertainment", "Medical", "Savings"]

amount = [15000, 6500, 3500, 2000, 5000]

col_pie = ["lightcoral", "green", "red", "lightskyblue", "gold"]
exp_pie = [0,0,0.1,0,0.1]   # explode 3rd and 5th slices

plt.pie(amount, labels = items, colors = col_pie, explode = exp_pie, autopct = "%1.1f%%")
plt.title("Monthly Expenses in Rupees")
plt.show()


# Matplotlib is a library and pyplot is a module/ 
# interface to create 2D graphs and plots 
# pie function is to create pie charts 
# explode parameter is to explode the slices
# autocpt parameter controls how the percentages are displayed in the wedges.