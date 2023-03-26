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


    """ENDPOINT TO ALLOW CREATION OF JOURNALS"""
    @http.route('/create_journal', type='json', auth='public', cors='*', method=['POST'])
    def new_journal(self, **kw):
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
            if  not data['type']:
                    return {
                        "code":400,
                        "message":"Journal Type cannot be empty"
                    }
            if  not data['name']:
                    return {
                        "code":400,
                        "message":"Name cannot be empty"
                    }
            journal = request.env["account.journal"].sudo().create({
                 "name":data['name'],
                 'type':data['type'],
                 'code':data['code'],
                 'company_id':verrification['company_id'][0],
                 'created_by':verrification['user_id'][0]
            })
            if journal:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Journal"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }


    # """ENDPOINT TO ALLOW CREATION OF CHARTS OF ACCOUNT"""
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

    # """ENDPOINT TO ALLOW CREATION OF TAXES"""
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

    # """ENDPOINT TO ALLOW CREATION OF EMPLOYEES"""
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
    
    #     """ENDPOINT TO ALLOW CREATION OF JOB TITLE"""
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


    # """ENDPOINT TO ALLOW CREATION OF DEPARTMENTS"""
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
    
    #     """ENDPOINT TO ALLOW CREATION OF TRIP LINES"""
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
    
    #     """ENDPOINT TO ALLOW CREATION OF FILE RELATED DOCUMENTS"""
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