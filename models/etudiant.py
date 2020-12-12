# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ufec_Etudiant(models.Model):
    _name = 'ufec.etudiant'
    
    image = fields.Binary('')
    nom = fields.Char()
    prenom = fields.Char()
    age = fields.Char()
    lieu_de_naissance = fields.Date()
    sexe = fields.Selection([("Homme","Homme"),("Femme","femme")])
    Nationalite = fields.Char()
    statue_de_enfant= fields.Char()
    adreesse = fields.Text()
    date_inscription= fields.Datetime()

    tuteur = fields.Char(string="Tuteur")
    Non_du_tuteur = fields.Char(string="string")
    profession = fields.Char()
    Contacts = fields.Char()

    state = fields.Selection([("l1","Level 1"),("l2","Level 2"),("l3","Level 3"),("fin_parcours","fin parcours"),])

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    classe_id = fields.Many2one(comodel_name='ufec.classe')

    #champs relier
    subject_ids= fields.Many2many(related='classe_id.subject_ids')



    @api.multi
    def name_get(self):
        result = []
        for etudiant in self:
            name = '[' + str(etudiant.classe_id.classe_nom) + '] ' + str(etudiant.nom) + ' '+ str(etudiant.prenom)
            result.append((etudiant.id, name))
        return result

    @api.one
    @api.constrains('lieu_de_naissance','date_inscription')
    def date_check(self):
        if self.date_inscription > self.lieu_de_naissance:
            raise ValueError('the binary')

    @api.multi
    def next_level(self):
        if self.state == 'l1':
            return self.write({'state':'l2'})
        elif self.state == 'l2':
            return self.write({'state':'l3'})
        elif self.state == 'l3':
            return self.write({'state':'fin_parcours'})
        elif self.state == 'fin_parcours':
            return {'warning': {'title': 'warning', 'message':'Nombre de matiere est suprieur a 3'}}
