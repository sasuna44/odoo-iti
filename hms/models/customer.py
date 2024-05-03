# from odoo import fields, models, api
# from odoo.exceptions import ValidationError

# class CRM(models.Model):
#     _inherit = 'crm.lead'
#     related_patient_id = fields.Many2one('hms.patient', string='Related Patient')
#     @api.constrains('related_patient_id')
#     def check_email(self):
#         for record in self:
#             if record.related_patient_id and record.related_patient_id.email:
#                 exists_email = self.env['crm.lead'].search([('related_patient_id.email', '=', record.related_patient_id.email)], limit=1)
#                 if exists_email:
#                     raise ValidationError('This eamil is aleardy exists !!')
