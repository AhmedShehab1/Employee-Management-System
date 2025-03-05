import frappe


def get_permission_query_conditions(user):
	"""
	Only show the employee's own record to the employee
	"""
	if not user:
		return ""

	if "Employee" in frappe.get_roles(user) and "Manager" not in frappe.get_roles(user):
		return f"`tabEmployee`.email = '{user}'"

	return ""
