import frappe


def update_department_count(doc, method):
	"""
	Update the department count in the company doctype
	"""
	company = frappe.get_doc("Company", doc.company)
	dep_count = frappe.db.count("Department", {"company": company})
	company.db_set("department_count", dep_count)
