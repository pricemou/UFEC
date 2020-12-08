from odoo import models, fields, api

class Ufec_classe(models.Model):
    _name = 'ufec.classe'

    nom = fields.Char()
    code = fields.Char()
    