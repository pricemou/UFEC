from odoo import models, fields, api
import logging

_logger  = logging.getLogger(__name__)

class Ufec_classe(models.Model):
    _name = 'ufec.classe'
    _inherit = 'mail.thread'
    _rec_name='classe_nom'

    classe_nom = fields.Char(string='Nom')
    code = fields.Char()

    student_ids = fields.One2many(comodel_name='ufec.etudiant', inverse_name='classe_id')
    professeurs_ids = fields.Many2many(comodel_name='ufec.porfesseurs',
                            relation='class_prof_ref',
                            column1='nom',
                            column2='f_nom')

    subject_ids = fields.Many2many(comodel_name='ufec.subject',
                            relation='class_subj_ref',
                            column1='classe_nom',
                            column2='nom')

    num_prof = fields.Integer(string='Nombre de Professeurs', compute='comp_prof')
    num_sub = fields.Integer(string='Nombre des Matières', compute='comp_sub')
    num_ets = fields.Integer(string='Nombre des Etudiants', compute='comp_stu')
    
    # champ calculer
    def comp_prof(self):
        self.num_prof = len(self.professeurs_ids)

    def comp_sub(self):
        self.num_sub = len(self.subject_ids)
    
    def comp_stu(self):
        self.num_ets = len(self.student_ids)
            
    
    @api.onchange('subject_ids')
    def on_change_state(self):
        if len(self.subject_ids) > 3:
            return {'warning': {'title': 'warning', 'message':'Nombre de matiere est suprieur a 3'}}