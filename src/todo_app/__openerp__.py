# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': 'To-Do Application',  # nombre del módulo
    'summary': "Test",  # muestra un subtitulo del módulo.
    'description': 'Manage your personal Tasks with this module.',  # descripción del módulo
    'website': 'www.test.com',  # dirección de documentación.
    'author': 'Edgar de la Cruz',  # autor    
    'depends': ['mail'],# dependencias, puede tener una lista de otros módulos requeridos. Odoo los instalará automáticamente cuando este módulo sea instalado.
    'version': '1.0',  # versión
    'category': 'Website',  # categoría
    'data' : ['views/todo_view.xml',], # define la lista de archivos que son cargados por el módulo. 
    'installable': True,  # es instalable
    'application': True,  # se considera como una aplicación
    'auto_install': False #se auto instalará
}
