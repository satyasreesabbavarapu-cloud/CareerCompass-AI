import streamlit as st
import plotly.express as px

from database import (
    get_student,
    get_dsa,
    get_aptitude,
    get_interviews
)

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="CareerCompass AI",
    page_icon="🎓",
    layout="wide"
)

# -------------------- LOAD DATA --------------------

student = get_student()

dsa_data = get_dsa()
aptitude_data = get_aptitude()
interviews = get_interviews()

# -------------------- STUDENT DETAILS --------------------

if student:
    name = student[1]
    roll_no = student[2]
    branch = student[3]
    cgpa = student[4]
    graduation_year = student[5]
else:
    name = "Student"
    roll_no = "-"
    branch = "-"
    cgpa = 0
    graduation_year = "-"

# -------------------- CALCULATIONS --------------------

eligible_companies = 0

if cgpa >= 9.0:
    eligible_companies = 25
elif cgpa >= 8.5:
    eligible_companies = 20
elif cgpa >= 8.0:
    eligible_companies = 15
elif cgpa >= 7.5:
    eligible_companies = 10
else:
    eligible_companies = 5

# -------------------- DSA --------------------

total_topics = 12

completed_topics = sum(status for _, status in dsa_data)

dsa_percentage = (
    completed_topics / total_topics * 100
    if total_topics
    else 0
)

# -------------------- APTITUDE --------------------

if aptitude_data:
    aptitude_percentage = sum(score for _, score in aptitude_data) / len(aptitude_data)
else:
    aptitude_percentage = 0

# -------------------- OVERALL SCORE --------------------

overall = int(
    (cgpa / 10) * 40
    + dsa_percentage * 0.30
    + aptitude_percentage * 0.30
)

# -------------------- HEADER --------------------

st.title("🎓 CareerCompass AI")

st.caption("Intelligent Placement Preparation System")

st.markdown("---")

st.markdown(f"""
# 👋 Welcome, {name}

Track your placement progress,
prepare for interviews,
and achieve your dream job.
""")

# -------------------- KPI CARDS --------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎓 CGPA", f"{cgpa:.2f}")

with col2:
    st.metric("📚 DSA", f"{dsa_percentage:.0f}%")

with col3:
    st.metric("🧠 Aptitude", f"{aptitude_percentage:.0f}%")

with col4:
    st.metric("💼 Companies", eligible_companies)

# -------------------- READINESS --------------------

st.markdown("## 🚀 Placement Readiness")

st.progress(overall / 100)

st.write(f"Overall Readiness : **{overall}%**")

st.divider()

# -------------------- CHART --------------------

chart_data = {
    "Category": [
        "CGPA",
        "DSA",
        "Aptitude",
        "Placement"
    ],
    "Score": [
        cgpa * 10,
        dsa_percentage,
        aptitude_percentage,
        overall
    ]
}

fig = px.bar(
    chart_data,
    x="Category",
    y="Score",
    text="Score",
    color="Category",
    title="Overall Performance"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------- STUDENT INFO --------------------

st.divider()

st.subheader("👤 Student Information")

left, right = st.columns(2)

with left:
    st.write(f"**Name:** {name}")
    st.write(f"**Roll Number:** {roll_no}")

with right:
    st.write(f"**Branch:** {branch}")
    st.write(f"**Graduation Year:** {graduation_year}")

# -------------------- INTERVIEW SUMMARY --------------------

st.divider()

st.subheader("📅 Interview Summary")

if interviews:

    st.success(f"Total Interviews Scheduled : {len(interviews)}")

    for interview in interviews[-5:]:

        st.info(
            f"{interview[0]} | {interview[1]} | {interview[2]} | {interview[3]}"
        )

else:

    st.warning("No interviews scheduled.")

# -------------------- QUICK ACTIONS --------------------

st.divider()

st.subheader("⚡ Quick Actions")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.page_link("pages/1_Profile.py", label="👤 Profile")

with c2:
    st.page_link("pages/2_Company_Eligibility.py", label="💼 Companies")

with c3:
    st.page_link("pages/3_DSA_Tracker.py", label="📚 DSA Tracker")

with c4:
    st.page_link("pages/5_Interview_Tracker.py", label="📅 Interviews")

# -------------------- FOOTER --------------------

st.markdown("---")

st.caption("© 2026 CareerCompass AI | Built with Python, Streamlit & SQLite")