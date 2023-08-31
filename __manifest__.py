# -*- coding: utf-8 -*-
{
    'name': "Hospital_Management",

    'summary': """
        Este modulo es para manejar las citas en un hospital""",

    'description': """
        Este modulo es para manejar las citas en un hospital
    """,

    'author': "Pedro David Paredes",
    'website': "",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/MedicalAppointments_view_form.xml',
        'views/DoctorRegister_view_tree.xml',
        'views/DoctorsSpecialty_view_tree.xml',

    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
