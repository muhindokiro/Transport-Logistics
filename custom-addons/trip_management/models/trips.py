from odoo import models, fields, api,_


class VehicleTrip(models.Model):
    _name = 'vehicle.trip'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('vehicle.trip') or _('New')
        res = super(VehicleTrip, self).create(vals)
        return res
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
    name = fields.Char(string='Trip Reference', readonly=True)
    type = fields.Selection([
        ('internal', 'Internal'),
        ('external', 'External')], string='Transport Type', tracking=True) 
    related_file=fields.Many2one("open.file",string="Related File")
    partner_id = fields.Many2one('res.partner',string="Client",related="related_file.customer_id")
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

    # External Transport Details
    external_driver = fields.Char(string='Driver', required=1)
    external_truck = fields.Char(string='Vehicle', required=1)
    external_turnboy = fields.Char(string='Turnboy', required=1)

    # Internal Transport Details
    internal_driver = fields.Many2one("res.partner", string='Driver', required=1)
    internal_truck = fields.Many2one("fleet.vehicle", string='Vehicle', required=1)
    internal_turnboy = fields.Many2one("res.partner", string='Turnboy', required=1)
    


class VehicleTripLine(models.Model):
    _name = 'vehicle.trip.line'

    service_type = fields.Many2one("fleet.service.type",string='Service', required=1)
    description = fields.Char(string='Description', required=1)
    vendor = fields.Many2one("res.partner",string='Vendor', required=1)
    cost = fields.Float(string='Cost', required=1)
    driver_license = fields.Float(string='License No.', required=1)
    trip_lines = fields.Many2one('vehicle.trip',string="Trip Lines") 