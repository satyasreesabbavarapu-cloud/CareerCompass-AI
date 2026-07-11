import streamlit as st
import os
from utils.gemini_helper import (
    extract_text_from_pdf,
    analyze_resume,
    extract_ats_score
)

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.markdown("""
Upload your resume and let **Gemini AI** analyze it.

The AI will provide:

- 📄 Resume Summary
- 🎯 ATS Score
- 💪 Strengths
- ⚠️ Weaknesses
- 📚 Missing Skills
- 💡 Improvement Suggestions
- 💼 Recommended Job Roles
- 🏢 Recommended Companies
""")

st.divider()

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing resume using Gemini AI..."):

            resume_text = extract_text_from_pdf(file_path)

            result = analyze_resume(resume_text)

        st.success("Analysis Complete!")

        st.divider()

        ats = extract_ats_score(result)

        col1, col2, col3 = st.columns(3)

        with col2:
            st.metric(
                label="🎯 ATS Score",
                value=f"{ats}/100"
            )

        st.divider()

        st.markdown(result)

else:

    st.info("Please upload a PDF resume.")