# -*- coding: utf-8 -*-

{
    'name': 'Marketing in CRM',
    'version': '1.0',
    'depends': ['marketing', 'crm'],
    'author': 'OpenERP SA',
    'category': 'Hidden/Dependency',
    'description': """
Bridge module between marketing and CRM
    """,
    'website': 'http://www.openerp.com',
    'data': [
        'views/crm.xml',
        'views/res_config.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
}
