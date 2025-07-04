# PMIS (Construction Project Management Information System)

This Frappe app provides a comprehensive Project Management Information System tailored for the construction industry.

## Features (Planned & Implemented)

*   **Project Management:**
    *   Detailed Project Setup (WBS, Client, Team, Dates)
    *   Resource Planning (Manpower, Machinery)
    *   Task Scheduling with Dependencies (`Project Schedule Task`)
    *   Daily Work Planning & Logging (`Daily Work Plan`, `Daily Log`)
*   **Pre-Construction:**
    *   Contract Document Management
    *   Rebar Modeling & BBS Linking
    *   Cost Estimation & Bill of Quantities (BOQ)
*   **Construction Execution:**
    *   Daily Progress Tracking
    *   Rebar Execution Logging
    *   Subcontract Management
*   **Financial Control:**
    *   Payment Certificate Generation (Interim & Final)
    *   Variation Order Management
    *   (Future: Detailed Job Costing Reports)
*   **Quality & Safety Assurance:**
    *   Site Inspections with customizable Checklist Templates
    *   Non-Conformance Reports (NCRs)
    *   Snag List / Punch List Management
    *   Toolbox Talk Records
*   **Project Handover & Closeout:**
    *   As-Built Drawing Management
    *   Commissioning Checklists
    *   Final Account Settlement
    *   Lessons Learned Documentation
*   **Reporting & Dashboards:**
    *   Initial Project Status Report
    *   Basic Construction Projects Dashboard
    *   (Future: Comprehensive suite of time-based, cost, resource, and quality reports)

## Installation

1.  Ensure you have a Frappe Bench setup for ERPNext v14.
2.  Navigate to your bench directory: `cd ~/frappe-bench` (or your bench path)
3.  Add the app: `bench get-app https://github.com/[your-github-username]/PMIS` (Replace with your actual repo URL)
4.  Install the app on your site: `bench --site [your-site-name] install-app construction_pmis`

## License

MIT License (Refer to `LICENSE` file for details)
