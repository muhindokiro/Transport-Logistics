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
    bond_duration = fields.Char(string='Bond Duration',required=True, tracking=True,readonly=True, default='1 year')
    purchase_date = fields.Date(string="Purchase Date", tracking=True)
    expiry_date = fields.Date(string="Expiry Date", compute='_compute_expiry_date', readonly=True, tracking=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("valid", "Valid"),
            ("expired", "Expired"),
        ],
        default="draft",
        tracking=True,
    )
    def bond_idsbond_ids(self):
        bond_ids=self.env["bond.number"].sudo().search([("state","in",['draft','valid','expired']),("name",'=',self.name)])
        if bond_ids:
          raise UserError(_("Bond Number should be unique"))
        if not bond_ids:
            self.write({"state":"valid"})

    @api.depends('purchase_date')
    def _compute_expiry_date(self):
        for record in self:
            if record.purchase_date:
                record.expiry_date = record.purchase_date + timedelta(days=365)
            else:
                record.expiry_date = False


