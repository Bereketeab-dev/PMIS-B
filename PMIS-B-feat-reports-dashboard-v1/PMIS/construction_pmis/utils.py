# Utility functions for Construction PMIS app
# import frappe

# Example utility function:
# def get_project_details(project_id):
#     project = frappe.get_doc("Project", project_id) # Assuming your custom Project DocType
#     return {
#         "name": project.name,
#         "status": project.status,
#         # Add other details you might need
#     }

# def get_query(doctype, txt, searchfield, start, page_len, filters):
#     """
#     Example function for custom query in Link fields.
#     To be used in `get_query` property of a Link field in a DocType.
#     e.g., options: construction_pmis.utils.get_query
#     """
#     if doctype == "YourTargetDocType":
#         # Implement your custom filtering logic here
#         conditions = []
#         if filters and filters.get("custom_filter_field"):
#             conditions.append(f"custom_field = '{filters.get('custom_filter_field')}'")
#
#         # Base query
#         query = f"SELECT name, display_field FROM `tab{doctype}` WHERE `{searchfield}` LIKE '%{txt}%'"
#         if conditions:
#             query += " AND " + " AND ".join(conditions)
#
#         query += f" ORDER BY modified DESC LIMIT {start}, {page_len}"
#
#         return frappe.db.sql(query, as_dict=1)
#     pass

pass
