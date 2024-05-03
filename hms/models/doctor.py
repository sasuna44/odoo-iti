from odoo import fields, models

class Doctors(models.Model):
    _name = "hms.doctor"
    _rec_name = "first_name"
    _description = "Doctor"

    first_name = fields.Char(string="first name", required=True)
    last_name = fields.Char(string="last name", required=True)
    log_ids = fields.One2many(comodel_name='hms.patient.log.history',inverse_name='doctor_id', string="Logs")
    image = fields.Image(string="image")
