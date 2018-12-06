# -*- coding: utf-8 -*-
{
    'name': "Vega HR Approval Restriction",

    'summary': """
        This module won't allowed Leave Officer and Leave Manager to approve their own leave""",

    'description': """
        This module won't allowed Leave Officer and Leave Manager to approve their own leave
    """,

    'author': "Yodi Safikri",
    'website': "http://www.yodisafikri.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Leave',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_holidays'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}