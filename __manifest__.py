# -*- coding: utf-8 -*-
{
    'name': "puskesmas_sinjay",

    'summary': """
        modul puskesmas coy""",

    'description': """
        modul untuk puskesmas
    """,

    'author': "Fachrul",
    'website': "http://www.fachrul.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/puskesmas_pendaftaran.xml',
        'views/puskesmas_pasien.xml',
        'views/puskesmas_poli.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
