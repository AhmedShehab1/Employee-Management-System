# Copyright (c) 2025, Ahmed Shehab and contributors
# For license information, please see license.txt

from datetime import datetime

import frappe
from frappe.model.document import Document


class Employee(Document):
	def before_save(self):
		self.title = f"{self.name1} - {self.department}, {self.company}"

	def on_update(self):
		if self.status == "Hired":
			if not self.hired_on:
				self.hired_on = datetime.today().date()

			if not isinstance(self.hired_on, datetime):
				self.hired_on = datetime.strptime(self.hired_on, "%Y-%m-%d").date()

			self.days_employed = (datetime.today().date() - self.hired_on).days
		else:
			self.days_employed = None
			self.hired_on = None
