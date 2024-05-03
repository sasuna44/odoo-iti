from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import date
import re

class Patient(models.Model):
    _name = "hms.patient"
    _description = "HMS Patient"
    _rec_name = 'first_name'

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birth_date = fields.Date(string="Birthdate")
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR Ratio")
    pcr_test = fields.Boolean(string="PCR Test")
    image = fields.Image(string="Image")
    address = fields.Text(string="Address")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    blood_group = fields.Selection([
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('o-', 'O-'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ], string="Blood Type")
    department_id = fields.Many2one(comodel_name="hms.department", string="Department")
    doctor_ids = fields.Many2many(comodel_name="hms.doctor")
    department_capacity = fields.Integer(string="Department Capacity", related="department_id.capacity")
    state = fields.Selection([
        ('unstable', 'Unstable'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string="State", default='unstable')

    log_history_ids = fields.One2many(comodel_name="hms.patient.log.history", inverse_name="patient_id", string="Log History")
    email = fields.Char(string="Email", required=True, unique=True)

    @api.constrains('email')
    def check_valid_email(self):
        for patient in self:
            if patient.email and not re.match(r"[^@]+@[^@]+\.[^@]+", patient.email):
                raise ValidationError("Please enter a valid email address.")
            if self.search_count([('email', '=', patient.email)]) > 1:
                raise ValidationError("Sorry!! the email is already taken. Please try another email. ")

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for patient in self:
            if patient.birth_date:
                delta_in_days = (today - patient.birth_date).days
                patient.age = delta_in_days // 365
            else:
                patient.age = 0

    def toggle_state(self):
     if self.state == "unstable":
         self.state = "good"
     elif self.state == "good":
         self.state = "fair"
     elif self.state == "fair":
         self.state = "serious"
     else:
         self.state = "unstable"

