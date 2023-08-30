# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DoctorRegister(models.Model):
    _name = 'Doctor.Register'
    _description = 'Es un modulo que se encarga de registrar a doctores en la base de datos'

    Name = fields.Char(string="Doctor's Name")
    LastName = fields.Char(string="Doctor's Last Name")
    DoctorID = fields.Char(string='Doctor ID')
