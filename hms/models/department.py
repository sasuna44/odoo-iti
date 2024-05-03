from odoo import fields, models

class Department(models.Model):
    _name = "hms.department"
    _rec_name = "name"
    name = fields.Char(string="name")
    capacity = fields.Integer(string="capacity")
    is_opened = fields.Boolean(string="is opend")
    patient_ids = fields.One2many(comodel_name="hms.patient",inverse_name="department_id", string="patients")
