from odoo import fields, models, api


class MedicalAppointments(models.Model):
    _name = 'Hospital_Management.MedicalAppointments'
    _description = 'Este Modelo se encarga de Registrar las citas en la base de datos.'

    PatientName = fields.Char(string="Patient's name")
    PatientLastName = fields.Char(string="Patient's Last name")
    Id = fields.Char(string="Patient's ID")
    DoctorId = fields.Many2many('Hospital_Management.DoctorRegister', string='Doctor')
    PatientSchedule = fields.date
    PatientInsurance = fields.Char(string="Life insurance")
    Note = fields.Text(string="Note")



