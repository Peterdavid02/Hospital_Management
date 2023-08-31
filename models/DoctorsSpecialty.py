from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'Hospital_Management.DoctorsSpecialty'
    _description = 'Este modelo gestiona la especialidad de los doctores'

    Name = fields.Char()
    Area = fields.Char()
