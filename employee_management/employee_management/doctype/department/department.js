// Copyright (c) 2025, Ahmed Shehab and contributors
// For license information, please see license.txt

frappe.ui.form.on("Department", {
	refresh: function (frm) {
        frm.add_custom_button('Employees', () => {
            frappe.set_route('List', 'Employee', { department: frm.doc.name });
        });
	},
});
