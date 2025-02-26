# Copyright (c) 2025, Ahmed Shehab and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestCompany(UnitTestCase):
	"""
	Unit tests for Company.
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

		self.company.reload()

	def tearDown(self):
		"""
		Delete test records created as part of the tests
		"""
		self.employee.delete()
		self.department.delete()
		self.company.delete()

	def test_number_of_departments(self):
		"""
		Test the number of departments in the company
		"""
		self.assertEqual(self.company.department_count, 1)

	def test_number_of_employees(self):
		"""
		Test the number of employees in the company
		"""
		self.assertEqual(self.company.employee_count, 1)

	def test_prevention_of_deletion(self):
		"""
		Test that the company cannot be deleted if there are departments or employees assigned to it
		"""
		self.assertRaises(frappe.exceptions.ValidationError, self.company.delete)


class IntegrationTestCompany(IntegrationTestCase):
	"""
	Integration tests for Company.
	Use this class for testing interactions between multiple components.
	"""

	pass
