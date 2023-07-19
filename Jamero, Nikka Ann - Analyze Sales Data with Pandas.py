#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df1 = pd.read_csv("/Users/najjamero/Desktop/fct_invoice.csv")

df1


# In[4]:


df2 = pd.read_json("/Users/najjamero/Desktop/dim_customer.json")

df2


# In[8]:


# Easy 1. How many unique customers are in the dataset?

unique_customers = df2["id"].nunique()

print("There are " + unique_customers + " customers in the dataset.")


# In[11]:


# Easy 2. What are the different categories of products available? How many unique categories are there?

categories = df1["category"].unique()
num_categories = df1["category"].nunique()

print("There are " + str(categories) + ", making it a total of " + str(num_categories) + " categories in the dataset.")


# In[26]:


# Easy 3. Which payment method is the most popular? How many times was it used?

num_popular_pm = df1["payment_method"].value_counts()
popular_pm = payment_counts.idxmax()
count_num_popular_pm = num_popular_pm.loc[popular_pm]

print("Most popular payment method:", most_popular_payment)
print("Number of times used:", count_num_popular_pm)


# In[48]:


# Medium 1. What are the three most popular categories, by total sales?

num_popular_pm = df1["payment_method"].value_counts()
popular_pm = num_popular_pm.idxmax()
top_three_pm = num_popular_pm.head(3)

print("Top Three Payment Methods:")
print(top_three_pm.to_string())


# In[50]:


# Medium 2. What are the total sales attributed to customers over the age of 45?

merged = pd.merge(df1,df2,left_on = "customer_id", right_on = "id")
merged["sales"] = merged["quantity"] * merged["price"]
print("The total sales attributed to customers over the age of 45 is " + str(merged[merged["age"] > 45]["sales"].sum()))


# In[83]:


# Medium 3. How is the data distributed across different invoice dates? Are there any seasonal trends or patterns? (Use a graph for this.)

import matplotlib.pyplot as plt

merged["invoice_date"] = pd.to_datetime(merged["invoice_date"], format = "%d/%m/%Y")
merged["year"] = merged["invoice_date"].dt.year
merged["month"] = merged["invoice_date"].dt.month
monthly_sales = merged.groupby(["year", "month"])['sales'].sum()

monthly_sales.plot(kind='line')
plt.title('Data Distribution by Invoice Date')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()


# In[86]:


# Hard 1. Create a pivot table showing the breakdown of sales across these dimensions, in this order: category, decade age range (e.g., 10-19, 20-29, and so forth).

merged["range"] = pd.cut(merged["age"], bins = range(10, 91, 10), right = False)
table = pd.pivot_table(merged, index = "range", columns = "category", values = "sales", aggfunc = "sum")
print(table)

