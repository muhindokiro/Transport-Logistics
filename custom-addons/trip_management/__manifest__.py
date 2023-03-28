{
    'name': "Trip Management",
    'summary': """This module will to run a trip service""",
    'version': '15.0.1.0.0',
    'description': """This module will add a record to for trip details""",
    'author': '@Muhindo-Kiro',
    'category': 'Tools',
    'depends': ['base','hr','contacts','ooh_logistic_system','fleet','ooh_logistic_apis'],
    'license': 'AGPL-3',
    'data': [
        'views/trips.xml',
        'views/menu_action.xml',
        "views/menu_item.xml",
        'security/ir.model.access.csv',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}