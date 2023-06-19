{
    'name': "Ooh Logistic Center",
    'summary': """This module for home banking""",
    'version': '15.0.1.0.0',
    'description': """This module will add a record to store student details""",
    'author': 'Hussein Kadweka',
    'category': 'Tools',
    'depends': ['base', 'contacts', 'account', 'sale_management', 'stock'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_actions.xml',
        'views/menu_items.xml',
        'views/file.xml',
        'views/bond.xml',
        'views/shipping_line.xml',
        'views/documents.xml'
        # 'wizard/trip_wizard_view.xml'
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'ooh_logistic_system/static/src/scss/styles.css',
        ],
    },
    'installable': True,
    'auto_install': False,
}
