import frappe
from frappe import _

def get_data():
    data = frappe.db.sql("""
        SELECT
            status,
            COUNT(*) as count
        FROM
            `tabProject`
        GROUP BY
            status
        ORDER BY
            status
    """, as_dict=True)

    if not data:
        return {
            "labels": [_("No Projects Found")],
            "datasets": [{"name": _("Status"), "values": [0]}],
        }

    labels = [row['status'] if row['status'] else _("Uncategorized") for row in data]
    values = [row['count'] for row in data]

    return {
        "labels": labels,
        "datasets": [{"name": _("Projects"), "values": values}],
    }
