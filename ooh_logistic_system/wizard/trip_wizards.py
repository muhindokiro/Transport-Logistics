from dataclasses import field
import string
from odoo import models, fields, api,_
from datetime import datetime
from random import randint
from odoo.exceptions import UserError

# today = date.today()

import logging

_logger = logging.getLogger(__name__)

class TripManager(models.Model):
    
    _name = "trip.management.vehicle"
    _description = "Transporter Management"
    
    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')], string='Transport Type', tracking=True)

    """FOR EXTERNAL TRIP DRIVERS PREFERENCES"""

    external_driver_name = fields.Char(string='Driver Name')
    external_driver_mobile = fields.Char(string='Driver Name')
    external_truck_number = fields.Char(string='Vehicle Plate No.')
    external_turnboy_name = fields.Char(string='Turnboy Name')
    external_turnboy_mobile = fields.Char(string='Driver Name')
    file_ids=fields.Many2one("open.file",string="Related File")


    """INTERNAL TRANSPORTERS"""
    internal_driver = fields.Many2one("hr.employee", string='Driver Name')
    internal_truck = fields.Many2one("fleet.vehicle", string='Vehicle Plate No.')
    internal_turnboy = fields.Many2one("res.partner", string='Turnboy Name')


    def create_transporter(self):
        print("HUSSEIN KADWEKA KATANA")