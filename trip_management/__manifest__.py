{
    'name': "Trip Management",
    'summary': """This module will to run a trip service""",
    'version': '15.0.1.0.0',
    'description': """This module will add a record to for trip details""",
    'author': '@Muhindo-Kiro',
    'category': 'Tools',
    'depends': ['base','hr','contacts','ooh_logistic_system','fleet','account'],
    'license': 'AGPL-3',
    'data': [
        'views/trips.xml',
        # 'views/trip_expense.xml',
        'data/sequence.xml',
        'views/menu_action.xml',
        "views/menu_item.xml",
        'reports/trip_report.xml',
        'security/ir.model.access.csv',
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,

}