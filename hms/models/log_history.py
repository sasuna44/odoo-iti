from odoo import fields, models


class LogHistory(models.Model):
    _name = "hms.patient.log.history"
    _description = "log history"
    description = fields.Text(string="log content ", required=True)

    doctor_id = fields.Many2one(comodel_name="hms.doctor", required=True, string="created by ")
    patient_id = fields.Many2one(comodel_name="hms.patient", required=True)

    date = fields.Datetime(string="log date", default=fields.Datetime.now, required=True)
    issued_for=fields.Char(related="patient_id.first_name", string="patient image")
    
