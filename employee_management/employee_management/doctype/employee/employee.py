# Copyright (c) 2025, Ahmed Shehab and contributors
# For license information, please see license.txt

from datetime import datetime

from frappe.model.document import Document


class Employee(Document):
	def before_save(self):
		"""
		Set the title of the employee
		"""
		self.title = f"{self.name1} - {self.department}, {self.company}"

	def on_update(self):
		"""
		Automatically calculate the days employed when the employee is hired
		"""
		if self.status == "Hired":
			if not self.hired_on:
				self.hired_on = datetime.today().date()
		else:
			self.hired_on = None

	@property
	def days_employed(self):
		if self.hired_on:
			return (datetime.today().date() - self.hired_on).days
		return None
