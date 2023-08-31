# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DoctorRegister(models.Model):
    _name = 'Hospital_Management.DoctorRegister'
    _description = 'Es un modulo que se encarga de registrar a doctores en la base de datos'

    DoctorName = fields.Char(string="Doctor's Name")
    DoctorLastName = fields.Char(string="Doctor's Last Name")
    DoctorId = fields.Char(string='Doctor Id')
    DoctorsSpecialtyId = fields.Many2many('Hospital_Management.DoctorsSpecialty', string='specialization')
    DoctorSchedule = fields.Selection([('Morning', '8 AM - 4 PM'), ('Night', '4 PM - 10 PM')], string="Schedule")
