from odoo import models, fields, api, _
from datetime import datetime
import logging
from random import randint

_logger = logging.getLogger(__name__)


# today = datetime.date.today()
class OpenFile(models.Model):
    _name = 'open.file'
    _description = "The file information and documents management"
    _inherit = ["mail.thread", 'mail.activity.mixin']

    def get_associated_invoice(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree',
            'res_model': 'account.move',
            'domain': [('file_ref', '=', self.name)],
            'context': "{'create': False}"
        }

    def get_associated_trips(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Trips',
            'view_mode': 'tree',
            'res_model': 'vehicle.trip',
            'domain': [('related_file.id', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_count(self):
        unpaid = 0.00
        invoices = self.env['account.move'].search([('file_ref', '=', self.name)])
        for record in invoices:
            unpaid += record.amount_residual
        return self.sudo().write({'invoice_count': unpaid})

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('open.file') or _('New')
        res = super(OpenFile, self).create(vals)
        return res

    def calculate_account_blc(self):
        value = 0.00
        for x in self.file_lines:
            value += x.product_id.list_price
        self.account_total = value
        return True

    state = fields.Selection([
        ('draft', 'DRAFT'),
        ('invoiced', 'INVOICED'),
        ('cancel', 'CANCELLED'),
    ], default='draft', tracking=True)
    name = fields.Char(readonly=True, tracking=True)
    inv_ref = fields.Char(readonly=True, tracking=True, string="Invoice Ref")
    bill_ref = fields.Char(string="Bill Lading Ref", tracking=True)
    date = fields.Date(string="Date", default=datetime.now(), readonly=True, tracking=True)
    arr_date = fields.Date(string="Arrival Date", default=datetime.now(), tracking=True)
    dep_date = fields.Date(string="Departure Date", default=datetime.now(), tracking=True)
    customer_id = fields.Many2one('res.partner', string="Client", tracking=True)
    journal_id = fields.Many2one('account.journal', string="Journal", required=True)
    country_id = fields.Many2one('res.country', string="Destination Country", related="customer_id.country_id")
    return_date = fields.Date(string="Container Return Date", default=datetime.now(), tracking=True)
    rela_docs = fields.One2many('open.file.document', 'assoc_file')
    file_lines = fields.One2many('open.file.line', 'assoc_file_line')
    invoice_payment_term_id = fields.Many2one('account.payment.term')
    account_total = fields.Float(string="Total Amount", tracking=True, compute='calculate_account_blc')
    invoice_count = fields.Integer(compute='compute_count')
    company_id=fields.Many2one('res.company',string="Company",related="log_user_id.company_id",readonly=True)
    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

    def create_invoice(self):
        inv_lines = []
        invoice = self.env['account.move'].sudo().create({
            'partner_id': self.customer_id.id,
            'invoice_date': self.date,
            "move_type": "out_invoice",
            'invoice_payment_term_id': self.invoice_payment_term_id.id,
            "journal_id": self.journal_id.id,
            "file_ref": self.name
        })
        if invoice:
            [inv_lines.append((0, 0,
                               {"product_id": x.product_id, "name": x.name, "account_id": x.account_id.id,
                                "quantity": 1,
                                "price_unit": x.amount})) for x in self.file_lines]
            invoice.invoice_line_ids = inv_lines
            self.write({"inv_ref": invoice.name})
        return True

class OpenFileDocument(models.Model):
    _name = 'open.file.document'
    _description = "The file documents for easy tracking and management"
    _inherit = ["mail.thread", 'mail.activity.mixin']

    date = fields.Date(string="Uploaded On", default=datetime.now(), readonly=True, tracking=True)
    name = fields.Char(string="Document Tittle", tracking=True)
    document = fields.Binary(string="Document")
    assoc_file = fields.Many2one('open.file')
    file_ref = fields.Char(related="assoc_file.name", readonly=True, string="Related File", tracking=True)
    company_id=fields.Many2one('res.company',string="Company",related="log_user_id.company_id",readonly=True)
    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

class OpenFileLine(models.Model):
    _name = 'open.file.line'
    _description = "The Properties of the file for invoice creation"
    _inherit = ["mail.thread", 'mail.activity.mixin']

    product_id = fields.Many2one("product.template", string="Product", tracking=True)
    name = fields.Char(string="Container Number", tracking=True)
    account_id = fields.Many2one('account.account', string="Account", required=True)
    amount = fields.Float(string="Price", related="product_id.list_price")
    assoc_file_line = fields.Many2one('open.file', tracking=True)
    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
    company_id=fields.Many2one('res.company',string="Company",related="log_user_id.company_id",readonly=True)

class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Relating invoice to the file for easy tracking"

    file_ref = fields.Char(string="File ref", readonly=True)
    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

class Account(models.Model):
    _inherit = "account.account"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

# class AccountTax(models.Model):
#     _inherit = "account.tax"
#     _description = "Tracking who created the record above"

#     log_user_id=fields.Many2one('logistic.users',string="Created By")
#     company_id=fields.Many2one('res.company',string="Company",related="log_user_id.company_id")

class HrDepartnent(models.Model):
    _inherit = "hr.department"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

class HrEmployees(models.Model):
    _inherit = "hr.employee"
    _description = "Tracking who created the record above"


    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
    # company_id=fields.Many2one('res.company',string="Company",related="log_user_id.company_id",readonly=True)

class HrStructure(models.Model):
    _inherit = "hr.payroll.structure"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)

class FleetVehicle(models.Model):
    _inherit = "fleet.vehicle"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
class ProductCategory(models.Model):
    _inherit = "product.category"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
    company_id=fields.Many2one('res.company',string="Company",readonly=True)
class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
class FleetVehicleBrand(models.Model):
    _inherit = "fleet.vehicle.model.brand"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
class FleetVehicleModel(models.Model):
    _inherit = "fleet.vehicle.model"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
class AccountJournal(models.Model):
    _inherit = "account.journal"
    _description = "Tracking who created the record above"

    log_user_id=fields.Many2one('logistic.users',string="Created By",required=True)
