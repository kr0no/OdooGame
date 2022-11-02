# -*- coding: utf-8 -*-
# from odoo import http


# class OdooGame(http.Controller):
#     @http.route('/odoo_game/odoo_game', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_game/odoo_game/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_game.listing', {
#             'root': '/odoo_game/odoo_game',
#             'objects': http.request.env['odoo_game.odoo_game'].search([]),
#         })

#     @http.route('/odoo_game/odoo_game/objects/<model("odoo_game.odoo_game"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_game.object', {
#             'object': obj
#         })
