from odoo import models, fields, api

class Ufec_classe(models.Model):
    _name = 'ufec.classe'

    classe_nom = fields.Char(string='Nom')
    code = fields.Char()

    student_ids = fields.One2many(comodel_name='ufec.etudiant', inverse_name='classe_id')
    professeurs_id = fields.Many2many(comodel_name='ufec.porfesseurs',
                            relation='class_prof_ref',
                            column1='nom',
                            column2='f_nom')

    subject_id = fields.Many2many(comodel_name='ufec.subject',
                            relation='class_subj_ref',
                            column1='classe_nom',
                            column2='nom')
    