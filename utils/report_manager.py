from utils.db import get_connection
from datetime import datetime


def add_report(
    report_id,
    reporter_name,
    location,
    issue_type,
    description,
    severity,
    image_path,
    status,
    date_reported,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
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
            date_reported,
        ),
    )

    conn.commit()
    conn.close()


def submit_report(
    reporter_name, location, issue_type, description, severity, image_path=""
):
    report_id = f"RPT-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    add_report(
        report_id=report_id,
        reporter_name=reporter_name,
        location=location,
        issue_type=issue_type,
        description=description,
        severity=severity,
        image_path=image_path,
        status="Pending",
        date_reported=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    return report_id


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


def get_reports():
    return get_all_reports()


def search_report(report_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports WHERE report_id = ?", (report_id,))

    report = cursor.fetchone()

    conn.close()
    return report


def update_status(report_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE reports
        SET status = ?
        WHERE report_id = ?
        """,
        (status, report_id),
    )

    conn.commit()
    conn.close()


def get_report_counts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reports")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status='Resolved'")
    resolved = cursor.fetchone()[0]

    conn.close()

    return total, pending, resolved
