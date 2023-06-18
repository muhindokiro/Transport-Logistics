# -*- coding: utf-8 -*-
from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import date, datetime, timedelta
from random import randint
from odoo.http import request
from odoo.exceptions import UserError

today = date.today()
import logging

_logger = logging.getLogger(__name__)

class BondNumber(models.Model):
    
    _name = "bond.number"
    _description = "Company Bond Configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
   
    name = fields.Char(string='Bond Number',required=True)
    bond_amount = fields.Integer(string='Bond Amount',required=True, tracking=True)
    bond_duration = fields.Char(string='Bond Duration',required=True, tracking=True, readonly=True, default='1 year')
    purchase_date = fields.Date(string="Purchase Date", tracking=True)
    expiry_date = fields.Date(string="Expiry Date", compute='_compute_expiry_date', readonly=True, tracking=True)
    state = fields.Selection([
        ('draft', 'DRAFT'),
        ('submit', 'SUBMIT'),
        ('activate', 'ACTIVE'),
        ('expired', 'EXPIRED'),], default='draft', store=True, readonly=True, tracking=True)
    
    @api.depends('purchase_date')
    def _compute_expiry_date(self):
        for record in self:
            if record.purchase_date:
                record.expiry_date = record.purchase_date + timedelta(days=365)
            else:
                record.expiry_date = False
    
    def submit_to_manager(self):
        # context = self._context
        # current_uid = context.get('uid')
        # user_id = self.env['res.users'].browse(current_uid).id
        # week_number = 0
        # email_to = self.block_manager_id.work_email
        # template = self.env.ref(
        #     'ooh_logistic_system.mail_template_bond_request_submitted')
        # submit_stage = request.env['crop.stage'].search(
        #     [('name', '=', 'Confirmed')]).id
        
        # managers_to_approve = self._default_res_users_planting_approver_manager()
        # users = self.env.ref('ooh_logistic_system.bond_approver_manager').users
        # try:
        #     email_values = {
        #         'email_to': ','.join(users.mapped('login'))
        #     }
        #     template.send_mail(self.id, force_send=True,
        #                        email_values=email_values)
        #     self.write({'state': 'submit'})

        # except Exception as e:
        #     raise UserError(_(f'Notifying the Block Manager Failed:{e}'))
        return 

    def action_confirm(self):
        # email_to = self.user_id.login
        # template = self.env.ref(
        #     'ooh_logistic_system.mail_template_bond_request_approved')
        # can_approve = self.user_has_groups(
        #     'ooh_logistic_system.bond_approver_manager')
        # if can_approve:
        #     try:
        #         email_values = {
        #             'email_to': email_to
        #         }
        #         template.send_mail(self.id, force_send=True,
        #                            email_values=email_values)
        #         self.write({'state': 'activate'})
        #     except Exception as e:
        #         raise UserError(
        #             _(f'Notifying the Bond Approve Request Failed:{e}'))
        # else:
        #     raise UserError(
        #         _('You dont have sufficient rights to perform this action'))
        return 

    def action_cancel(self):
        for rec in self:
            if not self.reason:
                raise UserError(_("Please Provide Reason for Rejection"))
            else:
                # self.notify_reject_create()
                self.state = 'expired'



