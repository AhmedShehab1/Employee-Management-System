# Copyright (c) 2025, Ahmed Shehab and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestEmployee(UnitTestCase):
	"""
	Unit tests for Employee.
	Use this class for testing individual functions and methods.
	"""

	def setUp(self):
		self.company = frappe.get_doc({"doctype": "Company", "name1": "Test Company"}).insert()

		self.department = frappe.get_doc(
			{"doctype": "Department", "name1": "Test Department", "company": self.company.name}
		).insert()

		self.employee = frappe.get_doc(
			{
				"doctype": "Employee",
				"name1": "Test Employee",
				"email": "test@example.com",
				"address": "Test Address",
				"mobile_no": "+201274315689",
				"position": "Test Position",
				"department": self.department.name,
				"company": self.company.name,
			}
		).insert()

	def tearDown(self):
		self.employee.delete()
		self.department.delete()
		self.company.delete()

	def test_title(self):
		"""
		Test the title of the employee
		"""
		self.assertEqual(
			self.employee.title, f"{self.employee.name1} - {self.department.name1}, {self.company.name1}"
		)


class IntegrationTestEmployee(IntegrationTestCase):
	"""
	Integration tests for Employee.
	Use this class for testing interactions between multiple components.
	"""

	pass
