import streamlit as st
from database import get_student

st.set_page_config(
    page_title="Company Eligibility",
    page_icon="💼"
)

st.title("💼 Company Eligibility")
student = get_student()

if student is None:
    st.warning("Please create your profile first.")
    st.stop()

name = student[1]
cgpa = student[4]

st.success(f"Student: {name}")
st.write(f"Current CGPA: **{cgpa}**")

companies = {
    "Infosys": 6.5,
    "TCS": 6.0,
    "Accenture": 7.0,
    "Capgemini": 6.5,
    "Cognizant": 7.0,
    "Wipro": 6.0,
    "Deloitte": 7.5,
    "IBM": 7.0,
    "Oracle": 7.5,
    "Google": 8.5,
    "Microsoft": 8.5,
    "Amazon": 8.0
}

st.divider()

for company, required_cgpa in companies.items():

    col1, col2 = st.columns([3,1])

    with col1:
        st.write(f"**{company}**")

    with col2:
        if cgpa >= required_cgpa:
            st.success("Eligible ✅")
        else:
            st.error("Not Eligible ❌")

st.divider()

eligible = []

for company, required_cgpa in companies.items():
    if cgpa >= required_cgpa:
        eligible.append(company)

st.subheader("Eligible Companies")

if eligible:
    st.write(", ".join(eligible))
else:
    st.error("No eligible companies.")