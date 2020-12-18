# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ufec_Etudiant(models.Model):
    _name = 'ufec.etudiant'
    
    image = fields.Binary()
    matricule = fields.Char(required=True)
    nom = fields.Char(required=True)
    prenom = fields.Char(required=True)
    age = fields.Char(required=True)
    date_de_naissance = fields.Date(required=True)
    lieu_de_naissance = fields.Char()
    sexe = fields.Selection([("Homme","Homme"),("Femme","femme")])
    Nationalite = fields.Char()
    statue_de_enfant= fields.Char(string="Statue de l'enfant")
    adreesse = fields.Text()
    date_inscription= fields.Datetime()

    tuteur = fields.Char(string="Tuteur")
    Non_du_tuteur = fields.Char()
    profession = fields.Char()
    Contacts = fields.Char()

    state = fields.Selection([("l1","Level 1"),("l2","Level 2"),("l3","Level 3"),("fin_parcours","fin parcours")],default='l1')

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    classe_id = fields.Many2one(comodel_name='ufec.classe')

    #champs rellier
    subject_ids= fields.Many2many(related='classe_id.subject_ids')



    @api.multi
    def name_get(self):
        result = []
        for etudiant in self:
            name = '[' + str(etudiant.classe_id.classe_nom) + '] ' + str(etudiant.nom) + ' '+ str(etudiant.prenom)
            result.append((etudiant.id, name))
        return result

    # @api.one
    # @api.constrains('lieu_de_naissance','date_inscription')
    # def date_check(self):
    #     if self.lieu_de_naissance > self.date_inscription  :
    #         raise ValueError('the binary')

    @api.multi
    def next_level(self):
        if self.state == 'l1':
            return self.write({'state':'l2'})
        elif self.state == 'l2':
            return self.write({'state':'l3'})
        elif self.state == 'l3':
            return self.write({'state':'fin_parcours'})
        else:
            raise ValidationError ("l' Etudiants a fini sont parcour scolaire ")
