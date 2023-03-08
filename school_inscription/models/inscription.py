# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class School_inscriptionInscription(models.Model):
    _name = 'school_inscription.inscription'
    _description = 'school_inscription.school_inscription'
    num_inscription= fields.Char(string="Numéro d'inscription", required=True, help='Numéro d inscription')
    date_inscription = fields.Date('Date inscription')
    candidate_ids = fields.One2many(comodel_name='school_inscription.candidate', inverse_name='inscription_id')
    state = fields.Selection([
        ('l1', 'Nouveau'),
        ('l2', 'Encours de validation'),
        ('l3', 'Terminé'),
        ('l4', 'Annulé')], string='Status', required=True, default='l1')

    def to_validate(self):
        if self.state == 'l1':
            return self.write({'state': 'l2'})
        elif self.state == 'l2':
            raise ValidationError('Inscription est en cours de validation ')
        elif self.state == 'l3':
            raise ValidationError('Inscription est déja confirmée ')
        elif self.state == 'l4':
            raise ValidationError('Inscription est annulée')

    def to_confirm(self):
        if self.state == 'l1':
            raise ValidationError('Inscription est déja confirmée ')
        elif self.state == 'l2':
            return self.write({'state': 'l3'})
        elif self.state == 'l3':
            raise ValidationError('Inscription est déja confirmée ')
        elif self.state == 'l4':
            raise ValidationError('Inscription est annulée')

    def to_cancel(self):
        if self.state != 'l4':
            return self.write({'state': 'l4'})
        elif self.state == 'l4':
            raise ValidationError('Inscription est déja annulée')








#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100