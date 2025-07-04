frappe.listview_settings['Cost Estimate'] = {
    add_fields: ["project", "status", "date", "total_estimated_cost", "version"],
    get_indicator: function(doc) {
        var colors = {
            "Draft": "grey",
            "Submitted": "blue",
            "Approved": "green",
            "Rejected": "red",
            "Cancelled": "darkgrey" // Changed from 'red' to avoid confusion with 'Rejected'
        };
        return [__(doc.status), colors[doc.status] || "grey", "status,=," + doc.status];
    },
    // Example of custom button for workflow action if not using standard submit/cancel
    // button: {
    //     show: function(doc) {
    //         return doc.docstatus === 0 && doc.status === "Draft"; // Show only for Draft documents
    //     },
    //     get_label: function() {
    //         return __('Submit for Approval');
    //     },
    //     get_description: function(doc) {
    //         return __('Submit {0} for approval', [doc.name]);
    //     },
    //     action: function(doc) {
    //         frappe.call({
    //             method: "frappe.desk.doctype.workflow_action.workflow_action.apply_workflow_action",
    //             args: {
    //                 docname: doc.name,
    //                 doctype: "Cost Estimate",
    //                 action: "Submit" // Replace with your actual workflow action
    //             },
    //             callback: function(r) {
    //                 if (!r.exc) {
    //                     frappe.listview_settings["Cost Estimate"].refresh();
    //                     frappe.show_alert({message: __("Cost Estimate submitted."), indicator: "green"});
    //                 }
    //             }
    //         });
    //     }
    // }
};
