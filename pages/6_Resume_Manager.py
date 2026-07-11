import streamlit as st
import os

st.set_page_config(
    page_title="Resume Manager",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Manager")

st.write("Upload and manage your latest resume.")

UPLOAD_FOLDER = "resumes"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    filepath = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

st.divider()

st.subheader("Uploaded Resumes")

files = os.listdir(UPLOAD_FOLDER)

if files:

    for file in files:

        col1, col2 = st.columns([8,2])

        with col1:
            st.write(f"📄 {file}")

        with col2:
            with open(os.path.join(UPLOAD_FOLDER,file),"rb") as f:
                st.download_button(
                    "Download",
                    data=f,
                    file_name=file
                )

else:
    st.info("No resumes uploaded.")