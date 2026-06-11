from utils.db import get_connection


def add_report(
    report_id,
    reporter_name,
    location,
    issue_type,
    description,
    severity,
    image_path,
    status,
    date_reported
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports (
        report_id,
        reporter_name,
        location,
        issue_type,
        description,
        severity,
        image_path,
        status,
        date_reported
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        report_id,
        reporter_name,
        location,
        issue_type,
        description,
        severity,
        image_path,
        status,
        date_reported
    ))

    conn.commit()
    conn.close()


def get_all_reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM reports
    ORDER BY id DESC
    """)

    reports = cursor.fetchall()

    conn.close()

    return reports


def update_status(report_id, status):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE reports
    SET status = ?
    WHERE report_id = ?
    """, (status, report_id))

    conn.commit()
    conn.close()


def get_report_counts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM reports"
    )
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM reports WHERE status='Pending'"
    )
    pending = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM reports WHERE status='Resolved'"
    )
    resolved = cursor.fetchone()[0]

    conn.close()

    return total, pending, resolved