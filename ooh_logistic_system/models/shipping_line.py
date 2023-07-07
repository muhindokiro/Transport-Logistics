from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import datetime
from random import randint
from odoo.exceptions import UserError

# today = date.today()

import logging

_logger = logging.getLogger(__name__)

class ShippingLine(models.Model):
    
    _name = "shipping.line"
    _description = "Shipping Line configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    
    name = fields.Char(string='Shipping Line',required=True, tracking=True)
    address = fields.Char(string='Address',required=True, tracking=True)
    tel = fields.Char(string='Telephone',required=True, tracking=True, size=15)
    contact_person = fields.Many2one("res.partner", string='Person in Charge',required=True, tracking=True)
   
    currency_id = fields.Many2one("res.currency",string="Currency", tracking=True, store=True, default=lambda self: self.env.company.currency_id)
    drc = fields.Many2one("product.pricelist", string='D.R.C Charges',required=True, tracking=True)
    east_africa = fields.Many2one("product.pricelist", string='E.A Charges',required=True, tracking=True)




    