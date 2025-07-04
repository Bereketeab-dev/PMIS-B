import frappe
from frappe import _

def get_data():
    data = frappe.db.sql("""
        SELECT
            status,
            COUNT(*) as count
        FROM
            `tabProject Schedule Task`
        GROUP BY
            status
        ORDER BY
            status
    """, as_dict=True)

    if not data:
        return {
            "labels": [_("No Tasks Found")],
            "datasets": [{"name": _("Status"), "values": [0]}],
        }

    labels = [row['status'] if row['status'] else _("Uncategorized") for row in data]
    values = [row['count'] for row in data]

    # For Bar chart, structure might be slightly different if multiple datasets,
    # but for a single dataset, this is fine.
    return {
        "labels": labels,
        "datasets": [{"name": _("Tasks"), "values": values}],
    }
