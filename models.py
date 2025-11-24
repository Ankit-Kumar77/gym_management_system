from datetime import datetime, timedelta
from database import connect_db


# --------- Members ---------

def add_member(name, age, gender, phone, email, join_date, plan, expiry_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO members 
           (name, age, gender, phone, email, join_date, plan, expiry_date)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (name, age, gender, phone, email, join_date, plan, expiry_date),
    )
    conn.commit()
    conn.close()


def update_member(member_id, name, age, gender, phone, email, join_date, plan, expiry_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """UPDATE members
           SET name=?, age=?, gender=?, phone=?, email=?, join_date=?, plan=?, expiry_date=?
           WHERE id=?""",
        (name, age, gender, phone, email, join_date, plan, expiry_date, member_id),
    )
    conn.commit()
    conn.close()


def delete_member(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM members WHERE id=?", (member_id,))
    conn.commit()
    conn.close()


def get_all_members():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, gender, phone, email, join_date, plan, expiry_date FROM members")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_members(keyword):
    conn = connect_db()
    cur = conn.cursor()
    like = f"%{keyword}%"
    cur.execute(
        """SELECT id, name, age, gender, phone, email, join_date, plan, expiry_date
           FROM members
           WHERE name LIKE ? OR phone LIKE ? OR plan LIKE ?""",
        (like, like, like),
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def get_member_by_id(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, age, gender, phone, email, join_date, plan, expiry_date FROM members WHERE id=?",
        (member_id,),
    )
    row = cur.fetchone()
    conn.close()
    return row


# --------- Trainers ---------

def add_trainer(name, specialty, phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO trainers (name, specialty, phone) VALUES (?, ?, ?)",
        (name, specialty, phone),
    )
    conn.commit()
    conn.close()


def update_trainer(trainer_id, name, specialty, phone):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE trainers SET name=?, specialty=?, phone=? WHERE id=?",
        (name, specialty, phone, trainer_id),
    )
    conn.commit()
    conn.close()


def delete_trainer(trainer_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM trainers WHERE id=?", (trainer_id,))
    conn.commit()
    conn.close()


def get_all_trainers():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, specialty, phone FROM trainers")
    rows = cur.fetchall()
    conn.close()
    return rows


# --------- Membership plans ---------

def get_all_membership_plans():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, duration_months, price FROM memberships")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_membership_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, duration_months, price FROM memberships WHERE name=?",
        (name,),
    )
    row = cur.fetchone()
    conn.close()
    return row


# --------- Attendance ---------

def mark_attendance(member_id, date_str, time_str):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO attendance (member_id, date, time) VALUES (?, ?, ?)",
        (member_id, date_str, time_str),
    )
    conn.commit()
    conn.close()


def get_attendance_for_member(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT date, time FROM attendance WHERE member_id=? ORDER BY date DESC, time DESC",
        (member_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows


# --------- Payments ---------

def add_payment(member_id, amount, date_str, method, notes):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO payments (member_id, amount, date, method, notes) VALUES (?, ?, ?, ?, ?)",
        (member_id, amount, date_str, method, notes),
    )
    conn.commit()
    conn.close()


def get_payments_for_member(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, amount, date, method, notes FROM payments WHERE member_id=? ORDER BY date DESC",
        (member_id,),
    )
    rows = cur.fetchall()
    conn.close()
    return rows
