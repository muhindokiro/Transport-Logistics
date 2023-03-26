from odoo import models, fields, api, _
import datetime
import random
import math

today = datetime.date.today()

class ResCompany(models.Model):
    _inherit = 'res.company'
    _description = "Adding Custom Fields in Compnay View"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expire', 'Expired')
        ], 
        default='draft', required=True, tracking=True)

    def create_admin(self):
        if self.state == "draft":
            new_admin = self.env["logistic.users"].sudo().create({
                "name":self.name,
                "email":self.email,
                "company_id":self.id,
                "mobile":self.mobile
            })
            if new_admin:
                self.write({"state":"active"})
                new_admin._prepare_otp_email_values()
        return True
class LogisticUsers(models.Model):
    _name = 'logistic.users'
    _description = "Model for storing logistic users"
    _inherit = ["mail.thread", 'mail.activity.mixin']

    passwd = fields.Char(string="partner password",readonly=True)
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    company_id=fields.Many2one('res.company',string="Compnay",related="log_user_id.company_id")
    log_user_id=fields.Many2one('logistic.users',string="Created By")
    mobile = fields.Char(string="Mobile")
    access_token_ids = fields.One2many('jwt_provider.access_token', 'user_id', string='Access Tokens' )
    otp = fields.Char(string='Otp',readonly=True)
    when_sent = fields.Date(string="Otp Validation")
    state = fields.Selection([
        ('archived', 'Archived'),
        ('active', 'Active')
        ], 
        default='active', required=True, tracking=True)

    def _prepare_otp_email_values(self):
        digits = "0123456789"
        OTP = ""
        if self:
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            self.sudo().write({'otp': OTP, 'when_sent': today})
        mail_user = self.env['ir.mail_server'].sudo().search([('smtp_port', '=', 465)])
        mail_obj = self.env['mail.mail']
        email_from = mail_user.smtp_user
        subject = f"Forgot My Password"
        email_to = self.email
        body_html = f"""
            <html>
            <body>
            <div style="margin:0px;padding: 0px;">
                <p style="padding: 0px; font-size: 13px;">
                    Hello {self.name} !!,
                    <br/>
                    Your request to reset password was successfuly.
                    <br/>
                    use {self.otp} to reset your Password.
                    <br/>
                    Otp is Valid for <strong>1 minute</strong>
                    <br/>
                    if you did not request for this ignore this message.
                    <br/>
                    .
                <br/>
                </p>

                <p>Best Regards
                    <br/>
                The Team</p>
            <br/>
            </div>
            </body>
            </html>
        """
        mail = mail_obj.sudo().create({
            'body_html': body_html,
            'subject': subject,
            'email_from': email_from,
            'email_to': email_to
        })
        mail.send()
        return {
            'code': 200,
            'status': 'success',
            "email": self.email,
            "mail":mail,
            'message': 'A code was Sent to your Email'
        }