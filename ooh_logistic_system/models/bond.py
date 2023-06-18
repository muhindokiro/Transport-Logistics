# -*- coding: utf-8 -*-
from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import date
from random import randint
from odoo.exceptions import UserError

today = date.today()
import logging

_logger = logging.getLogger(__name__)

class BondNumber(models.Model):
    
    _name = "bond.number"
    _description = "Company bond configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    
    name = fields.Char(string='Bond Number',required=True)
    bond_amount = fields.Integer(string='Bond Amount',required=True, tracking=True)

