from odoo import fields, models, api


class DoctorsSpecialty(models.Model):
    _name = 'Hospital_Management.DoctorsSpecialty'
    _description = 'Este modelo gestiona la especialidad de los doctores'

    Name = fields.Char(string="Name of specialty")
    Area = fields.Char(string="Area of specialty")
