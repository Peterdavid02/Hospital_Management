# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DoctorRegister(models.Model):
    _name = 'Hospital_Management.DoctorRegister'
    _description = 'Es un modulo que se encarga de registrar a doctores en la base de datos'

    Name = fields.Char(string="Doctor's Name")
    LastName = fields.Char(string="Doctor's Last Name")
    DoctorID = fields.Char(string='Doctor ID')
    DoctorsSpecialtyId = fields.Many2many('Hospital_Management.DoctorsSpecialty', string='specialization')
    document = fields.Selection([('Morning', '8 AM - 4 PM'), ('Night', '4 PM - 10 PM')], string="Schedule")
