// Copyright (c) 2025, Ahmed Shehab and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee', {
	refresh(frm) {
        frm.toggle_display(['hired_on', 'days_employed'], frm.doc.status === 'Active');
	},
    status: function(frm) {
        frm.toggle_display(['hired_on', 'days_employed'], frm.doc.status === 'Active');
        if (frm.doc.status === 'Active' && !frm.doc.hired_on) {
            frm.set_value('hired_on', frappe.datetime.get_today());
        }
    },
    hired_on: function(frm) {
        if (frm.doc.hired_on) {
            const today = frappe.datetime.get_today();
            const days_employed = frappe.datetime.get_diff(today, frm.doc.hired_on);
            frm.set_values('days_employed', days_employed);
        }
    },
	company: function(frm) {
	    frm.set_query('department', () => {
	        return {
	            filters: {
	                'company': frm.doc.company
	            }
	        }
	    })
	}
})
