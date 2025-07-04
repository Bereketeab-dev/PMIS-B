# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt

class BOQItem(Document):
    def validate(self):
        self.calculate_amount()
        # After calculating, if part of a Cost Estimate, trigger update on parent
        # This is often better handled client-side via JS or on parent's save,
        # but can be done here if immediate server-side update is desired.

    def on_change(self): # Note: on_change might not always trigger as expected for child table interactions from UI
        self.calculate_amount()

    def before_save(self):
        self.calculate_amount()

    def calculate_amount(self):
        self.amount = flt(self.quantity) * flt(self.rate)

    # Example: Call parent document method to update totals when a child item changes
    # This is typically done from client-side JS for better UX,
    # or the parent recalculates on its own validate/before_save.
    # If doing it from here, ensure it doesn't cause save loops.
    def on_update(self):
        if self.parenttype == "Cost Estimate" and self.parent:
            # Simple way: let parent recalculate on its next save.
            # More proactive:
            # frappe.get_doc(self.parenttype, self.parent).calculate_total_estimated_cost()
            # frappe.get_doc(self.parenttype, self.parent).save() # Be cautious with auto-saving parent
            # Consider using the whitelisted function in Cost Estimate if needed:
            # frappe.call("construction_pmis.construction_pmis.doctype.cost_estimate.cost_estimate.update_total_cost_from_child", parent_name=self.parent)
            pass # Parent's validate/before_save will handle recalculation.

    def on_trash(self):
        # If an item is deleted, parent should also recalculate
        if self.parenttype == "Cost Estimate" and self.parent:
            # Similar to on_update, parent will recalculate on its save.
            # If immediate update is needed and parent isn't being saved:
            # frappe.call("construction_pmis.construction_pmis.doctype.cost_estimate.cost_estimate.update_total_cost_from_child", parent_name=self.parent)
            pass
