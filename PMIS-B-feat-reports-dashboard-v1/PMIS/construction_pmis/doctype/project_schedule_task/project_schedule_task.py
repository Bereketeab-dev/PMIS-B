# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, add_days, date_diff

class ProjectScheduleTask(Document):
    def validate(self):
        self.calculate_duration_or_end_date()

    def calculate_duration_or_end_date(self):
        if self.start_date and self.end_date:
            if getdate(self.start_date) > getdate(self.end_date):
                frappe.throw("End Date cannot be before Start Date.")
            self.duration = date_diff(self.end_date, self.start_date) + 1
        elif self.start_date and self.duration:
            if self.duration < 0:
                frappe.throw("Duration cannot be negative.")
            self.end_date = add_days(self.start_date, int(self.duration) -1 if int(self.duration) > 0 else 0)
        elif self.end_date and self.duration: # Less common, but could calculate start_date
             if self.duration < 0:
                frappe.throw("Duration cannot be negative.")
            self.start_date = add_days(self.end_date, - (int(self.duration) -1 if int(self.duration) > 0 else 0))


    # Trigger on save to ensure calculations are always correct if manually changed
    def on_update(self):
        self.calculate_duration_or_end_date()

    # Could also add on_change triggers for start_date, end_date, duration if live updates are needed in UI without save
    # but validate/on_update usually suffice.
