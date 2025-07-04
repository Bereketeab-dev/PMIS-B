frappe.listview_settings['Project'] = {
    get_indicator: function(doc) {
        var colors = {
            "Planning": "orange",
            "Active": "blue",
            "Completed": "green",
            "On Hold": "grey",
            "Cancelled": "red"
        };
        return [__(doc.status), colors[doc.status], "status,=," + doc.status];
    },
    // add_fields: ["client"], // Example: if you want to show client in list view even if not in_list_view by default
    // order_by: "start_date desc"
};
