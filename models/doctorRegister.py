# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DoctorRegister(models.Model):
    _name = 'hospital_m.doctor_register'
    _description = 'Es un modulo que se encarga de registrar a doctores en la base de datos'

    name = fields.Char(string="Doctor's Name")
    doctorLastName = fields.Char(string="Doctor's Last Name")
    doctorId = fields.Char(string='Doctor Id')
    doctorsSpecialtyId = fields.Many2one('hospital_m.doctor_specialty', string='specialization')
    doctorSchedule = fields.Selection([('Morning', '8 AM - 4 PM'), ('Night', '4 PM - 10 PM')], string="Schedule")
