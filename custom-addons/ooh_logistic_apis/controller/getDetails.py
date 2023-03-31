import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class ValuesDetails(http.Controller):

    # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    @http.route('/me', type='json', auth='public', cors='*', method=['POST'])
    def get_my_details(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        _logger.error(verrification)
        _logger.error("CHECKING THE RESPONSE@@@@@@@@@@@2")
        if verrification['status']:
            # """get all account types"""
            types = request.env["logistic.users"].sudo().search([('name', '!=', False),("company_id.id","=",verrification['company_id'][0]),("id","=",verrification['id'])])
            [values.append({
            "name": x.name if x.name else "",
            "login": x.email if x.email else "",
            "mobile": x.mobile if x.mobile else "",
            'id': x.id
            })
             for x in types]
            return {
                "code": 200,
                "status": "success",
                "me": values,
                "message": "My Details"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
