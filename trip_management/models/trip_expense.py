# -*- coding: utf-8 -*-
from dataclasses import field
from odoo import models, fields, api, _
from datetime import date

today = date.today()
import logging

class TripExpense(models.Model):
    _inherit = 'fleet.vehicle.log.services'
    _description = "Model that adds trip expenses"
    
    trip_expenses = fields.Many2one('vehicle.trip', string="Trip Expenses")


