import streamlit as st
from database import save_dsa, get_dsa

st.set_page_config(
    page_title="DSA Tracker",
    page_icon="📚"
)

st.title("📚 DSA Progress Tracker")

topics = [
    "Arrays",
    "Strings",
    "Linked List",
    "Stack",
    "Queue",
    "Trees",
    "Graphs",
    "Heap",
    "Hashing",
    "Recursion",
    "Backtracking",
    "Dynamic Programming"
]

saved = dict(get_dsa())

completed = 0

for topic in topics:

    checked = st.checkbox(
        topic,
        value=bool(saved.get(topic, 0))
    )

    save_dsa(topic, int(checked))

    if checked:
        completed += 1

progress = completed / len(topics)

st.divider()

st.subheader("Overall Progress")

st.progress(progress)

st.metric(
    "Completed Topics",
    f"{completed}/{len(topics)}"
)

st.metric(
    "Progress",
    f"{progress*100:.1f}%"
)