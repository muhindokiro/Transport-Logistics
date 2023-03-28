import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request


class ModelName(http.Controller):
    # """ENDPOINT TO ALLOW CREATION OF A NEW FILE"""
    # @http.route('/new_chart_account', type='json', auth='public', cors='*', method=['POST'])
    # def create_chart_of_account(self, **kw):
    #     data = json.loads(request.httprequest.data)
    #     # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
    #     verrification = verrifyAuth.validator.verify_token(data['token'])
    #     if verrification['status']:
    #         # """make sure fields are not empty"""
    #         if not data['code']:
    #             response = {
    #                 'code': 422,
    #                 'message': 'Code cannot be empty'
    #             }
    #             return response
    #         if not data['name']:
    #             response = {
    #             'code': 422,
    #             'message': 'Name cannot be empty'
    #             }
    #             return response
    #         if not data['user_type_id']:
    #             response = {
    #             'code': 422,
    #             'message': 'Type cannot be empty'
    #             }
    #             return response
    #         # """verify that code does not existing in the database"""
    #         if request.env["account.account"].sudo().search([("code", "=", data['code'])]):
    #             response = {
    #                 'code': 422,
    #                 'message': 'Account Code should be unique'
    #             }
    #             return response

    #         # """continue if the code does not exist in the database"""
    #         account=request.env["account.account"].sudo().create({
    #             "name":data['name'],
    #             "code":data['code'],
    #             "user_type_id":data['user_type_id'],
    #             "company_id":verrification['company_id']
    #         })
    #         # """return the response if the action is successful"""
    #         if account:
    #             return {
    #                 "code":200,
    #                 "status":"Success",
    #                 "message":"YOu have added a chart of account"
    #             }
    #     else:
    #         return {
    #             "code":403,
    #             "status":"Failed",
    #             "Message":"NOT AUTHORISED!"
    #         }
    # """"ENDPOINT TO ALLOW CREATIONS OF A TRIPS FOR THE FILE"""
    # @http.route('/new_file', type='json', auth='public', cors='*', method=['POST'])
    # def create_file(self, **kw):
    #     data = json.loads(request.httprequest.data)
    #     """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
    #     verrification = verrifyAuth.validator.verify_token(data['token'])
    #     if verrification['status']:
    #         """your code goes here"""
    #         pass
    #     else:
    #         return {
    #             "code":403,
    #             "status":"Failed",
    #             "Message":"NOT AUTHORISED!"
    #         }


    # """ENDPOINT TO ALLOW CREATION OF A NEW CUSTOMER"""
    # @http.route('/new_file', type='json', auth='public', cors='*', method=['POST'])
    # def create_file(self, **kw):
    #     data = json.loads(request.httprequest.data)
    #     """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
    #     verrification = verrifyAuth.validator.verify_token(data['token'])
    #     if verrification['status']:
    #         """your code goes here"""
    #         pass
    #     else:
    #         return {
    #             "code":403,
    #             "status":"Failed",
    #             "Message":"NOT AUTHORISED!"
    #         }
    
    # ACCOUNTING
    """ENDPOINT TO ALLOW CHARTS OF ACCOUNTS"""
    @http.route('/create_chart', type='json', auth='public', cors='*', method=['POST'])
    def new_charts(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['code']:
                return {
                    "code":400,
                    "message":"Code cannot be empty"
                }
            if  not data['name']:
                    return {
                        "code":400,
                        "message":"Name cannot be empty"
                    }
            if  not data['user_type_id']:
                    return {
                        "code":400,
                        "message":"Type cannot be empty"
                    }
            if  not data['currency_id']:
                    return {
                        "code":400,
                        "message":"Account Currency cannot be empty"
                    }
            if  not data['tax_ids']:
                    return {
                        "code":400,
                        "message":"Default Taxes cannot be empty"
                    }
            if  not data['deprecated']:
                    return {
                        "code":400,
                        "message":"Deprecated cannot be empty"
                    }
            if  not data['tag_ids']:
                    return {
                        "code":400,
                        "message":"Tags cannot be empty"
                    }
            if  not data['allowed_journal_ids']:
                    return {
                        "code":400,
                        "message":"Allowed Journal cannot be empty"
                    }

            charts = request.env["account.account"].sudo().create({
                 "code":data['code'],
                 "name":data['name'],
                 'user_type_id':data['user_type_id'],
                 'currency_id':data['currency_id'],
                 "tax_ids":data['tax_ids'],
                 'deprecated':data['deprecated'],
                 'tag_ids':data['tag_ids'],
                 'allowed_journal_ids':data['allowed_journal_ids'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if charts:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Chart of Account"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }


    