# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolInscription(http.Controller):
#     @http.route('/school_inscription/school_inscription', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_inscription/school_inscription/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_inscription.listing', {
#             'root': '/school_inscription/school_inscription',
#             'objects': http.request.env['school_inscription.school_inscription'].search([]),
#         })

#     @http.route('/school_inscription/school_inscription/objects/<model("school_inscription.school_inscription"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_inscription.object', {
#             'object': obj
#         })
