import google.generativeai as genai
import pdfplumber

import re
# -----------------------------
# CONFIGURE GEMINI
# -----------------------------

# Replace with your Gemini API Key


from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.5-flash")

# -----------------------------
# EXTRACT TEXT FROM PDF
# -----------------------------

def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# -----------------------------
# ANALYZE RESUME
# -----------------------------

def analyze_resume(resume_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume and respond ONLY in the following format.

ATS Score: <number>

Resume Summary:
<summary>

Technical Skills:
- skill
- skill

Strengths:
- point
- point

Weaknesses:
- point
- point

Missing Skills:
- skill
- skill

Project Suggestions:
- suggestion
- suggestion

Resume Improvements:
- suggestion
- suggestion

Recommended Job Roles:
- role
- role

Recommended Companies:
- company
- company

Resume:

{resume_text}
"""

    response = model.generate_content(prompt)

    return response.text


def extract_ats_score(text):

    match = re.search(r"ATS Score:\s*(\d+)", text)

    if match:
        return int(match.group(1))

    return 0