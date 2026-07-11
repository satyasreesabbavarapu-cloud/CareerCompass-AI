import streamlit as st
from database import save_interview, get_interviews
import pandas as pd

st.set_page_config(
    page_title="Interview Tracker",
    page_icon="📅"
)

st.title("📅 Interview Tracker")

company = st.text_input("Company")

interview_date = st.date_input("Interview Date")

round_name = st.selectbox(
    "Round",
    [
        "Online Assessment",
        "Technical",
        "Managerial",
        "HR"
    ]
)

result = st.selectbox(
    "Status",
    [
        "Scheduled",
        "Selected",
        "Rejected",
        "Pending"
    ]
)

notes = st.text_area("Notes")

if st.button("Save Interview"):

    save_interview(
        company,
        str(interview_date),
        round_name,
        result,
        notes
    )

    st.success("Interview Saved Successfully!")

st.divider()

st.subheader("Interview History")

data = get_interviews()

if data:

    df = pd.DataFrame(
        data,
        columns=[
            "Company",
            "Date",
            "Round",
            "Status",
            "Notes"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No Interviews Added Yet.")