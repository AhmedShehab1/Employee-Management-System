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

			if isinstance(self.hired_on, str):
				self.hired_on = datetime.strptime(self.hired_on, "%Y-%m-%d").date()

			self.days_employed = (datetime.today().date() - self.hired_on).days
		else:
			self.days_employed = None
			self.hired_on = None
