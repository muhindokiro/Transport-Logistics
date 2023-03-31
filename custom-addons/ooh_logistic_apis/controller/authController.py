from werkzeug.security import generate_password_hash, check_password_hash
from .. import verrifyAuth
from odoo.http import request
from odoo import http
import datetime
import random
import json
import math
import jwt
# bsA@VKV58-qJEB
import logging
import string

_logger = logging.getLogger(__name__)
today = datetime.date.today()
SENSITIVE_FIELDS = ['auth_key', 'auth_key_crypt', 'new_auth_key', 'create_uid', 'write_uid']


class JwtController(http.Controller):
    def key(self):
        return '8dxtZrbfRJQJd2NtPujww3OfwAUfKOXf'

    def _prepare_final_email_values(user):
        mail_user = request.env['ir.mail_server'].sudo().search([('smtp_port', '=', 465)])
        subject = f"Password Changed Successfully"
        mail_obj = request.env['mail.mail']
        email_from = mail_user.smtp_user
        email_to = user.email
        body_html = f"""
            <html>
            <body>
            <div style="margin:0px;padding: 0px;">
                <p style="padding: 0px; font-size: 13px;">
                    Hello {user.name} !!,
                    <br/>
                    Your password was successfuly changed.
                    <br/>
                    We are happy to serve you the best.
                    <br/>
                    .
                <br/>
                </p>

                <p>
                Best Regards
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
        return mail


    def _prepare_otp_email_values(user):
        mail_user = request.env['ir.mail_server'].sudo().search([('smtp_port', '=', 465)])
        mail_obj = request.env['mail.mail']
        email_from = mail_user.smtp_user
        subject = f"Forgot My Password"
        email_to = user.email
        body_html = f"""
            <html>
            <body>
            <div style="margin:0px;padding: 0px;">
                <p style="padding: 0px; font-size: 13px;">
                    Hello {user.name} !!,
                    <br/>
                    Your request to reset password was successfuly.
                    <br/>
                    use {user.otp} to reset your Password.
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
        return mail


    def _prepare_registration_email_values(self, user):
        mail_user = request.env['ir.mail_server'].sudo().search([('smtp_port', '=', 465)])
        mail_obj = request.env['mail.mail']
        email_from = mail_user.smtp_user
        subject = f"SuccessFully Registration"
        email_to = user.email
        body_html = f"""
            <html>
            <body>
            <div style="margin:0px;padding: 0px;">
                <p style="padding: 0px; font-size: 13px;">
                    Hello {user.name} !!,
                    <br/>
                    Your Account was successfully Registered with us.
                    <br/>
                    We hope you will enjoy the best experience as
                    <br/>
                    you track all your invoices and payments.
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
        return mail

    @http.route('/login', type='json', auth='public', cors='*', method=['POST'])
    def login(self, **kw):
        exp = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        data = json.loads(request.httprequest.data)
        email = data['email']
        password = data['password']
        if not email:
            response = {
                'code': 400,
                'message': 'Email address cannot be empty'
            }
            return response
        if not password:
            response = {
                'code': 400,
                'message': 'Password cannot be empty'
            }
            return response
        user = request.env['logistic.users'].sudo().search([('email', '=', email)])
        if user:
            users = check_password_hash(user['passwd'], password)
            if users:
                payload = {
                    'exp': exp,
                    'iat': datetime.datetime.utcnow(),
                    'sub': user['id'],
                    'lgn': user['email'],
                    'name': user['name'],
                    'phone': user['mobile'],
                }
                token = jwt.encode(payload, self.key(), algorithm='HS256')
                request.env['jwt_provider.access_token'].sudo().create({'user_id': user.id, 'expires': exp, 'token': token})
                return {
                    'mobile': user.mobile,
                    'user_name': user.name,
                    'email': user.email,
                    'user_id': user.id,
                    'company_id': user.company_id.id,
                    'company_name': user.company_id.name,
                    'token_type': 'Bearer',
                    'access_token': token,
                    'code': 200
                }

            else:
                return {
                    'code': 401,
                    'status': 'failed',
                    'message': 'Your Password is Incorrect'
                }
        else:
            return {
                'code': 401,
                'status': 'failed',
                'message': 'Email address does not Exist'
            }

    @http.route('/forgot_password', type='json', auth='public', cors='*', method=['POST'])
    def forgot_my_password(self, **kw):
        digits = "0123456789"
        OTP = ""
        data = json.loads(request.httprequest.data)
        email = data['email']
        if not email:
            response = {
                'code': 400,
                'message': 'Email address cannot be empty'
            }
            return response
        users = request.env['logistic.users'].sudo().search([('email', '=', email)])
        if not users:
            response = {
                'code': 400,
                'message': 'Email address does not exist'
            }
            return response
        if users:
            users._prepare_otp_email_values()
            if users.otp:
                return {
                    'code': 200,
                    'status': 'success',
                    "email": users.email,
                    'message': 'A code was Sent to your Email'
                }

    @http.route('/set_password', type='json', auth='public', cors='*', method=['POST'])
    def set_new_password(self, **kw):
        data = json.loads(request.httprequest.data)
        code = data['code']
        password = generate_password_hash(data['password'], method='sha256')
        data['password'] = password
        if not code:
            response = {
                'code': 400,
                'message': 'Email address cannot be empty'
            }
            return response
        if not password:
            response = {
                'code': 400,
                'message': 'Password cannot be empty'
            }
            return response
        users = request.env['logistic.users'].sudo().search([('otp', '=', code)])
        if not users:
            response = {
                'code': 400,
                'message': 'The Code is Invalid'
            }
            return response
        if users:
            diff = ((today - users.when_sent).total_seconds()) / 60
            if diff < 1:
                users.sudo().write({'passwd': password})
                users.sudo().write({'otp': ''})
                # self._prepare_final_email_values(users)
                return {
                    'code': 200,
                    'status': 'success',
                    'message': 'Password Successfully changed'
                }
            else:
                return {
                    'code': 402,
                    'status': 'success',
                    'message': 'The Code has expired'
                }

    @http.route('/logout', type='json', auth='public', cors='*', method=['POST'])
    def logout(self, **kw):
        data = json.loads(request.httprequest.data)
        token = data['token']
        data.pop('token', None)
        result = verrifyAuth.validator.verify_token(token)
        _logger.error(result)
        _logger.error("TESTING THE ")
        if not result['status']:
            response = {
                'code': 400,
                'message': 'Logout Failed'
            }
            return response
        logout = request.env['jwt_provider.access_token'].sudo().search([('token', '=', token)])
        logout.sudo().unlink()
        response = {
            'code': 200,
            'message': 'Logout'
        }
        return response
    
    @http.route('/register', type='json', auth='public', cors='*', method=['POST'])
    def register(self, **kw):
        data = json.loads(request.httprequest.data)
        email = data['email']
        name = data['name']
        mobile = data['mobile']
        token = data['token']
        if not email:
            response = {
                'code': 422,
                'message': 'Email address cannot be empty'
            }
            return response
        if not name:
            response = {
                'code': 422,
                'message': 'Name cannot be empty'
            }
            return response
        if not mobile:
            response = {
                'code': 422,
                'message': 'Phone cannot be empty'
            }
            return response
        verrification = verrifyAuth.validator.verify_token(token)
        if verrification['status']:
            if request.env["logistic.users"].sudo().search([("email", "=", email)]):
                response = {
                    'code': 422,
                    'message': 'Email address already existed'
                }
                return response
            if request.env["logistic.users"].sudo().search([("mobile", "=", mobile)]):
                response = {
                    'code': 422,
                    'message': 'Phone Number already existed'
                }
            users = request.env['logistic.users'].sudo().create({
                "email":data['email'],
                "mobile":data['mobile'],
                "name":data['name'],
                "user_id":verrification['id'],
                "company_id":verrification['company_id']
            })
            if users:
                users._prepare_otp_email_values()
                response = {
                    'code': 200,
                    'message': {
                        'name': users.name,
                        'email': users.email,
                        'mobile': users.mobile,
                        "company_id": users.company_id,
                    }
                }
            return response
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
