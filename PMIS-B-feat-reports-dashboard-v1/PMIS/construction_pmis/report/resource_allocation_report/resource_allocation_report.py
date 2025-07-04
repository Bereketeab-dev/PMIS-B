# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": _("Project Name"),
            "fieldname": "project_name",
            "fieldtype": "Link",
            "options": "Project",
            "width": 200
        },
        {
            "label": _("Resource Type"),
            "fieldname": "resource_type",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": _("Resource Name/Category"),
            "fieldname": "resource_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Quantity / Number"),
            "fieldname": "quantity",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": _("Planned Start Date"),
            "fieldname": "start_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("Planned End Date"),
            "fieldname": "end_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": _("Notes"),
            "fieldname": "notes",
            "fieldtype": "Small Text",
            "width": 200
        }
    ]

def get_data(filters):
    conditions = ""
    filter_values = {}

    if filters:
        if filters.get("project"):
            conditions += " AND prpi.parent = %(project)s"
            filter_values["project"] = filters.get("project")
        if filters.get("resource_type"):
            conditions += " AND prpi.resource_type = %(resource_type)s"
            filter_values["resource_type"] = filters.get("resource_type")

    # `tabProject Resource Plan Item` is a child table of `tabProject`
    # We need to join with `tabProject` to get the project name if desired,
    # or just show the parent project ID if that's sufficient.
    # Here, let's get the project name.

    sql_query = f"""
        SELECT
            prpi.parent AS project_name,
            prpi.resource_type,
            prpi.resource_name,
            prpi.quantity,
            prpi.start_date,
            prpi.end_date,
            prpi.notes
        FROM
            `tabProject Resource Plan Item` prpi
        WHERE 1=1 {conditions}
        ORDER BY
            prpi.parent ASC, prpi.idx ASC
    """
    # Note: prpi.parent will give the Project's name (ID).
    # If you need the project's `project_name` field, you'd join `tabProject`
    # SELECT p.project_name, prpi.resource_type ... FROM `tabProject Resource Plan Item` prpi JOIN `tabProject` p ON prpi.parent = p.name ...
    # For simplicity and since parent is already a Link to Project, prpi.parent (which is project's name) is fine.

    data = frappe.db.sql(sql_query, filter_values, as_dict=True)
    return data
