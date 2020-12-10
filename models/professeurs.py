from odoo import models, fields, api

class Ufec_professeurs(models.Model):
    _name = 'ufec.porfesseurs'

    image = fields.Binary('')
    f_nom = fields.Char(string="Nom")
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

    deparment_id = fields.Many2one(comodel_name='ufec.departement')
    subject_id = fields.Many2one(comodel_name='ufec.subject')

    classe_ids = fields.Many2many(comodel_name='ufec.classe',
                            relation='prof_class_ref',
                            column1='f_nom',
                            column2='classe_nom')

    @api.multi
    def name_get(self):
        result = []
        for porfesseurs in self:
            f_name = '[' + str(porfesseurs.deparment_id.nom) + '] ' + str(porfesseurs.f_nom) + ' '+ str(porfesseurs.prenom)
            result.append((porfesseurs.id, f_name))
        return result
