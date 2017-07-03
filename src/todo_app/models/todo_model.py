#-*- coding:utf-8 -*-
from openerp import models, fields 
"""
Por default odoo agrega cinco campos a cualquier modelo automaticamente que son:
- id: Este es el identificador único para cada registro en un modelo en particular. 
- create_date y create_uid: Estos nos indican cuando el registro fue creado y quien lo creó, respectivamente.
 - write_date y write_uid: Estos nos indican cuando fue la última vez que el registro fue modificado y quien lo modificó.
"""

class TodoTask(models.Model):
    _name = 'todo.task'#identificador que utilizará odoo para referirse a este modelo
    name = fields.Char('Description', required = True)#Nombre de campo especial, odoo lo usará como titulo del registro cuando sea referenciado desde otro modelo. Description >> Label 
    active = fields.Boolean('Active', default=True)#Nombre de campo especial, es usado para desactivar registros, por default solo los registros activos son mostrados.
    is_done = fields.Boolean('Done?')