# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ufec_Departement(models.Model):
    _name = 'ufec.departement'
    _rec_name = 'nom'

    nom = fields.Char()
    code = fields.Char()
    
    prosseurs_id = fields.One2many(comodel_name='ufec.porfesseurs', inverse_name='deparment_id')
    subject_id = fields.One2many(comodel_name='ufec.subject', inverse_name='deparment_id')  