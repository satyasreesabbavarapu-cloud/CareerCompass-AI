import streamlit as st
from database import save_student, get_student

st.set_page_config(page_title="Student Profile", page_icon="👤")

st.title("👤 Student Profile")

name = st.text_input("Name")

roll_no = st.text_input("Roll Number")

branch = st.selectbox(
    "Branch",
    [
        "CSE",
        "CSE (Data Science)",
        "ECE",
        "EEE",
        "Mechanical",
        "Civil"
    ]
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.01
)

graduation_year = st.selectbox(
    "Graduation Year",
    [2026, 2027, 2028, 2029]
)

if st.button("💾 Save Profile"):
    save_student(
        name,
        roll_no,
        branch,
        cgpa,
        graduation_year
    )
    st.success("Profile saved successfully!")

st.divider()

st.subheader("Latest Saved Profile")

student = get_student()

if student:
    st.write(f"**Name:** {student[1]}")
    st.write(f"**Roll Number:** {student[2]}")
    st.write(f"**Branch:** {student[3]}")
    st.write(f"**CGPA:** {student[4]}")
    st.write(f"**Graduation Year:** {student[5]}")
else:
    st.info("No profile found.")