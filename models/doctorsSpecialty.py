from odoo import fields, models, api


class DoctorsSpecialty(models.Model):
    _name = 'hospital_m.doctor_specialty'
    _description = 'Este modelo gestiona la especialidad de los doctores'

    name = fields.Char(string="Name of specialty")
    area = fields.Char(string="Area of specialty")
