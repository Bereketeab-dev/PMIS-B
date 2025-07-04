# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt

class CostEstimate(Document):
    def validate(self):
        self.calculate_total_estimated_cost()

    def before_save(self):
        # Ensure total is calculated before final save, especially if items change
        self.calculate_total_estimated_cost()

    def calculate_total_estimated_cost(self):
        total_cost = 0.0
        if self.boq_items:
            for item in self.boq_items:
                total_cost += flt(item.amount)
        self.total_estimated_cost = total_cost

    # After Submit: Potentially lock down certain fields or trigger next steps
    def on_submit(self):
        self.db_set("status", "Submitted") # Or "Approved" if no further workflow defined here
        # Potentially create a budget snapshot or link to project budget

    # On Cancel: Revert status, allow edits again
    def on_cancel(self):
        self.db_set("status", "Cancelled")

    # If you want to allow amendments, you might need an on_update_after_submit method
    # def on_update_after_submit(self):
    #     pass

# This function will be called by BOQ Item child table to update parent
@frappe.whitelist()
def update_total_cost_from_child(parent_name):
    if not parent_name:
        return
    try:
        parent_doc = frappe.get_doc("Cost Estimate", parent_name)
        parent_doc.calculate_total_estimated_cost()
        parent_doc.save(ignore_permissions=True) # Save parent, might need ignore_permissions if called from child context
        frappe.msgprint(f"Cost Estimate {parent_name} total updated.", indicator="green", alert=True)
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error updating total cost from child")
        # frappe.throw(f"Error updating parent Cost Estimate: {e}") # Avoid throwing error that stops child save
        pass # Silently fail or log, as this is a background update. User will see on refresh.
