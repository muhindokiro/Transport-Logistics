import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class DetailController(http.Controller):

    # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    @http.route('/trip_details', type='json', auth='public', cors='*', method=['POST'])
    def get_trip_details(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            files = request.env["open.file"].sudo().search([("company_id",'=',verrification['company_id']),('id','=',data['fileId'])])
            [values.append({"item": x.product_id, "account_id": x.account_id.name, 'id': x.id,"amount":x.amount})for x in files.file_lines]
            return {
                "code": 200,
                "status": "success",
                "name": files.name,
                "customer": files.customer_id.name,
                "bill_ref": files.bill_ref,
                "country_id": files.country_id,
                "return_date": files.return_date,
                "inv_ref": files.inv_ref,
                "lines":values,
                "message": "File Informations"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/customer_details', type='json', auth='public', cors='*', method=['POST'])
    def get_customer_details(self, **kw):
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            customer = request.env["res.partner"].sudo().search([("company_id",'=',verrification['company_id']),('id','=',data['fileId'])])
            if customer:
                return {
                    "code": 200,
                    "status": "success",
                    "name": customer.name,
                    "country_id": customer.country_id.name,
                    "phone": customer.phone,
                    "email": customer.email,
                    "city": customer.city,
                    "property_account_receivable_id": customer.property_account_receivable_id.name,
                    "property_account_payable_id":customer.property_account_payable_id.name,
                    "message": "Customer Informations"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }