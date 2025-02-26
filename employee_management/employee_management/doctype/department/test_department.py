# Copyright (c) 2025, Ahmed Shehab and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestDepartment(UnitTestCase):
	"""
	Unit tests for Department.
	Use this class for testing individual functions and methods.
	"""

	def setUp(self):
		"""
		Create test records before running the tests
		"""
		self.company = frappe.new_doc("Company")
		self.company.name1 = "Test Company"
		self.company.save()
		self.department = frappe.new_doc("Department")
		self.department.company = self.company
		self.department.name1 = "Test Department"
		self.department.save()

		self.employee = frappe.new_doc("Employee")
		self.employee.name1 = "Test Employee"
		self.employee.department = self.department
		self.employee.company = self.company
		self.employee.email = "test@example.com"
		self.employee.address = "Test Address"
		self.employee.mobile_no = "+201274315689"
		self.employee.position = "Test Position"
		self.employee.save()

	def tearDown(self):
		"""
		Delete test records created as part of the tests
		"""
		self.employee.delete()
		self.department.delete()
		self.company.delete()

	def test_title(self):
		"""
		Test the title of the department
		"""
		self.assertEqual(self.department.title, f"{self.department.name1} - {self.department.company}")

	def test_number_of_employees(self):
		"""
		Test the number of employees in the department
		"""
		self.department.reload()
		self.assertEqual(self.department.employee_count, 1)


class IntegrationTestDepartment(IntegrationTestCase):
	"""
	Integration tests for Department.
	Use this class for testing interactions between multiple components.
	"""

	pass
