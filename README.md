# 🎓 CareerCompass AI

## Intelligent Placement Preparation System

CareerCompass AI is an AI-powered placement preparation platform built using Python, Streamlit, SQLite, Plotly, and Google Gemini API. It helps students track placement preparation, analyze resumes using AI, monitor DSA and aptitude progress, and manage interview readiness.

## ✨ Features

- 👤 Student Profile Management
- 🏢 Company Eligibility Checker
- 💻 DSA Progress Tracker
- 🧠 Aptitude Tracker
- 📅 Interview Tracker
- 📄 Resume Manager
- 🤖 AI Resume Analyzer (Google Gemini)
- 📊 Analytics Dashboard
- 🗄️ SQLite Database Integration

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- Plotly
- Google Gemini API
- pdfplumber
- python-dotenv

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/satyasreesabbavarapu-cloud/CareerCompass-AI.git
```

Go to the project directory:

```bash
cd CareerCompass-AI
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📂 Project Structure

```text
CareerCompass-AI/
│
├── app.py                      # Main Streamlit application
├── database.py                 # Database functions
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignored files
├── .env                        # Environment variables (not uploaded to GitHub)
│
├── assets/                     # Images and screenshots
│
├── database/
│   └── placement.db            # SQLite database
│
├── pages/
│   ├── 1_Profile.py
│   ├── 2_Company_Eligibility.py
│   ├── 3_DSA_Tracker.py
│   ├── 4_Aptitude.py
│   ├── 5_Interview_Tracker.py
│   ├── 6_Resume_Manager.py
│   ├── 7_Analytics.py
│   └── 8_AI_Resume_Analyzer.py
│
├── resumes/                    # Uploaded resumes
│
└── utils/
    └── gemini_helper.py        # Gemini AI helper functions
```

## 📸 Screenshots

### 🏠 Dashboard
<img width="959" height="536" alt="Screenshot 2026-07-11 111719" src="https://github.com/user-attachments/assets/33f1d0d2-c036-48a5-b22f-70ba3b8e0801" />

### 💻 DSA Tracker
<img width="959" height="544" alt="Screenshot 2026-07-11 111730" src="https://github.com/user-attachments/assets/8730204d-b7ec-48bb-9a96-0a7cc01ca8c4" />


### 🧠 Aptitude Tracker
<img width="959" height="532" alt="Screenshot 2026-07-11 111744" src="https://github.com/user-attachments/assets/8f64f5a4-ee63-43a1-a9f5-4b8eaae6cc62" />


### 📊 Analytics Dashboard
<img width="959" height="542" alt="Screenshot 2026-07-11 111808" src="https://github.com/user-attachments/assets/d4bf58b0-9b96-474c-93ad-93f63d7f3ca2" />


### 🤖 AI Resume Analyzer
<img width="959" height="539" alt="Screenshot 2026-07-11 111645" src="https://github.com/user-attachments/assets/646c4aa7-044f-4be6-bd41-5dfe81e513c4" />


### 📋 AI Resume Analysis Result ⭐
<img width="960" height="600" alt="image" src="https://github.com/user-attachments/assets/2c87f77e-5500-4564-ab82-f212813aa0b3" />

## 🚀 Future Enhancements

- User Authentication
- Email Notifications
- AI Mock Interview Module
- Placement Prediction
- Resume ATS Comparison
