# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class School_inscriptionCandidate(models.Model):
    _name = 'school_inscription.candidate'
    _description = 'school_inscription.school_inscription'
    f_name = fields.Char('Prénom', required=True, help='Prénom de candidat')
    l_name = fields.Char('Nom', required=True, help='Nom de candidat')
    sexe = fields.Selection([('male', 'Masculin'), ('female', 'Féminin')])
    identity_car = fields.Char('CIN', required=True, help='Nom de candidat')
    address = fields.Text('Adress')
    birthday = fields.Date('Date naissance')
    email = fields.Char('Email')
    phone = fields.Char('Tel')
    country = fields.Char('Pays')
    region = fields.Char('Région')
    picture_identity = fields.Image(string="Photo d’identité")
    copy_identity_card = fields.Image(string="Copie CIN")
    inscription_id = fields.Many2one(comodel_name='school_inscription.inscription')

    @api.constrains('identity_car')
    def _check_identity_car(self):
        for rec in self:
            domain = [('identity_car', '=', rec.identity_car)]
            count = self.sudo().search_count(domain)
            if count > 1:
                raise ValidationError("Numéro de carte d'identité doit être unique")

    def name_get(self):
        result = []
        for candidate in self:
            name = candidate.f_name + ' ' + candidate.l_name
            result.append((candidate.id, name))
        return result



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100