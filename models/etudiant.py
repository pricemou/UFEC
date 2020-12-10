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

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    classe_id = fields.Many2one(comodel_name='ufec.classe')

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
