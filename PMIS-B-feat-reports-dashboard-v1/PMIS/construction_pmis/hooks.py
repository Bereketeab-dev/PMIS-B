app_name = "construction_pmis"
app_title = "Construction PMIS"
app_publisher = "[Your Name/Organization]"
app_description = "Construction Project Management Information System"
app_email = "[your.email@example.com]"
app_license = "MIT"
app_version = "0.0.1"

# required_apps = ["erpnext"] # Uncomment if your app depends on ERPNext features

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/construction_pmis/css/construction_pmis.css"
# app_include_js = "/assets/construction_pmis/js/construction_pmis.js"

# include js, css files in header of web template
# web_include_css = "/assets/construction_pmis/css/construction_pmis.css"
# web_include_js = "/assets/construction_pmis/js/construction_pmis.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "construction_pmis/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Project" : "public/js/project.js"}
# doctype_list_js = {"Project" : "public/js/project_list.js"}
# doctype_tree_js = {}
# doctype_calendar_js = {}

# Svg Icons
# ------------------
# app_svg_icons = "/assets/construction_pmis/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "construction_pmis.utils.jinja_methods",
#	"filters": "construction_pmis.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "construction_pmis.install.before_install"
# after_install = "construction_pmis.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "construction_pmis.uninstall.before_uninstall"
# after_uninstall = "construction_pmis.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being integrated is the key
# setup_integrations = {
#	"erpnext": {
#		"custom_fields": {
#			"Purchase Invoice": [
#				{
#					"fieldname": "construction_project",
#					"label": "Construction Project",
#					"fieldtype": "Link",
#					"options": "Project", # This should be our custom Project DocType
#					"insert_after": "project" # Example: insert after existing project field
#				}
#			]
#		}
#	}
# }


# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "construction_pmis.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "construction_pmis.custom_dashboards.get_task_dashboard_data"
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"construction_pmis.tasks.all"
#	],
#	"daily": [
#		"construction_pmis.tasks.daily"
#	],
#	"hourly": [
#		"construction_pmis.tasks.hourly"
#	],
#	"weekly": [
#		"construction_pmis.tasks.weekly"
#	],
#	"monthly": [
#		"construction_pmis.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "construction_pmis.install.before_tests"

# Overriding Methods API Hook
# ---------------------------
#
# override_whitelisted_methods = {
#	"frappe.core.doctype.file.file.upload_file": "construction_pmis.utils.upload_file_override"
# }


# Report Overrides
# ----------------
#
# report_override = {
#    "Some Standard Report": "construction_pmis.reports.custom_some_standard_report.execute"
# }


# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"Project": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"cron": {
#		"0 0 * * *": [
#			"construction_pmis.tasks.cron_task"
#		]
#	}
# }

# Fixtures
# --------
# List of fixtures to be exported when `bench export-fixtures` is run
fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Construction PMIS"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Construction PMIS"]]},
    # Add DocTypes if you want their records to be part of fixtures (e.g., default templates)
    # For just exporting the DocType structure itself, they are handled by normal app export/import.
    # If you create specific records (like a default Checklist Template later), you might add:
    # {"doctype": "Checklist Template", "filters": [["name", "in", ["Default Quality Checklist"]]]},

    # For now, we are primarily creating DocTypes.
    # If specific default records for these DocTypes were also created and need to be fixtures,
    # they would be listed here. E.g., if we made a "Default Project Status" record for a
    # "Project Status" DocType (which we haven't), it would be:
    # {"dt": "Project Status", "filters": [["name", "=", "Default Active Status"]]}

    # Typically, for custom DocTypes themselves, you don't list the DocType name here unless you
    # are exporting specific *data records* of that DocType as fixtures.
    # The structure (JSON files) are part of the app's definition.
    {"dt": "Report", "filters": [["module", "=", "Construction PMIS"]]},
    {"dt": "Dashboard Chart Source", "filters": [["module", "=", "Construction PMIS"]]},
    {"dt": "Number Card", "filters": [["module", "=", "Construction PMIS"]]},
    {"dt": "Dashboard", "filters": [["module", "=", "Construction PMIS"]]},
]

# Boot Session
# ---------------------
#
# boot_session = "construction_pmis.boot.boot_session"


# Server Driven Page Rendering
# --------------------------------
#
# server_renderer = [
#	"construction_pmis.www.some_page.get_context"
# ]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"delete": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"delete": 1,
#	},
# ]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "construction_pmis.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Custom Linked Child Tables
# --------------------------
# If you have child DocTypes that are not automatically discovered
# (e.g., an item table in a custom DocType linking to Sales Order Item)
# related_tables = ["custom_doctype_item"]

# Update Email Template
# --------------------------------
# update_email_template = {
#     "Order Confirmation": "construction_pmis.email_templates.order_confirmation.html"
# }

# Custom HTML Profiles
# ------------------------------------
# custom_html_profiles = {
#    "User": "construction_pmis.www.user_profile.html"
# }
pass
