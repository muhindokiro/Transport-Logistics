from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import datetime
from random import randint
from odoo.exceptions import UserError

# today = date.today()

import logging

_logger = logging.getLogger(__name__)

class ContainerDetails(models.Model):
    
    _name = "container.details"
    _description = "Container configuration"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    
    name = fields.Char(string='Container Number',required=True, tracking=True)
    shipping_line = fields.Char(string='Shipping Line',required=True, tracking=True)
    container_size = fields.Selection([
        ('CN 1*20', 'CN 1*20'),
        ('CN 1*40', 'CN 1*40'),
        ('UNIT 1*1', 'UNIT 1*1'),
        ('LC 1*1', 'LC 1*1'),
        ('BUK 1*1', 'BUK 1*1')], string='Container Size', tracking=True)
    date_in = fields.Date(string="Date In", default=datetime.now(), tracking=True)
