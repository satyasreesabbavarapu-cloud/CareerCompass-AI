import sqlite3

# Connect to database
conn = sqlite3.connect("database/placement.db", check_same_thread=False)
cursor = conn.cursor()

# ==========================
# Create Student Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    branch TEXT,
    cgpa REAL,
    graduation_year INTEGER
)
""")

# ==========================
# Create Interview Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS interviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    interview_date TEXT,
    round TEXT,
    result TEXT,
    notes TEXT
)
""")

# ==========================
# Create DSA Progress Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS dsa_progress(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    status INTEGER
)
""")

# ==========================
# Create Aptitude Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS aptitude(
    topic TEXT PRIMARY KEY,
    status INTEGER
)
""")

conn.commit()

# ===================================
# Student Functions
# ===================================

def save_student(name, roll_no, branch, cgpa, graduation_year):
    cursor.execute("""
    INSERT INTO student(name, roll_no, branch, cgpa, graduation_year)
    VALUES (?, ?, ?, ?, ?)
    """, (name, roll_no, branch, cgpa, graduation_year))
    conn.commit()


def get_student():
    cursor.execute("SELECT * FROM student ORDER BY id DESC LIMIT 1")
    return cursor.fetchone()


# ===================================
# Interview Functions
# ===================================

def save_interview(company, interview_date, round_name, result, notes):
    cursor.execute("""
    INSERT INTO interviews(
        company,
        interview_date,
        round,
        result,
        notes
    )
    VALUES (?, ?, ?, ?, ?)
    """, (company, interview_date, round_name, result, notes))

    conn.commit()


def get_interviews():
    cursor.execute("""
    SELECT company,
           interview_date,
           round,
           result,
           notes
    FROM interviews
    ORDER BY interview_date
    """)

    return cursor.fetchall()


# ===================================
# DSA Functions
# ===================================

def save_dsa(topic, status):
    cursor.execute("""
    SELECT * FROM dsa_progress
    WHERE topic = ?
    """, (topic,))

    data = cursor.fetchone()

    if data:
        cursor.execute("""
        UPDATE dsa_progress
        SET status = ?
        WHERE topic = ?
        """, (status, topic))
    else:
        cursor.execute("""
        INSERT INTO dsa_progress(topic, status)
        VALUES (?, ?)
        """, (topic, status))

    conn.commit()


def get_dsa():
    cursor.execute("""
    SELECT topic, status
    FROM dsa_progress
    """)
    return cursor.fetchall()


# ===================================
# Aptitude Functions
# ===================================

def save_aptitude(topic, status):

    cursor.execute("""
    SELECT * FROM aptitude
    WHERE topic = ?
    """, (topic,))

    data = cursor.fetchone()

    if data:
        cursor.execute("""
        UPDATE aptitude
        SET status = ?
        WHERE topic = ?
        """, (status, topic))
    else:
        cursor.execute("""
        INSERT INTO aptitude(topic, status)
        VALUES (?, ?)
        """, (topic, status))

    conn.commit()


def get_aptitude():

    cursor.execute("""
    SELECT topic, status
    FROM aptitude
    """)

    return cursor.fetchall()