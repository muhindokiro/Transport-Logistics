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
    
  
    bond_no = fields.Char(string='Bond Number',required=True)
    name = fields.Char(
        string="Bond Ref",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
    )
    journal_id = fields.Many2one("account.journal",string="Journal",required=True)
    account_id = fields.Many2one("account.account",string="Credit Account",required=True)
    currency_id = fields.Many2one("res.currency",string="Currency",request=True)
    partner_id =fields.Many2one("res.partner",string="Supplier",required=True)
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
    
    @api.model
    def create(self, vals):
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code("bond.number") or _("New")
        res = super(BondNumber, self).create(vals)
        return res
    def _prepare_entry_values(self):
        move_obj = self.env['account.move']
        line_ids = []
        today = fields.Date.today()  # Get the current date

        for request in self:
            move = {
                "ref": "Bond Payment Reference: " + request.name,
                "date": today,
                "journal_id": request.journal_id.id,
            }
            debit_line = {
                "account_id": request.account_id.id,
                "partner_id": request.partner_id.id,
                "name": "Bond Payment Reference: " + request.name,
                "debit": 0.00,
                "credit": request.bond_amount,
                "currency_id": request.currency_id.id,
            }
            line_ids.append((0, 0, debit_line))
            credit_line = {
                "account_id": request.partner_id.property_account_payable_id.id,
                "partner_id": request.partner_id.id,
                "name": "Bond Payment Reference: " + request.name,
                "debit": request.bond_amount,
                "credit": 0.00,
                "currency_id": request.currency_id.id,
            }
            line_ids.append((0, 0, credit_line))

        move.update({'line_ids': line_ids})  # Update 'invoice_line_ids' to 'line_ids'
        entry = move_obj.create(move)
        entry.action_post()
        return True
    def bond_idsbond_ids(self):
        bond_ids=self.env["bond.number"]
        if bond_ids.search([("name",'=',self.bond_no)]):
          raise UserError(_("Bond Number should be unique"))
        if not bond_ids:
            for x in bond_ids.search([("state",'=',"valid")]):
                if x:
                    raise UserError(_("You Alredy have a valid Bond `${self.name}`"))
                else:
                    self._prepare_entry_values()
                    self.write({"state":"valid"})

    @api.depends('purchase_date')
    def _compute_expiry_date(self):
        for record in self:
            if record.purchase_date:
                record.expiry_date = record.purchase_date + timedelta(days=365)
            else:
                record.expiry_date = False


class Product(models.Model):
    _inherit="product.product"

    is_bond=fields.Boolean(string="Is Bond?")
