# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ufec_subject(models.Model):
    _name = 'ufec.subject'

    nom = fields.Char()
    code = fields.Char()

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    professeurs_id = fields.Many2many(comodel_name='ufec.porfesseurs',
                            relation='subj_prof_ref',
                            column1='nom',
                            column2='f_nom')