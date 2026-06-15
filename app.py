import streamlit as st

st.set_page_config(page_title="Grade Calculator", page_icon="📚")

st.title("📚 Student Grade Calculator")

st.write("Enter marks for 5 subjects:")

subject1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
subject2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
subject3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)
subject4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100)
subject5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100)

if st.button("Calculate Grade"):
    total = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.success(f"Total Marks: {total}/500")
    st.info(f"Percentage: {percentage:.2f}%")
    st.warning(f"Grade: {grade}")
