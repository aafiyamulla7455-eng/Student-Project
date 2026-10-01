import streamlit as st
import sqlite3
import pandas as pd

st.title("Student Performance Analysis")

# Database connection
conn = sqlite3.connect("student.db")

# Read data
student = pd.read_sql("SELECT * FROM students", conn)

# Show data
st.subheader("Student Data")
st.dataframe(student)

# Average Marks
st.subheader("Average Marks")
average = student["Marks"].mean()
st.write(round(average, 2))

# Gender Wise Average Marks
st.subheader("Gender Wise Average Marks")

gender_marks = student.groupby("Gender")["Marks"].mean()

st.bar_chart(gender_marks)

# Course Wise Average Marks
st.subheader("Course Wise Average Marks")

course_marks = student.groupby("Course")["Marks"].mean()

st.bar_chart(course_marks)

# City Wise Average Marks
st.subheader("City Wise Average Marks")

city_marks = student.groupby("City")["Marks"].mean()

st.bar_chart(city_marks)

# Grade Wise Students
st.subheader("Grade Wise Students")

student["Grade"] = pd.cut(
    student["Marks"],
    bins=[0, 40, 60, 75, 90, 100],
    labels=["F", "C", "B", "A", "A+"]
)

grade_count = student["Grade"].value_counts()

st.bar_chart(grade_count)