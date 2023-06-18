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
    contact_person = fields.Char(string='Person in Charge',required=True, tracking=True)
    
    currency_id = fields.Selection([
        ('KSH', 'KSH'),
        ('USD', 'USD')], string='Currency', tracking=True)
    drc = fields.Char(string='D.R.C Charges',required=True, tracking=True)
    east_africa = fields.Char(string='E.A Charges',required=True, tracking=True)




    