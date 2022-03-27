TRANSPORT_MODES = {"Road": 1, "Rail": 2, "Air": 3, "Ship": 4}
VEHICLE_TYPES = {"Regular": "R", "Over Dimensional Cargo (ODC)": "O"}
SUPPLY_TYPE = {"Inward": "I", "Outward": "O"}
DOC_TYPE = {
    "Tax Invoice": "INV",
    "Bill of Supply": "BIL",
    "Bill of Entry": "BOE",
    "Delivery Challan": "CHL",
    "Others": "OTH",
}


dn_ewaybill_fields = [
    {
        "fieldname": "distance",
        "label": "Distance (in km)",
        "fieldtype": "Int",
        "insert_after": "vehicle_no",
        "print_hide": 1,
    },
    {
        "fieldname": "gst_transporter_id",
        "label": "GST Transporter ID",
        "fieldtype": "Data",
        "insert_after": "transporter",
        "fetch_from": "transporter.gst_transporter_id",
        "print_hide": 1,
        "translatable": 0,
    },
    {
        "fieldname": "mode_of_transport",
        "label": "Mode of Transport",
        "fieldtype": "Select",
        "options": "\nRoad\nAir\nRail\nShip",
        "default": "Road",
        "insert_after": "transporter_name",
        "print_hide": 1,
        "translatable": 0,
    },
    {
        "fieldname": "gst_vehicle_type",
        "label": "GST Vehicle Type",
        "fieldtype": "Select",
        "options": "Regular\nOver Dimensional Cargo (ODC)",
        "depends_on": 'eval:(doc.mode_of_transport === "Road")',
        "default": "Regular",
        "insert_after": "lr_date",
        "print_hide": 1,
        "translatable": 0,
    },
    {
        "fieldname": "ewaybill",
        "label": "e-Waybill No.",
        "fieldtype": "Data",
        "depends_on": "eval:(doc.docstatus === 1)",
        "allow_on_submit": 1,
        "insert_after": "customer_name_in_arabic",
        "translatable": 0,
    },
]

si_ewaybill_fields = [
    {
        "fieldname": "transporter_info",
        "label": "Transporter Info",
        "fieldtype": "Section Break",
        "insert_after": "terms",
        "collapsible": 1,
        "collapsible_depends_on": "transporter",
        "print_hide": 1,
    },
    {
        "fieldname": "transporter",
        "label": "Transporter",
        "fieldtype": "Link",
        "insert_after": "transporter_info",
        "options": "Supplier",
        "print_hide": 1,
    },
    {
        "fieldname": "gst_transporter_id",
        "label": "GST Transporter ID",
        "fieldtype": "Data",
        "insert_after": "transporter",
        "fetch_from": "transporter.gst_transporter_id",
        "print_hide": 1,
        "translatable": 0,
        "length": 20,
    },
    {
        "fieldname": "driver",
        "label": "Driver",
        "fieldtype": "Link",
        "insert_after": "gst_transporter_id",
        "options": "Driver",
        "print_hide": 1,
    },
    {
        "fieldname": "lr_no",
        "label": "Transport Receipt No",
        "fieldtype": "Data",
        "insert_after": "driver",
        "print_hide": 1,
        "translatable": 0,
        "length": 30,
    },
    {
        "fieldname": "vehicle_no",
        "label": "Vehicle No",
        "fieldtype": "Data",
        "insert_after": "lr_no",
        "print_hide": 1,
        "translatable": 0,
        "length": 15,
    },
    {
        "fieldname": "distance",
        "label": "Distance (in km)",
        "fieldtype": "Int",
        "insert_after": "vehicle_no",
        "print_hide": 1,
    },
    {
        "fieldname": "transporter_col_break",
        "fieldtype": "Column Break",
        "insert_after": "distance",
    },
    {
        "fieldname": "transporter_name",
        "label": "Transporter Name",
        "fieldtype": "Small Text",
        "insert_after": "transporter_col_break",
        "fetch_from": "transporter.name",
        "read_only": 1,
        "print_hide": 1,
        "translatable": 0,
    },
    {
        "fieldname": "mode_of_transport",
        "label": "Mode of Transport",
        "fieldtype": "Select",
        "options": "\nRoad\nAir\nRail\nShip",
        "insert_after": "transporter_name",
        "print_hide": 1,
        "translatable": 0,
        "length": 5,
    },
    {
        "fieldname": "driver_name",
        "label": "Driver Name",
        "fieldtype": "Small Text",
        "insert_after": "mode_of_transport",
        "fetch_from": "driver.full_name",
        "print_hide": 1,
        "translatable": 0,
    },
    {
        "fieldname": "lr_date",
        "label": "Transport Receipt Date",
        "fieldtype": "Date",
        "insert_after": "driver_name",
        "default": "Today",
        "print_hide": 1,
    },
    {
        "fieldname": "gst_vehicle_type",
        "label": "GST Vehicle Type",
        "fieldtype": "Select",
        "options": "Regular\nOver Dimensional Cargo (ODC)",
        "depends_on": 'eval:(doc.mode_of_transport === "Road")',
        "default": "Regular",
        "insert_after": "lr_date",
        "print_hide": 1,
        "translatable": 0,
        "length": 30,
    },
    {
        "fieldname": "ewaybill",
        "label": "e-Waybill No.",
        "fieldtype": "Data",
        "depends_on": (
            "eval:((doc.docstatus === 1 || doc.ewaybill) && doc.eway_bill_cancelled"
            " === 0)"
        ),
        "allow_on_submit": 1,
        "insert_after": "tax_id",
        "translatable": 0,
        "length": 20,
    },
]

E_WAYBILL_FIELDS = {
    "Sales Invoice": si_ewaybill_fields,
    "Delivery Note": dn_ewaybill_fields,
}

E_WAYBILL_API_FIELDS = {
    ("Sales Invoice", "Delivery Note"): {
        "fieldname": "e_waybill_validity",
        "label": "e-Waybill Valid Upto",
        "fieldtype": "Datetime",
        "read_only": 1,
        "no_copy": 1,
        "print_hide": 1,
        "insert_after": "ewaybill",
        "translatable": 0,
    },
}
