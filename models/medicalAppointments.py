from odoo import fields, models
import random


class MedicalAppointments(models.Model):
    _name = 'hospital_m.medical_appointments'
    _description = 'Este Modelo se encarga de Registrar las citas en la base de datos.'

    patientName = fields.Char(string="Patient's name")
    patientLastName = fields.Char(string="Patient's Last name")
    patientid = fields.Char(string="Patient's ID",required=True)
    doctorId = fields.Many2one('hospital_m.doctor_register', string='Doctor', required=True)
    patientSchedule = fields.Datetime(string='Date and Time', required=True)
    patientInsurance = fields.Char(string="Life insurance")
    note = fields.Text(string="Note", default="Note")
    code = fields.Char(string='Code', readonly=True, default=lambda self: str(random.randint(10000000, 99999999)))
