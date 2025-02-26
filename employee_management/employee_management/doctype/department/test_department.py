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

	def tearDown(self):
		"""
		Delete test records created as part of the tests
		"""
		self.department.delete()
		self.company.delete()

	def test_title(self):
		"""
		Test the title of the department
		"""
		self.assertEqual(self.department.title, f"{self.department.name1} - {self.department.company}")


class IntegrationTestDepartment(IntegrationTestCase):
	"""
	Integration tests for Department.
	Use this class for testing interactions between multiple components.
	"""

	pass
