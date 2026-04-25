{
    'name': 'Vendor Bill Payment Validation',
    'version': '1.0.0',
    'summary': 'Restrict payment registration to valid vendor bills',
    'description': """
        This module adds validation when registering payments for Vendor Bills.

        It ensures that:
        - Only posted vendor bills can be paid
        - Miscellaneous journal entries cannot be paid
        - Prevents invalid payment actions from the UI
    """,

    'author': 'Thein Htoo Aung',

    'category': 'Accounting',
    'license': 'LGPL-3',

    'depends': [
        'account',
    ],

    'data': [
        # No XML needed for this module
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}  #type: ignore