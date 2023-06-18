from odoo import models, fields, api,_

class VehicleTrip(models.Model):
    _name = 'vehicle.trip'
    _description = "The trip management"
    _inherit = ["mail.thread", 'mail.activity.mixin']

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
                total += each.amount
            obj.total_cost = total


    def trip_report(self):
        return self.env.ref("trip_management.trip_report_pdf").report_action(self)
 
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
    trip_lines = fields.One2many('fleet.vehicle.log.services','trip_expenses')
    state = fields.Selection([
        ('Draft', 'Draft'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Progress', 'Progress'),
        ('Finished', 'Finished'),
        ('Paid', 'Paid'),
    ], default='Draft')

    # External Transport Details
    external_driver = fields.Char(string='Driver Name')
    external_driver_mobile = fields.Char(string='Driver Name')
    external_truck = fields.Char(string='Vehicle Plate No.')
    external_turnboy = fields.Char(string='Turnboy Name')
    external_turnboy_mobile = fields.Char(string='Turnboy Name')

    # Internal Transport Details
    internal_driver = fields.Many2one("hr.employee", string='Driver Name')
    internal_truck = fields.Many2one("fleet.vehicle", string='Vehicle Plate No.')
    internal_turnboy = fields.Many2one("res.partner", string='Turnboy Name')
    company_id=fields.Many2one('res.company',string="Company",readonly=True)

    
