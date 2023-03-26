import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request
from datetime import datetime

# today = datetime.date.today()
import logging
import string

_logger = logging.getLogger(__name__)
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
                'user_id':verrification['user_id'][0]
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

    """ENDPOINT TO ALLOW CREATION DEPARTMENTS"""
    @http.route('/department', type='json', auth='public', cors='*', method=['POST'])
    def create_department(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['name']:
                return {
                    "code":400,
                    "message":"Name cannot be empty"
                }
            if  not data['manager_id']:
                    return {
                        "code":400,
                        "message":"Manager cannot be empty"
                    }
            department = request.env["hr.department"].sudo().create({
                "name":data['name'],
                'manager_id':data['manager_id'],
                'log_user_id':verrification['id']
            })
            if department:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created a department"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }

    """ENDPOINT TO ALLOW CREATION PRODUCT CATEGORY"""
    @http.route('/new_category', type='json', auth='public', cors='*', method=['POST'])
    def create_category(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['name']:
                return {
                    "code":400,
                    "message":"Name cannot be empty"
                }
            category = request.env["product.category"].sudo().create({
                "name":data['name'],
                'log_user_id':verrification['id']
            })
            if category:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created a Category"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }

    """ENDPOINT TO ALLOW CREATION OF PRODUCTS"""
    @http.route('/new_product', type='json', auth='public', cors='*', method=['POST'])
    def create_product(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['name']:
                return {
                    "code":400,
                    "message":"Name cannot be empty"
                }
            if  not data['list_price']:
                return {
                    "code":400,
                    "message":"Price cannot be empty"
                }
            if  not data['categ_id']:
                return {
                    "code":400,
                    "message":"Category cannot be empty"
                }
            if  not data['detailed_type']:
                return {
                    "code":400,
                    "message":"Type cannot be empty"
                }
            category = request.env["product.template"].sudo().create({
                "name":data['name'],
                "list_price":data['list_price'],
                "categ_id":data['categ_id'],
                 "detailed_type":data['detailed_type'],
                'log_user_id':verrification['id']
            })
            if category:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created a product"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
    
    """ENDPOINT TO ALLOW CREATION OF TRIPS"""
    @http.route('/new_trip', type='json', auth='public', cors='*', method=['POST'])
    def create_trip(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            if data['type']=="internal":
                """your code goes here"""
                if  not data['internal_driver']:
                    return {
                        "code":400,
                        "message":"Driver cannot be empty"
                    }
                if  not data['internal_truck']:
                        return {
                            "code":400,
                            "message":"Truck cannot be empty"
                        }
                if  not data['internal_turnboy']:
                        return {
                            "code":400,
                            "message":"Driver Assistant cannot be empty"
                        }
                if  not data['related_file']:
                    return {
                    "code":400,
                    "message":"Related File cannot be empty"
                    }
                if  not data['departure_date']:
                    return {
                    "code":400,
                    "message":"Departure Date cannot be empty"
                    }
                if  not data['return_date']:
                    return {
                    "code":400,
                    "message":"Expected Return cannot be empty"
                    }
                if  not data['departure_date']:
                     return {
                          "code":200,
                          "message":"Type Cannot be empty"
                     }
                trip = request.env["vehicle.trip"].sudo().create({
                "internal_driver":data['internal_driver'],
                'internal_truck':data['internal_truck'],
                "internal_turnboy":data['internal_turnboy'],
                "related_file":data['related_file'],
                'departure_date':data['departure_date'],
                'return_date':data['return_date'],
                "type":data['type'],
                'log_user_id':verrification['id']
            })
                if trip:
                    return {
                        "code":200,
                        "status":"Success",
                        "message":"You have successful created internal trip"
                    }
            if data['type']=="external":
                """your code goes here"""
                if  not data['external_driver']:
                    return {
                        "code":400,
                        "message":"Driver cannot be empty"
                    }
                if  not data['external_truck']:
                        return {
                            "code":400,
                            "message":"Truck cannot be empty"
                        }
                if  not data['external_turnboy']:
                        return {
                            "code":400,
                            "message":"Driver Assistant cannot be empty"
                        }
                if  not data['related_file']:
                    return {
                    "code":400,
                    "message":"Related File cannot be empty"
                    }
                if  not data['departure_date']:
                    return {
                    "code":400,
                    "message":"Departure Date cannot be empty"
                    }
                if  not data['return_date']:
                    return {
                    "code":400,
                    "message":"Expected Return cannot be empty"
                    }
            trip = request.env["vehicle.trip"].sudo().create({
                "external_driver":data['external_driver'],
                'external_truck':data['external_truck'],
                "external_turnboy":data['external_turnboy'],
                "related_file":data['related_file'],
                'departure_date':data['departure_date'],
                "type":data['type'],
                'return_date':data['return_date'],
                'log_user_id':verrification['id']
            })
            if trip:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"You have successful opened a trip"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
    
    """ENDPOINT TO ALLOW CREATION OF CUSTOMERS"""
    @http.route('/new_customer', type='json', auth='public', cors='*', method=['POST'])
    def new_customer(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['company_type']:
                return {
                    "code":400,
                    "message":"Type cannot be empty"
                }
            if  not data['country_id']:
                    return {
                        "code":400,
                        "message":"Country cannot be empty"
                    }
            if  not data['city']:
                    return {
                        "code":400,
                        "message":"City cannot be empty"
                    }
            if  not data['phone']:
                return {
                "code":400,
                "message":"Phone cannot be empty"
                }
            if  not data['email']:
                return {
                "code":400,
                "message":"Email cannot be empty"
                }
            if  not data['property_account_receivable_id']:
                return {
                "code":400,
                "message":"Account Receivable cannot be empty"
                }
            if  not data['property_account_payable_id']:
                return {
                "code":400,
                "message":"Account Payable cannot be empty"
                }
            file = request.env["res.partner"].sudo().create({
                "company_type":data['company_type'],
                'country_id':data['country_id'],
                "city":data['city'],
                "name":data['name'],
                'phone':data['phone'],
                'email':data['email'],
                'property_account_receivable_id':data['property_account_receivable_id'],
                'property_account_payable_id':data['property_account_payable_id'],
                'log_user_id':verrification['id']
            })
            if file:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"You have successful opened a file"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
    
    """ENDPOINT TO ALLOW CREATION OF FILE OPENNING"""
    @http.route('/new_file', type='json', auth='public', cors='*', method=['POST'])
    def create_file(self, **kw):
        data = json.loads(request.httprequest.data)

        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['customer_id']:
                return {
                    "code":400,
                    "message":"Code cannot be empty"
                }
            if  not data['bill_ref']:
                    return {
                        "code":400,
                        "message":"Bill of Lading cannot be empty"
                    }
            if  not data['arr_date']:
                    return {
                        "code":400,
                        "message":"Arrival Date cannot be empty"
                    }
            if  not data['dep_date']:
                return {
                "code":400,
                "message":"Departure Date cannot be empty"
                }
            if  not data['journal_id']:
                return {
                "code":400,
                "message":"Payment Journal cannot be empty"
                }
            if  not data['country_id']:
                return {
                "code":400,
                "message":"Country cannot be empty"
                }
            if  not data['return_date']:
                return {
                "code":400,
                "message":"Container Return Date cannot be empty"
                }
            if  not data['invoice_payment_term_id']:
                return {
                "code":400,
                "message":"Payment Term cannot be empty"
                }
            file = request.env["open.file"].sudo().create({
                "bill_ref":data['bill_ref'],
                # 'date':today,
                'arr_date':data['arr_date'],
                "dep_date":data['dep_date'],
                'customer_id':data['customer_id'],
                'journal_id':data['journal_id'],
                "country_id":data['country_id'],
                'return_date':data['return_date'],
                'invoice_payment_term_id':data['invoice_payment_term_id'],
                'log_user_id':verrification['id']
            })
            if file:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"You have successful opened a file"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }