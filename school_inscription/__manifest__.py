# -*- coding: utf-8 -*-
{
    'name': "school_inscription",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Stagaire weelite",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'reports/report.xml',
        'reports/candidate_identity_card.xml',
        'views/candidate_views.xml',
        'views/inscription_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
