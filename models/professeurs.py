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
    active = fields.Boolean('Active', default=True)
    email = fields.Char()

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

    @api.multi
    def send_mail(self):
        self.ensure_one()
        template_id = self.env.ref('ufec.email_template_prof').id
        ctx = {
            'default_model': 'ufec.porfesseurs',
            'default_res_id': self.id,
            'default_user_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'email_to': self.email,
        } 
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }