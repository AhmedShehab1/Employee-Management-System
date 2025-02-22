import frappe

def update_employee_count(doc, method):
    company = frappe.get_doc("Company", doc.company)
    dep = frappe.get_doc("Department", doc.department)
    comp_emp_count = frappe.db.count("Employee", {"company": company})
    dep_emp_count = frappe.db.count("Employee", {"department": dep})
    company.db_set("employee_count", comp_emp_count)
    dep.db_set("employee_count", dep_emp_count)

