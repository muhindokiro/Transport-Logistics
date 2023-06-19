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

class LogisticEntry(models.Model):
    
    _name = "logistic.entry"
    _description = "T810 Entry Configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    
    t810_no = fields.Char(string='T810 No.',required=True)
    entry_date = fields.Date(string="T810 Entry Date", tracking=True)
    extension_date = fields.Date(string="T810 Extension Date", tracking=True)
    t812_no = fields.Char(string='T812 No.',required=True)
    passed_date = fields.Date(string="T812 Passed Date", tracking=True)
    returned_date = fields.Date(string="T812 Returned Date", tracking=True)
    bond_id = fields.Many2one("bond.number",string="Bond Number", tracking=True, store=True)
    currency_id = fields.Selection([
        ('KSH', 'KSH'),
        ('USD', 'USD')], string='Currency', tracking=True)
    exchange_rate = fields.Integer(string='Exchange Rate',required=True)
    bond_cost = fields.Float(string="Bond Amount", readonly=True)
    cancellation_date = fields.Date(string="T810 Cancellation Date", tracking=True)
    
    @api.onchange('bond_id')
    def _onchange_bond_id(self):
        if self.bond_id:
            self.bond_cost = self.bond_id.bond_amount
        else:
            self.bond_cost = 0.0


