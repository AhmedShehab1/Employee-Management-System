# Copyright (c) 2025, Ahmed Shehab and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Company(Document):
	def before_delete(self):
		if frappe.db.exists("Department", {"company": self.name}):
			frappe.throw("Cannot delete company, Departments are assigned to this company")
		if frappe.db.exists("Employee", {"company": self.name}):
			frappe.throw("Cannot delete company, Employees are assigned to this company")
