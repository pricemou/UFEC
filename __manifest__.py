# -*- coding: utf-8 -*-
{
    'name': "UFEC",

    'summary': """""",

    'description': """
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/etudiant.xml',
        'views/classe.xml',
        'views/departement.xml',
        'views/professeurs.xml',
        'views/subject.xml',
        'views/caisse.xml',
        'views/menu.xml',
        'reports/report.xml',
        'reports/partient_card.xml',
        'views/send_mail.xml',
        'data/mail_template.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}