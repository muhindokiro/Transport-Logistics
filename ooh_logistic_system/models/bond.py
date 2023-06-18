# -*- coding: utf-8 -*-
from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import date,datetime
from random import randint
from odoo.exceptions import UserError

today = date.today()
import logging

_logger = logging.getLogger(__name__)

class BondNumber(models.Model):
    
    _name = "bond.number"
    _description = "Company bond configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    
    @api.model
    def calculate_period(self):
        start_date = datetime.strptime(str(self.purchase_date), "%Y-%m-%d")
        end_date = datetime.strptime(str(self.expiry_date), "%Y-%m-%d")
        months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        if end_date.day < start_date.day:
            months -= 1
        return months
    name = fields.Char(string='Bond Number',required=True)
    purchase_date = fields.Date(string="Purchase Date")
    expiry_date = fields.Date(string="Expiry Date")
    validity_period=fields.Char(string="Validity Period(Months)")
    bond_amount = fields.Integer(string='Bond Amount',required=True, tracking=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("valid", "Valid"),
            ("expired", "Expired"),
        ],
        default="draft",
        tracking=True,
    )
    def validate_bond(self):
        bond_ids=self.env["bond.number"].sudo().search([("state","in",['draft','valid','expired']),("name",'=',self.name)])
        if bond_ids:
          raise UserError(_("Bond Number should be unique"))
        if not bond_ids:
            self.write({"state":"valid"})