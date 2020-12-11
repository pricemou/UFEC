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

    state = fields.Selection([("L1","Level 1"),("L2","Level 2"),("L3","Level 3"),("fini","fini")])

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    classe_id = fields.Many2one(comodel_name='ufec.classe')

    #champs relier
    subject_ids= fields.Many2many(related='classe_id.subject_ids')

    tuteur = fields.Char()
    Non_du_tuteur = fields.Char()
    profession = fields.Char()
    Contacts = fields.Char()


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
        if self.lieu_de_naissance > self.date_inscription:
            raise ValueError('the binary')

    
    @api.multi
    def next_level(self):
        if self.state == 'L1':
            return self.write({'state':'L2'})
        elif self.state == 'L2':
            return self.write({'state':'L3'})
        elif self.state == 'L3':
            return self.write({'state':'fini'})
        else:
            return {'warning':{'title': 'fini', 'message':'l elever a deja terminer son annee'}}
