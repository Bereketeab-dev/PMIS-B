from frappe import _

def get_data():
    return [
        {
            "module_name": "Construction PMIS",
            "color": "blue",
            "icon": "octicon octicon-briefcase", # Example icon
            "type": "module",
            "label": _("Construction PMIS"),
            "description": "Construction Project Management Information System.",
            "items": [
                # This section will be populated by DocTypes that belong to this module
                # Example of how you might manually add links if needed:
                # {
                #     "type": "doctype",
                #     "name": "Project", # Name of your custom Project DocType
                #     "label": _("Projects"),
                #     "description": _("Construction Projects"),
                #     "onboard": 1, # Show in onboarding
                # },
                # {
                #     "type": "report",
                #     "name": "Project Summary", # Example Report
                #     "label": _("Project Summary Report"),
                #     "doctype": "Project", # Related DocType for context
                #     "is_query_report": True,
                # },
            ]
        }
    ]
