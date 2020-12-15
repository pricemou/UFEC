
from odoo import models

class EtudiantXlsx(models.AbstractModel):
    _name = 'report.ufec.report_etudiant_xlx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        print("lines",lines)
        format1 = workbook.add_format({'font_size':14,'align':'vcenter', "bold":True})
        format2 = workbook.add_format({'font_size':10,'align':'vcenter', })
        sheet = workbook.add_worksheet('Etudiant Card Excel')
        sheet.write(2,2,'Matricule',format1)
        sheet.write(2,3,lines.matricule,format2)
        sheet.write(3,2,'Nom',format1)
        sheet.write(3,3,lines.nom,format2)
        sheet.write(4,2,'Prenom',format1)
        sheet.write(4,3,lines.prenom,format2)
        sheet.write(5,2,'sexe ',format1)
        sheet.write(5,3,lines.sexe,format2)
        