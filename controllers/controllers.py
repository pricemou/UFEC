# -*- coding: utf-8 -*-
from odoo import http

# class Ufec(http.Controller):
#     @http.route('/ufec/ufec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ufec/ufec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ufec.listing', {
#             'root': '/ufec/ufec',
#             'objects': http.request.env['ufec.ufec'].search([]),
#         })

#     @http.route('/ufec/ufec/objects/<model("ufec.ufec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ufec.object', {
#             'object': obj
#         })