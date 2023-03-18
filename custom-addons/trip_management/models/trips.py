from odoo import models, fields, api,_


class VehicleTrip(models.Model):
    _name = 'vehicle.trip'

    @api.model
    def create(self, vals):
        vals['partner_id'] = self.env['ir.sequence'].next_by_code('vehicle.trip')
        return super(VehicleTrip, self).create(vals)

    @api.depends('trip_lines')
    def get_total(self):
        total = 0
        for obj in self:
            for each in obj.trip_lines:
                total += each.cost
            obj.total_cost = total
    # @api.depends('trip_lines')
    # def get_total(self):
    #     total = 0
    #     for obj in self:
    #         for each in obj.trip_lines:
    #             total += each.cost
    #         obj.total_cost = total


    # name=fields.Char(readonly=True) 
    departure_date = fields.Date(string="Departure Date")
    return_date = fields.Date(string="Return Date")
    trip_ref = fields.Char(string='Trip Reference', required=1)
    is_internal = fields.Boolean("Internal Transport", tracking=True)
    is_external = fields.Boolean("External Transport", tracking=True)
    partner_id = fields.Many2one('res.partner',string="Client")
    total_cost = fields.Float(compute='get_total', string='Total', store=1)
    trip_lines = fields.One2many('vehicle.trip.line','trip_lines') 
    state = fields.Selection([
        ('Draft', 'Draft'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Progress', 'Progress'),
        ('Finished', 'Finished'),
        ('Paid', 'Paid'),
    ], default='Draft')


class VehicleTripLine(models.Model):
    _name = 'vehicle.trip.line'

    vehicle = fields.Char(string='Vehicle', required=1)
    vehicle_plate = fields.Char(string='Vehicle No.', required=1)
    driver_name = fields.Char(string='Driver', required=1)
    driver_contact = fields.Float(string='Contact', required=1)
    driver_license = fields.Float(string='License No.', required=1)
    trip_lines = fields.Many2one('vehicle.trip',string="Trip Lines") 