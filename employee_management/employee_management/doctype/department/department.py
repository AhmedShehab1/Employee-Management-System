# Copyright (c) 2025, Ahmed Shehab and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Department(Document):
	def before_save(self):
		"""
		Set the title of the department
		"""
		self.title = f"{self.name1} - {self.company}"

	def before_delete(self):
		"""
		Prevent the deletion of the department if there are employees assigned to it
		"""
		if frappe.db.exists("Employee", {"department": self.name}):
			frappe.throw("Cannot delete department, Employees are assigned to this department")
