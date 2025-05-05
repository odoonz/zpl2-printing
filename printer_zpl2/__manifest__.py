# Copyright (C) 2016-2022 SUBTENO-IT (<https://subteno-it.fr>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Printer ZPL II",
    "version": "18.0.1.0.0",
    "category": "Printer",
    "summary": "Add a ZPL II label printing feature",
    "author": "SUBTENO-IT, FLorent de Labarre, Graeme Gellatly,"
    "Apertoso NV, Odoo Community Association (OCA)",
    "website": "https://github.com/odoonz/odoonz-addons",
    "license": "AGPL-3",
    "depends": ["base_report_to_printer"],
    "data": [
        "security/ir.model.access.csv",
        "views/printing_label_zpl2.xml",
        "wizard/print_record_label.xml",
        "wizard/wizard_import_zpl2.xml",
    ],
    "installable": True,
}
