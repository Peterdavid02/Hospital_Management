from datetime import timedelta

from odoo import models, api
from odoo.exceptions import ValidationError


class NoDuplicateTime(models.Model):
    _inherit = "hospital_m.medical_appointments"

    @api.constrains('patientSchedule', 'doctorId')
    def _check_unique_datetime(self):
        for record in self:
            if record.doctorId:
                min_datetime = record.patientSchedule - timedelta(minutes=20)
                max_datetime = record.patientSchedule + timedelta(minutes=20)
                overlapping_records = self.search([
                    ('id', '!=', record.id),
                    ('doctorId', '=', record.doctorId.id),
                    ('patientSchedule', '>=', min_datetime),
                    ('patientSchedule', '<=', max_datetime),
                ])
                if overlapping_records:
                    raise ValidationError(
                        "Another appointment for the same doctor is scheduled within the 20-minute interval.")
