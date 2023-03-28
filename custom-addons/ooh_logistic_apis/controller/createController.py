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
    """"ENDPOINT TO VERRIFY LEGITIMATE OF ACCESS TOKEN ON LOCAL STORAGE"""
    @http.route('/validate_type_token', type='json', auth='public', cors='*', method=['POST'])
    def verrfiy_token(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            return {
                "code":200,
                "status":"fine",
                "Message":"EVERYTHING SEEMS FINE!"
            }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"THERE IS SUSPICIOUS ATTEMPTS TO ACCESS THE SYSTEM!!!!!!!!!!!!1"
            }


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


    """ENDPOINT TO ALLOW CREATION OF TAXES"""
    @http.route('/create_tax', type='json', auth='public', cors='*', method=['POST'])
    def new_tax(self, **kw):
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
            if  not data['type_tax_use']:
                    return {
                        "code":400,
                        "message":"Tax Type cannot be empty"
                    }
            if  not data['amount_type']:
                    return {
                        "code":400,
                        "message":"Tax Computation cannot be empty"
                    }
            if  not data['amount']:
                    return {
                        "code":400,
                        "message":"Amount cannot be empty"
                    }
            # if  not data['tax_scope']:
            #         return {
            #             "code":400,
            #             "message":"Tax Scope cannot be empty"
            #         }
            # if  not data['tax_group_id']:
            #         return {
            #             "code":400,
            #             "message":"Tax Group cannot be empty"
            #         }
            # if  not data['country_id']:
            #         return {
            #             "code":400,
            #             "message":"Country cannot be empty"
            #         }

            tax = request.env["account.tax"].sudo().create({
                 "name":data['name'],
                 'type_tax_use':data['type_tax_use'],
                 'amount_type':data['amount_type'],
                 "amount":data['amount'],
                #  'tax_scope':data['tax_scope'],
                #  'tax_group_id':data['tax_group_id'],
                #  'country_id':data['country_id'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if tax:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Tax"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }

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
                #  'created_by':verrification['id']
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
            
    """ENDPOINT TO ALLOW JOURNAL ENTRIES"""
    @http.route('/create_journalentry', type='json', auth='public', cors='*', method=['POST'])
    def new_journalentry(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['ref']:
                return {
                    "code":400,
                    "message":"Ref cannot be empty"
                }
            if  not data['name']:
                    return {
                        "code":400,
                        "message":"Name cannot be empty"
                    }
            if  not data['date']:
                    return {
                        "code":400,
                        "message":"Date cannot be empty"
                    }
            if  not data['journal_id']:
                    return {
                        "code":400,
                        "message":"Journal cannot be empty"
                    }
            

            journal_entry = request.env["account.move"].sudo().create({
                 "ref":data['ref'],
                 "name":data['name'],
                 'date':data['date'],
                 'journal_id':data['journal_id'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if journal_entry:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Journal Entry"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
            
    # FLEET
    """ENDPOINT TO CREATE SERVICE"""
    @http.route('/create_service', type='json', auth='public', cors='*', method=['POST'])
    def new_service(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['description']:
                return {
                    "code":400,
                    "message":"Description cannot be empty"
                }
            if  not data['vehicle_id']:
                    return {
                        "code":400,
                        "message":"Vehicle cannot be empty"
                    }
            if  not data['service_type_id']:
                    return {
                        "code":400,
                        "message":"Service Type cannot be empty"
                    }
            if  not data['purchaser_id']:
                    return {
                        "code":400,
                        "message":"Driver cannot be empty"
                    }
            if  not data['date']:
                    return {
                        "code":400,
                        "message":"Date cannot be empty"
                    }
            if  not data['vendor_id']:
                    return {
                        "code":400,
                        "message":"Vendor cannot be empty"
                    }
            if  not data['amount']:
                    return {
                        "code":400,
                        "message":"Cost cannot be empty"
                    }
            if  not data['odometer']:
                    return {
                        "code":400,
                        "message":"Odometer Value cannot be empty"
                    }
            

            service = request.env["fleet.vehicle.log.services"].sudo().create({
                 "description":data['description'],
                 "vehicle_id":data['vehicle_id'],
                 'service_type_id':data['service_type_id'],
                 'purchaser_id':data['purchaser_id'],
                 'date':data['date'],
                 'vendor_id':data['vendor_id'],
                 'date':data['date'],
                 'amount':data['amount'],
                 'odometer':verrification['odometer'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if service:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Service"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
            
    """ENDPOINT TO CREATE FLEET"""
    @http.route('/create_fleet', type='json', auth='public', cors='*', method=['POST'])
    def new_fleet(self, **kw):
        data = json.loads(request.httprequest.data)
        """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            """your code goes here"""
            if  not data['model_id']:
                return {
                    "code":400,
                    "message":"Model cannot be empty"
                }
            if  not data['license_plate']:
                    return {
                        "code":400,
                        "message":"License Plate cannot be empty"
                    }
            if  not data['driver_id']:
                    return {
                        "code":400,
                        "message":"Driver cannot be empty"
                    }
            if  not data['next_assignation_date']:
                    return {
                        "code":400,
                        "message":"Journal cannot be empty"
                    }
            

            fleet = request.env["fleet.vehicle"].sudo().create({
                 "model_id":data['model_id'],
                 "license_plate":data['license_plate'],
                 'driver_id':data['driver_id'],
                 'next_assignation_date':data['next_assignation_date'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if fleet:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Fleet"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
            
    """ENDPOINT TO CREATE MANUFACTURER"""
    @http.route('/create_manufacturer', type='json', auth='public', cors='*', method=['POST'])
    def new_manufacturer(self, **kw):
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

            manufacturer = request.env["fleet.vehicle.model.brand"].sudo().create({
                 "name":data['name'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if manufacturer:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Model"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
            
    """ENDPOINT TO CREATE VEHICLE MODEL"""
    @http.route('/create_model', type='json', auth='public', cors='*', method=['POST'])
    def new_model(self, **kw):
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
            if  not data['brand_id']:
                return {
                    "code":400,
                    "message":"Manufacturer cannot be empty"
                }
            if  not data['vehicle_type']:
                return {
                    "code":400,
                    "message":"Vehicle Type cannot be empty"
                }
            if  not data['category_id']:
                return {
                    "code":400,
                    "message":"Category cannot be empty"
                }

            manufacturer = request.env["fleet.vehicle.model"].sudo().create({
                 "name":data['name'],
                 "brand_id":data['name'],
                 "vehicle_type":data['vehicle_type'],
                 "category_id":data['category_id'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if manufacturer:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Manufacturer"
                 }
        else:
            return {
                "code":403,
                "status":"Failed",
                "Message":"NOT AUTHORISED!"
            }
            
    # EMPLOYEE
    """ENDPOINT TO CREATE EMPLOYEE"""
    @http.route('/create_employee', type='json', auth='public', cors='*', method=['POST'])
    def new_employee(self, **kw):
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
            if  not data['mobile_phone']:
                return {
                    "code":400,
                    "message":"Mobile cannot be empty"
                }
            if  not data['work_email']:
                return {
                    "code":400,
                    "message":"Email cannot be empty"
                }
            if  not data['department_id']:
                return {
                    "code":400,
                    "message":"Department cannot be empty"
                }

            employee = request.env["hr.employee"].sudo().create({
                 "name":data['name'],
                 "mobile_phone":data['mobile_phone'],
                 "work_email":data['work_email'],
                 "department_id":data['department_id'],
                 'company_id':verrification['company_id'][0],
                #  'created_by':verrification['user_id'][0]
            })
            if employee:
                 return {
                      "code":200,
                      "status":"Success",
                      "message":"Created Employee"
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
                'log_user_id':verrification['id'],
                'company_id':verrification['company_id'][0]
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
                'log_user_id':verrification['id'],
                'company_id':verrification['company_id'][0]
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
                'log_user_id':verrification['id'],
                'company_id':verrification['company_id'][0]
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
                'log_user_id':verrification['id'],
                'company_id':verrification['company_id'][0]

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
