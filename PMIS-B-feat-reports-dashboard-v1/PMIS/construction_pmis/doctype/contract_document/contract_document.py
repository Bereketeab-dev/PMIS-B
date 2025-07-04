# Copyright (c) [Your Name/Organization] and contributors. For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ContractDocument(Document):
    def validate(self):
        # Clear party fields based on party_type
        if self.party_type != "Client":
            self.client = None
        if self.party_type != "Supplier":
            self.supplier = None
        if self.party_type != "Consultant": # Assuming consultant might also use supplier link or a dedicated one
            self.consultant = None # Adjust if consultant links to a different DocType
        if self.party_type != "Other":
            self.other_party_name = None

        # Ensure at least one party is selected if party_type is not blank
        if self.party_type:
            if self.party_type == "Client" and not self.client:
                frappe.throw(f"Please select a Client for Party Type '{self.party_type}'")
            elif self.party_type == "Supplier" and not self.supplier:
                frappe.throw(f"Please select a Supplier for Party Type '{self.party_type}'")
            elif self.party_type == "Consultant" and not self.consultant: # Adjust as needed
                frappe.throw(f"Please select a Consultant for Party Type '{self.party_type}'")
            elif self.party_type == "Other" and not self.other_party_name:
                frappe.throw(f"Please enter Other Party Name for Party Type '{self.party_type}'")

    pass
