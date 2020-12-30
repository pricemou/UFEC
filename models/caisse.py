from odoo import models, fields, api
import logging

_logger  = logging.getLogger(__name__)

class Ufec_Caisse(models.Model):
    _name = 'ufec.caisse'

    versement = fields.Char()
    moi = fields.Selection([("Janvier","Janvier"),("Fevrier","Fevrier"),("Avril","Avril"),("Mai","Mai"),("Juin","Juin"),("Juillet","Juillet"),("Aout","Aout"),("Septembre","Septembre"),("Decembre","Decembre")])
    etudiant_id = fields.Many2one(comodel_name='ufec.etudiant')