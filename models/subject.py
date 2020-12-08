# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ufec_subject(models.Model):
    _name = 'ufec.subject'

    nom = fields.Char()
    code = fields.Char()
    