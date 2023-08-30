# -*- coding: utf-8 -*-
# from odoo import http


# class ScheduleOfMedicalAppointments(http.Controller):
#     @http.route('/schedule__of__medical__appointments/schedule__of__medical__appointments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schedule__of__medical__appointments/schedule__of__medical__appointments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('schedule__of__medical__appointments.listing', {
#             'root': '/schedule__of__medical__appointments/schedule__of__medical__appointments',
#             'objects': http.request.env['schedule__of__medical__appointments.schedule__of__medical__appointments'].search([]),
#         })

#     @http.route('/schedule__of__medical__appointments/schedule__of__medical__appointments/objects/<model("schedule__of__medical__appointments.schedule__of__medical__appointments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schedule__of__medical__appointments.object', {
#             'object': obj
#         })
