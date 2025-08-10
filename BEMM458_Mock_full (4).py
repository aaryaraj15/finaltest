# #######################################################################################################################################################
# # 
# # Name:
# # SID:
# # Exam Date:
# # Module:
# # Github link for this assignment:  
# #
# #######################################################################################################################################################
# # Instruction 1. Read each question carefully and complete the scripts as instructed.

# # Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
# #                but not to generate code. Clearly indicate how and where you used AI.

# # Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# # Instruction 4. Commit to Git and upload to ELE once you finish.

# #######################################################################################################################################################

# # Question 1 - Loops and Lists
# # You are given a list of numbers representing weekly sales in units:
# weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# # Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# # Calculate and print the average sales.
# average_sales = sum(weekly_sales) / len(weekly_sales)
# for sales in weekly_sales:
#     if sales > average_sales:
#         print(f"Week's sales of {sales} is above average.")
#     else:
#         print(f"Week's sales of {sales} is below average.")
# print(f"Average sales: {average_sales}")

# #######################################################################################################################################################

# # Question 2 - String Manipulation
# customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# # Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# # Store each position in a list as a tuple (start, end) for both words and print the list.
# positions = [
#     (customer_feedback.find('good'), customer_feedback.find('good') + len('good')),
#     (customer_feedback.find('improved'), customer_feedback.find('improved') + len('improved'))
# ]
# print("Positions of keywords:", positions)

# #######################################################################################################################################################

# # Question 3 - Functions for Business Metrics
# # Define functions to calculate Net Profit Margin, Customer Acquisition Cost (CAC), Net Promoter Score (NPS), and Return on Investment (ROI)

# def net_profit_margin(net_profit, revenue):
#     return (net_profit / revenue) * 100

# def customer_acquisition_cost(total_marketing_cost, new_customers_acquired):
#     return total_marketing_cost / new_customers_acquired

# def net_promoter_score(promoters, detractors, total_respondents):
#     return ((promoters - detractors) / total_respondents) * 100

# def return_on_investment(net_gain, investment_cost):
#     return (net_gain / investment_cost) * 100

# # Call functions with sample values (replace with ID digits)
# print("Net Profit Margin:", net_profit_margin(5000, 20000))
# print("Customer Acquisition Cost:", customer_acquisition_cost(2000, 50))
# print("Net Promoter Score:", net_promoter_score(80, 10, 100))
# print("Return on Investment:", return_on_investment(3000, 10000))

# #######################################################################################################################################################

# # Question 4 - Data Analysis with Pandas
# import pandas as pd

# # Using a dictionary to create a DataFrame and calculate cumulative monthly sales.
# sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
# df = pd.DataFrame(sales_data)
# df['Cumulative Sales'] = df['Sales'].cumsum()
# print(df)

# #######################################################################################################################################################

# # Question 5 - Linear Regression for Forecasting
# import numpy as np
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt

# # Data for linear regression
# prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)
# demand = np.array([200, 180, 170, 160, 150, 140, 130])

# # Create and train model
# model = LinearRegression()
# model.fit(prices, demand)

# # Predict demand at price 26
# predicted_demand = model.predict(np.array([[26]]))
# print(f"Predicted demand at price £26: {predicted_demand[0]}")

# # Plotting the data points and regression line
# plt.scatter(prices, demand, color='blue')
# plt.plot(prices, model.predict(prices), color='red')
# plt.xlabel("Price (£)")
# plt.ylabel("Demand (Units)")
# plt.title("Price vs Demand")
# plt.show()

# #######################################################################################################################################################

# # Question 6 - Error Handling
# prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# # Function to calculate total price, handling non-numeric values
# def calculate_total_price(prices_dict):
#     total_price = 0
#     for item, price in prices_dict.items():
#         try:
#             total_price += float(price)
#         except ValueError:
#             print(f"Skipping non-numeric price for item {item}")
#     return total_price

# print("Total Price:", calculate_total_price(prices))

# #######################################################################################################################################################

# # Question 7 - Plotting and Visualization
# import random

# # Generate 50 random numbers and plot histogram
# random_numbers = [random.randint(1, 500) for _ in range(50)]
# plt.hist(random_numbers, bins=10, color='blue', edgecolor='black')
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Histogram of Random Numbers")
# plt.show()

# #######################################################################################################################################################

# # Question 8 - List Comprehensions
# quantities = [5, 12, 9, 15, 7, 10]

# # Double quantities of 10 or more using list comprehension
# doubled_quantities = [q * 2 for q in quantities if q >= 10]
# print("Original quantities:", quantities)
# print("Doubled quantities:", doubled_quantities)

# #######################################################################################################################################################

# # Question 9 - Dictionary Manipulation
# ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

# # Filter products with a rating of 4 or more
# filtered_ratings = {product: rating for product, rating in ratings.items() if rating >= 4}
# print("Filtered ratings:", filtered_ratings)

# #######################################################################################################################################################

# # Question 10 - Debugging and Correcting Code
# # Correct the following code to calculate the average of values
# values = [10, 20, 30, 40, 50]
# total = 0
# for i in values:
#     total += i
# average = total / len(values)
# print("The average is:", average)

