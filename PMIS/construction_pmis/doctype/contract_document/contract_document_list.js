frappe.listview_settings['Contract Document'] = {
    add_fields: ["project", "document_type", "party_type", "client", "supplier", "effective_date", "expiry_date"],
    get_indicator: function(doc) {
        // Example: Highlight if nearing expiry (e.g., within 30 days)
        if (doc.expiry_date) {
            const today = frappe.datetime.now_date();
            const expiry = doc.expiry_date;
            if (frappe.datetime.get_diff(expiry, today) < 0) {
                return [__("Expired"), "red", "expiry_date,<," + today];
            } else if (frappe.datetime.get_diff(expiry, today) <= 30) {
                return [__("Nearing Expiry"), "orange", "expiry_date,between," + today + "," + frappe.datetime.add_days(today, 30)];
            }
        }
        return [__(doc.document_type), "blue", "document_type,=," + doc.document_type]; // Default indicator
    }
};
