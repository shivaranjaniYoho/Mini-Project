
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Employee Data Analysis Dashboard")

st.write("This dashboard shows employee information and salary details.")

# Load employee data
df = pd.read_csv("data/employees.csv")

# Display employee data
st.subheader("Employee Details")
st.dataframe(df)

# Chart 1: Employees by Department
st.subheader("1. Employees by Department")

department_count = df["department"].value_counts()

fig1, ax1 = plt.subplots()

department_count.plot(kind="bar", ax=ax1)

ax1.set_xlabel("Department")
ax1.set_ylabel("Number of Employees")
ax1.set_title("Employees by Department")

st.pyplot(fig1)

# Chart 2: Salary Distribution
st.subheader("2. Employee Salary Distribution")

fig2, ax2 = plt.subplots()

ax2.hist(df["salary"], bins=5)

ax2.set_xlabel("Salary")
ax2.set_ylabel("Number of Employees")
ax2.set_title("Employee Salary Distribution")

st.pyplot(fig2)

# Display average salary
st.subheader("Average Salary")

average_salary = df["salary"].mean()

st.write("Average employee salary:", average_salary)

# Final message
st.success("Employee analysis completed!")
