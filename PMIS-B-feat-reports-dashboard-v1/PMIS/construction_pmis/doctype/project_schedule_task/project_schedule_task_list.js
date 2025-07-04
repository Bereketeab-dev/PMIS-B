frappe.listview_settings['Project Schedule Task'] = {
    get_indicator: function(doc) {
        var colors = {
            "Open": "grey",
            "In Progress": "blue",
            "Completed": "green",
            "Cancelled": "red",
            "On Hold": "orange"
        };
        return [__(doc.status), colors[doc.status] || "grey", "status,=," + doc.status];
    },
    add_fields: ["project", "start_date", "end_date", "assigned_to"],
    // Custom button example
    // button: {
    //     show: function(doc) {
    //         return doc.status !== "Completed";
    //     },
    //     get_label: function() {
    //         return __('Mark as Complete');
    //     },
    //     get_description: function(doc) {
    //         return __('Mark {0} as Completed', [doc.name])
    //     },
    //     action: function(doc) {
    //         frappe.db.set_value('Project Schedule Task', doc.name, 'status', 'Completed')
    //             .then(r => {
    //                 frappe.listview_settings['Project Schedule Task'].refresh();
    //                 frappe.show_alert({message: __('Task {0} marked as completed', [doc.name]), indicator: 'green'});
    //             });
    //     }
    // }
};
