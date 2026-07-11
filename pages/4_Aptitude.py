import streamlit as st
from database import save_aptitude, get_aptitude

st.set_page_config(
    page_title="Aptitude Tracker",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Aptitude Tracker")

st.write("Track your aptitude preparation topic by topic.")

# ---------------- QUANTITATIVE ----------------

quantitative = [
    "Number System",
    "Percentage",
    "Profit & Loss",
    "Simple Interest",
    "Compound Interest",
    "Ratio & Proportion",
    "Average",
    "Time & Work",
    "Time, Speed & Distance",
    "Probability",
    "Permutation & Combination",
    "Data Interpretation"
]

# ---------------- LOGICAL ----------------

logical = [
    "Blood Relations",
    "Direction Sense",
    "Coding-Decoding",
    "Number Series",
    "Alphabet Series",
    "Syllogism",
    "Seating Arrangement",
    "Puzzles",
    "Clock",
    "Calendar"
]

# ---------------- VERBAL ----------------

verbal = [
    "Reading Comprehension",
    "Sentence Correction",
    "Error Detection",
    "Fill in the Blanks",
    "Synonyms",
    "Antonyms",
    "Vocabulary",
    "Grammar",
    "Para Jumbles",
    "Cloze Test"
]

# ---------------- PROGRAMMING ----------------

programming = [
    "Flowcharts",
    "Pseudocode",
    "Arrays",
    "Strings",
    "Loops",
    "Functions",
    "Recursion",
    "Output Prediction",
    "Debugging"
]

# ---------------- LOAD DATABASE ----------------

saved = dict(get_aptitude())

completed = 0
total = 0

# ---------------- FUNCTION ----------------

def show_section(title, topics):

    global completed
    global total

    with st.expander(title, expanded=False):

        for topic in topics:

            value = st.checkbox(
                topic,
                value=bool(saved.get(topic, 0)),
                key=topic
            )

            total += 1

            if value:
                completed += 1

            save_aptitude(topic, int(value))

# ---------------- DISPLAY ----------------

show_section("🧮 Quantitative Aptitude", quantitative)

show_section("🧩 Logical Reasoning", logical)

show_section("📖 Verbal Ability", verbal)

show_section("💻 Programming Aptitude", programming)

# ---------------- SUMMARY ----------------

st.divider()

percentage = (completed / total) * 100 if total else 0

st.subheader("📊 Overall Progress")

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Completed",
        f"{completed}/{total}"
    )

with c2:
    st.metric(
        "Progress",
        f"{percentage:.1f}%"
    )

st.progress(percentage / 100)