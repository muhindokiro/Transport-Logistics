import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)

class UpdateDetails(http.Controller):

    # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    @http.route('/update_me', type='json', auth='public', cors='*', method=['POST'])
    def update_me(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            user = request.env["logistic.users"].sudo().search([('name', '!=', False),("company_id.id","=",verrification['company_id'][0]),("id","=",verrification['id'])])
            if user:
                user.sudo().write({
                    "id":user.id,
                    "email":data['email'],
                    "mobile":data['mobile'],
                    "name":data['name'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful updated your information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        

    @http.route('/update_customer', type='json', auth='public', cors='*', method=['POST'])
    def update_customer(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            partner_id = request.env["res.partner"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['partner_id'])])
            if partner_id:
                partner_id.sudo().write({
                    'country_id':data['country_id'],
                    "city":data['city'],
                    "name":data['name'],
                    'phone':data['phone'],
                    'email':data['email'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful customer information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
