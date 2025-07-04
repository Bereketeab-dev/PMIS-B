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
            "label": _("Client"),
            "fieldname": "client",
            "fieldtype": "Link",
            "options": "Customer",
            "width": 150
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Start Date"),
            "fieldname": "start_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("End Date"),
            "fieldname": "end_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": _("Total Estimated Cost (Approved)"),
            "fieldname": "total_estimated_cost",
            "fieldtype": "Currency",
            "width": 200
        }
    ]

def get_data(filters):
    conditions = " WHERE 1=1"
    if filters:
        if filters.get("project"):
            conditions += f" AND p.name = '{filters.get('project')}'"
        if filters.get("client"):
            conditions += f" AND p.client = '{filters.get('client')}'"
        if filters.get("status"):
            conditions += f" AND p.status = '{filters.get('status')}'"

    sql_query = f"""
        SELECT
            p.name AS project_name,
            p.client,
            p.status,
            p.start_date,
            p.end_date,
            (SELECT ce.total_estimated_cost
             FROM `tabCost Estimate` ce
             WHERE ce.project = p.name AND ce.status = 'Approved'
             ORDER BY ce.creation DESC LIMIT 1) AS total_estimated_cost
        FROM
            `tabProject` p
        {conditions}
        ORDER BY
            p.creation DESC
    """

    data = frappe.db.sql(sql_query, as_dict=True)
    return data
