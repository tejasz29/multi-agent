import sqlite3, json

DB = "exam_planner.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS study_plan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day INTEGER,
            subject TEXT,
            topics TEXT,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_plan(plan: list[dict]):
    """plan = [{'day': 1, 'subject': 'ML', 'topics': 'Intro, Regression'}, ...]"""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM study_plan")   # reset old plan
    for entry in plan:
        c.execute(
            "INSERT INTO study_plan (day, subject, topics) VALUES (?,?,?)",
            (entry["day"], entry["subject"], entry["topics"])
        )
    conn.commit()
    conn.close()

def get_plan():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    rows = c.execute("SELECT id, day, subject, topics, completed FROM study_plan ORDER BY day").fetchall()
    conn.close()
    return [{"id": r[0], "day": r[1], "subject": r[2], "topics": r[3], "completed": r[4]} for r in rows]

def mark_completed(entry_id: int, done: bool):
    conn = sqlite3.connect(DB)
    conn.execute("UPDATE study_plan SET completed=? WHERE id=?", (int(done), entry_id))
    conn.commit()
    conn.close()