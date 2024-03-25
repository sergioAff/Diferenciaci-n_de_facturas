{
    'name': 'Nombre_del_Modulo',
    'version': '1.0',
    'category': 'Contabilidad',
    'summary': 'Agrega una vista de lista para el modelo account.invoice en Contabilidad',
    'author': 'Tu_Nombre',
    'depends': ['base','account'],
    'data': [
        'views/account_invoice_list_view.xml',
    ],
    'installable': True,
    'application': True,
}