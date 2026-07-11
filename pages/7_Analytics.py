import streamlit as st
import plotly.express as px

from database import (
    get_student,
    get_dsa,
    get_aptitude,
    get_interviews
)

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Dashboard")

student = get_student()
dsa = get_dsa()
aptitude = get_aptitude()
interviews = get_interviews()

# ---------------- Student ----------------

if student:
    cgpa = student[4]
else:
    cgpa = 0

# ---------------- DSA ----------------

total_topics = 12
completed = sum(status for _, status in dsa)

dsa_percentage = (
    completed/total_topics*100
    if total_topics else 0
)

# ---------------- Aptitude ----------------

if aptitude:
    aptitude_percentage = sum(score for _,score in aptitude)/len(aptitude)
else:
    aptitude_percentage = 0

# ---------------- KPI ----------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("CGPA",f"{cgpa:.2f}")

with c2:
    st.metric("DSA",f"{dsa_percentage:.0f}%")

with c3:
    st.metric("Aptitude",f"{aptitude_percentage:.0f}%")

with c4:
    st.metric("Interviews",len(interviews))

st.divider()

# ---------------- Bar Chart ----------------

bar = px.bar(
    x=[
        "CGPA",
        "DSA",
        "Aptitude"
    ],
    y=[
        cgpa*10,
        dsa_percentage,
        aptitude_percentage
    ],
    text=[
        round(cgpa*10,1),
        round(dsa_percentage,1),
        round(aptitude_percentage,1)
    ],
    title="Performance Overview"
)

st.plotly_chart(bar,use_container_width=True)

# ---------------- Pie Chart ----------------

pie = px.pie(
    names=[
        "Completed",
        "Remaining"
    ],
    values=[
        completed,
        total_topics-completed
    ],
    title="DSA Completion"
)

st.plotly_chart(pie,use_container_width=True)

# ---------------- Interview Status ----------------

if interviews:

    status_count = {}

    for interview in interviews:

        status = interview[3]

        status_count[status] = status_count.get(status,0)+1

    interview_chart = px.pie(
        names=list(status_count.keys()),
        values=list(status_count.values()),
        title="Interview Status"
    )

    st.plotly_chart(interview_chart,use_container_width=True)

else:

    st.info("No interview data available.")