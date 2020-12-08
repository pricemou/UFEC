# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ufec_Departement(models.Model):
    _name = 'ufec.departement'

    nom = fields.Char()
    code = fields.Char()
    