# -*- coding: utf-8 -*-
from odoo import http

# class Puskesmas(http.Controller):
#     @http.route('/puskesmas/puskesmas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/puskesmas/puskesmas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('puskesmas.listing', {
#             'root': '/puskesmas/puskesmas',
#             'objects': http.request.env['puskesmas.puskesmas'].search([]),
#         })

#     @http.route('/puskesmas/puskesmas/objects/<model("puskesmas.puskesmas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('puskesmas.object', {
#             'object': obj
#         })