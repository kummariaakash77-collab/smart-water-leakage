from utils.report_manager import (
    get_all_reports,
    get_report_counts,
)


def get_water_reports():
    """
    Returns report statistics and report data.
    """

    reports = get_all_reports()

    total, pending, resolved = get_report_counts()

    return {
        "total_reports": total,
        "pending_reports": pending,
        "resolved_reports": resolved,
        "reports": reports
    }


def get_pending_reports():
    """
    Returns pending report count.
    """

    total, pending, resolved = get_report_counts()

    return {
        "pending_reports": pending
    }


def get_resolved_reports():
    """
    Returns resolved report count.
    """

    total, pending, resolved = get_report_counts()

    return {
        "resolved_reports": resolved
    }


def get_summary():
    """
    Returns overall report summary.
    """

    total, pending, resolved = get_report_counts()

    return f"""
Total Reports: {total}
Pending Reports: {pending}
Resolved Reports: {resolved}
"""