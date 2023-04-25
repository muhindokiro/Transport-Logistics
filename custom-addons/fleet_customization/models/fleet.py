from odoo import models, fields, api,_
import string

class FleetCustom(models.Model):
    _inherit = "fleet.services"