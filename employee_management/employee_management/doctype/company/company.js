// Copyright (c) 2025, Ahmed Shehab and contributors
// For license information, please see license.txt

frappe.ui.form.on("Company", {
	refresh: function (frm) {
        frm.add_custom_button('Employees', () => {
            frappe.set_route('List', 'Employee', { company: frm.doc.name });
        });
        frm.add_custom_button('Departments', () => {
            frappe.set_route('List', 'Department', { company: frm.doc.name });
        });
	},
});
