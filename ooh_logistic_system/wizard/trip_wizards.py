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

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('vehicle.trip') or _('New')
        res = super(TripManager, self).create(vals)
        return res
    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')], string='Transport Type', tracking=True)
    name = fields.Char(string='Trip Reference', readonly=True)

    """FOR EXTERNAL TRIP DRIVERS PREFERENCES"""
    state = fields.Selection([
        ('Draft', 'Draft'),
        ('External', 'External'),
        ('Cancelled', 'Cancelled'),
        ('Finished', 'Finished'),
    ], default='Draft')
    date = fields.Date(string="Departure Date")
    external_driver_name = fields.Char(string='Driver Name')
    external_driver_mobile = fields.Char(string='Driver Mobile')
    external_truck_number = fields.Char(string='Vehicle Plate No.')
    external_turnboy_name = fields.Char(string='Turnboy Name')
    external_turnboy_mobile = fields.Char(string='Turnboy Mobile')
    file_ids=fields.Many2one("open.file",string="Related File")
    ref=fields.Char(string="File Ref",related="file_ids.name")
    partner_id = fields.Many2one('res.partner',string="Client",related="file_ids.customer_id")

    """INTERNAL TRANSPORTERS"""
    internal_driver = fields.Many2one("hr.employee", string='Driver Name')
    internal_truck = fields.Many2one("fleet.vehicle", string='Vehicle Plate No.')
    internal_turnboy = fields.Many2one("res.partner", string='Turnboy Name')
    internal_turnboy_mobile = fields.Char(string='Turnboy Mobile')
