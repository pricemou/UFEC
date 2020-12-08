from odoo import models, fields, api

class Ufec_professeurs(models.Model):
    _name = 'ufec.porfesseurs'

    image = fields.Binary('')
    nom = fields.Char()
    prenom = fields.Char()
    identifiant_carte = fields.Char()
    sexe = fields.Selection([("Homme","Homme"),("Femme","femme")])
    telephone= fields.Text()
    adresse = fields.Text()
    Nationalite = fields.Char()
    Responsabilite = fields.Char()
    NBR_jours = fields.Char()
    salaire = fields.Text()
    date_inscription= fields.Datetime()