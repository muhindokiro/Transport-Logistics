{
    'name': "Ooh Logistic Center",
    'summary': """This module for home banking""",
    'version': '15.0.1.0.0',
    'description': """This module will add a record to store student details""",
    'author': 'DevzKona',
    'category': 'Tools',
    'depends': ['base', 'contacts', 'account', 'sale','stock'],
    'license': 'AGPL-3',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu_actions.xml',
        'views/menu_items.xml',
        'views/file.xml',
        'views/documents.xml',
        "views/compnay.xml"
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