# #######################################################################################################################################################
#######################################################################################################################################################
# 
# Name: Your Name Here
# SID: Your SID Here
# Exam Date: DD/MM/YYYY
# Module: Module Name Here
# Github link for this assignment:  https://github.com/your-repo-link
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.
# Instruction 2. AI usage: This code was written by me with conceptual guidance from ChatGPT for clarifications and debugging,
#                but not to generate code. Clearly indicate how and where you used AI.
# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.
# Instruction 4. Commit to Git and upload to ELE once you finish.
#######################################################################################################################################################

# Question 1 - Loops and Lists
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Calculate average sales
average_sales = sum(weekly_sales) / len(weekly_sales)

# Loop through each week's sales and compare to average
for sales in weekly_sales:
    if sales > average_sales:
        print(f"Week's sales of {sales} is above average.")
    else:
        print(f"Week's sales of {sales} is below average.")

# Print average sales
print(f"Average sales: {average_sales}")

# Output explanation:
# The loop checks each week's sales against the average and prints if it’s above or below.
#######################################################################################################################################################

# Question 2 - String Manipulation
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find positions of 'good' and 'improved'
positions = [
    (customer_feedback.find('good'), customer_feedback.find('good') + len('good')),
    (customer_feedback.find('improved'), customer_feedback.find('improved') + len('improved'))
]

print("Positions of keywords:", positions)

# Output explanation:
# Each tuple contains (start_index, end_index) for the keyword in the string.
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
def net_profit_margin(net_profit, revenue):
    """Calculates Net Profit Margin as a percentage."""
    return (net_profit / revenue) * 100

def customer_acquisition_cost(total_marketing_cost, new_customers_acquired):
    """Calculates the Customer Acquisition Cost."""
    return total_marketing_cost / new_customers_acquired

def net_promoter_score(promoters, detractors, total_respondents):
    """Calculates NPS based on promoter and detractor counts."""
    return ((promoters - detractors) / total_respondents) * 100

def return_on_investment(net_gain, investment_cost):
    """Calculates ROI as a percentage."""
    return (net_gain / investment_cost) * 100

# Sample calls
print("Net Profit Margin:", net_profit_margin(5000, 20000))
print("Customer Acquisition Cost:", customer_acquisition_cost(2000, 50))
print("Net Promoter Score:", net_promoter_score(80, 10, 100))
print("Return on Investment:", return_on_investment(3000, 10000))

# Output explanation:
# Each function returns a metric calculated from given business data.
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
import pandas as pd

# Create DataFrame
sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
df = pd.DataFrame(sales_data)

# Add cumulative sales column
df['Cumulative Sales'] = df['Sales'].cumsum()
print(df)

# Output explanation:
# Displays monthly sales with a running total in 'Cumulative Sales'.
#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Prepare data
prices = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1, 1)
demand = np.array([200, 180, 170, 160, 150, 140, 130])

# Train model
model = LinearRegression()
model.fit(prices, demand)

# Predict demand at price £26
predicted_demand = model.predict(np.array([[26]]))
print(f"Predicted demand at price £26: {predicted_demand[0]}")

# Plot
plt.scatter(prices, demand, color='blue')
plt.plot(prices, model.predict(prices), color='red')
plt.xlabel("Price (£)")
plt.ylabel("Demand (Units)")
plt.title("Price vs Demand")
plt.show()

# Output explanation:
# Regression line shows the inverse relationship between price and demand.
#######################################################################################################################################################

# Question 6 - Error Handling
prices_dict = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

def calculate_total_price(prices_dict):
    """Calculates total price, skipping non-numeric values."""
    total_price = 0
    for item, price in prices_dict.items():
        try:
            total_price += float(price)
        except ValueError:
            print(f"Skipping non-numeric price for item {item}")
    return total_price

print("Total Price:", calculate_total_price(prices_dict))

# Output explanation:
# Adds only numeric prices, skipping entries with invalid data.
#######################################################################################################################################################

# Question 7 - Plotting and Visualization
import random

# Generate random numbers
random_numbers = [random.randint(1, 500) for _ in range(50)]

# Plot histogram
plt.hist(random_numbers, bins=10, color='blue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Random Numbers")
plt.show()

# Output explanation:
# Histogram groups numbers into bins to show distribution frequency.
#######################################################################################################################################################

# Question 8 - List Comprehensions
quantities = [5, 12, 9, 15, 7, 10]

# Double quantities >= 10
doubled_quantities = [q * 2 for q in quantities if q >= 10]
print("Original quantities:", quantities)
print("Doubled quantities:", doubled_quantities)

# Output explanation:
# Creates a new list with doubled values only for quantities 10 or more.
#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

# Filter ratings >= 4
filtered_ratings = {product: rating for product, rating in ratings.items() if rating >= 4}
print("Filtered ratings:", filtered_ratings)

# Output explanation:
# Keeps only products with a rating of 4 or 5.
#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
values = [10, 20, 30, 40, 50]
total = 0

for i in values:
    total += i

average = total / len(values)
print("The average is:", average)

# Output explanation:
# Sums all values and divides by the count to find the average.
#######################################################################################################################################################
