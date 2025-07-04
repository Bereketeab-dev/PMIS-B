# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import getdate, nowdate, date_diff

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "label": _("Task Name"),
            "fieldname": "task_name",
            "fieldtype": "Link",
            "options": "Project Schedule Task",
            "width": 250
        },
        {
            "label": _("Project"),
            "fieldname": "project",
            "fieldtype": "Link",
            "options": "Project",
            "width": 180
        },
        {
            "label": _("Assigned To"),
            "fieldname": "assigned_to",
            "fieldtype": "Link",
            "options": "User",
            "width": 150
        },
        {
            "label": _("Start Date"),
            "fieldname": "start_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("End Date"),
            "fieldname": "end_date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Days Overdue"),
            "fieldname": "days_overdue",
            "fieldtype": "Int",
            "width": 100
        }
    ]

def get_data(filters):
    conditions = " AND t.status NOT IN ('Completed', 'Cancelled') AND t.end_date < %(current_date)s"
    filter_values = {"current_date": nowdate()}

    if filters:
        if filters.get("project"):
            conditions += " AND t.project = %(project)s"
            filter_values["project"] = filters.get("project")
        if filters.get("assigned_to"):
            conditions += " AND t.assigned_to = %(assigned_to)s"
            filter_values["assigned_to"] = filters.get("assigned_to")

    sql_query = f"""
        SELECT
            t.name AS task_name,
            t.project,
            t.assigned_to,
            t.start_date,
            t.end_date,
            t.status,
            DATEDIFF(%(current_date)s, t.end_date) AS days_overdue
        FROM
            `tabProject Schedule Task` t
        WHERE
            1=1 {conditions}
        ORDER BY
            t.end_date ASC
    """

    data = frappe.db.sql(sql_query, filter_values, as_dict=True)
    return data
