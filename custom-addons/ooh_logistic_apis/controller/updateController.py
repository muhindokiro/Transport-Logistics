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
            user = request.env["logistic.users"].sudo().search([('name', '!=', False),("company_id.id","=",verrification['company_id'][0]),("id","=",data['user_id'])])
            if user:
                user.sudo().write({
                    "id":user.id,
                    "email":data['email'],
                    "state":data["state"],
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
        
    @http.route('/update_employee', type='json', auth='public', cors='*', method=['POST'])
    def update_employee(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            employee = request.env["hr.employee"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['employee_id'])])
            if employee:
                employee.sudo().write({
                   "name":data['name'],
                    "mobile_phone":data['mobile_phone'],
                    "employee_type":data['employee_type'],
                    "work_email":data['work_email'],
                    "department_id":data['department_id'],
                    "gender":data['gender'],
                    "parent_id":data['parent_id'],
                    "country_id":data['country_id'],
                    "identification_id":data['identification_id'],
                    "passport_id":data['passport_id'],
                    'kra':data['kra'],
                    'huduma':data['huduma'],
                    'nssf':data['nssf'],
                    'job_title':data['job_title'],
                    "birthday":data['birthday'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful updated empkoyee information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/update_service_type', type='json', auth='public', cors='*', method=['POST'])
    def update_service_type(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            service_type = request.env["fleet.service.type"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['type_id'])])
            if service_type:
                service_type.sudo().write({
                "name":data['name'],
                'category':data['category'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful service type"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_department', type='json', auth='public', cors='*', method=['POST'])
    def update_department(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            department = request.env["hr.department"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['department_id'])])
            if department:
                department.sudo().write({
                "name":data['name'],
                'manager_id':data['manager_id'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful service type"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_category', type='json', auth='public', cors='*', method=['POST'])
    def update_category(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            category = request.env["product.category"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['category_id'])])
            if category:
                category.sudo().write({
                "name":data['name'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful service type"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_product', type='json', auth='public', cors='*', method=['POST'])
    def update_product(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            product = request.env["product.template"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['product_id'])])
            if product:
                product.sudo().write({
                "name":data['name'],
                "list_price":data['list_price'],
                "categ_id":data['categ_id'],
                "detailed_type":data['detailed_type'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "You have successful service type"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_trip', type='json', auth='public', cors='*', method=['POST'])
    def update_trip(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            trip = request.env["vehicle.trip"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['trip_id'])])
            if trip:
                trip.sudo().write({
                 "external_driver":data['external_driver'],
                'external_truck':data['external_truck'],
                "external_turnboy":data['external_turnboy'],
                "related_file":data['related_file'],
                'departure_date':data['departure_date'],
                "type":data['type'],
                'return_date':data['return_date'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "update information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_file', type='json', auth='public', cors='*', method=['POST'])
    def update_file(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            file = request.env["open.file"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['file_id'])])
            if file:
                file.sudo().write({
                        "bill_ref":data['bill_ref'],
                        'arr_date':data['arr_date'],
                        "dep_date":data['dep_date'],
                        'customer_id':data['customer_id'],
                        'journal_id':data['journal_id'],
                        "country_id":data['country_id'],
                        'return_date':data['return_date'],
                        'invoice_payment_term_id':data['invoice_payment_term_id'],
                })
            return {
                "code": 200,
                "status": "success",
                "message": "update information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_model', type='json', auth='public', cors='*', method=['POST'])
    def update_model(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            model = request.env["fleet.vehicle.model"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['model_id'])])
            if model:
                model.sudo().write({
                 "name":data['name'],
                 "brand_id":data['name'],
                 "vehicle_type":data['vehicle_type'],
                 "category_id":data['category_id'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_manufacturer', type='json', auth='public', cors='*', method=['POST'])
    def update_manufacturer(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            manufacturer = request.env["fleet.vehicle.model.brand"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['manufacturer_id'])])
            if manufacturer:
                manufacturer.sudo().write({
                 "name":data['name']
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
    
    @http.route('/update_fleet', type='json', auth='public', cors='*', method=['POST'])
    def update_fleet(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            fleet = request.env["fleet.vehicle"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['fleet_id'])])
            if fleet:
                fleet.sudo().write({
                        "model_id":data['model_id'],
                        "license_plate":data['license_plate'],
                        'driver_id':data['driver_id'],
                        # 'next_assignation_date':data['next_assignation_date'],
                        "fuel_type":data['fuel_type'],
                        "license_plate":data['license_plate'],
                        'power':data['power'],
                        'horsepower':data['horsepower'],
                        "doors":data['doors'],
                        "seats":data['seats'],
                        "odometer":data['odometer'],
                        'color':data['color'],
                        'transmission':data['transmission'],
                        "model_year":data['model_year'],
                        'co2':data['co2'],
                        'co2_standard':data['co2_standard'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/update_service', type='json', auth='public', cors='*', method=['POST'])
    def update_service(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            service = request.env["fleet.vehicle.log.services"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['service_id'])])
            if service:
                service.sudo().write({
                    "description":data['description'],
                    "vehicle_id":data['vehicle_id'],
                    'service_type_id':data['service_type_id'],
                    'purchaser_id':data['purchaser_id'],
                    'date':data['date'],
                    'vendor_id':data['vendor_id'],
                    'date':data['date'],
                    'amount':data['amount'],
                    'odometer':data['odometer'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_journal', type='json', auth='public', cors='*', method=['POST'])
    def update_journal(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            journal = request.env["account.journals"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['journal_id'])])
            if journal:
                journal.sudo().write({
                        "name":data['name'],
                        'type':data['type'],
                        'code':data['code'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_tax', type='json', auth='public', cors='*', method=['POST'])
    def update_tax(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            tax = request.env["account.taxs"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['tax_id'])])
            if tax:
                tax.sudo().write({
                        "name":data['name'],
                        'type_tax_use':data['type_tax_use'],
                        'amount_type':data['amount_type'],
                        'tax_scope':data['tax_scope'],
                        "amount":data['amount'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
    @http.route('/update_account', type='json', auth='public', cors='*', method=['POST'])
    def update_account(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            account = request.env["account.account"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['account_id'])])
            if account:
                account.sudo().write({
                 "code":data['code'],
                 "name":data['name'],
                 'user_type_id':data['user_type_id'],
                })
                return {
                    "code": 200,
                    "status": "success",
                    "message": "update information"
                }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
