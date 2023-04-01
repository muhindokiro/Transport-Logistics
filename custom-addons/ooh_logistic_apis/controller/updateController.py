import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class UpdateDetails(http.Controller):

    # ACCOUNTING
    
    # """"ENDPOINT TO ALLOW READING OF CHART OF ACCOUNTS""
    @http.route('/update_charts', type='json', auth='public', cors='*', method=['POST'])
    def update_charts(self,**kw):
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
                    "code":data['code'],
                    "name":data['name'],
                    "user_type_id":data['user_type_id'],
                    # "currency_id":data['currency_id'],
                    # "tax_ids":data['tax_ids'],
                    # "deprecated":data['deprecated'],
                    # "tax_ids":data['tax_ids'],
                    # "allowed_journal_ids":data['allowed_journal_ids'],
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
            
    # """"ENDPOINT TO ALLOW READING OF TAXES""
    @http.route('/update_tax', type='json', auth='public', cors='*', method=['POST'])
    def update_tax(self,**kw):
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
                    "name":data['name'],
                    'type_tax_use':data['type_tax_use'],
                    'amount_type':data['amount_type'],
                    'tax_scope':data['tax_scope'],
                    "amount":data['amount'],
                    # 'tax_scope':data['tax_scope'],
                    # 'tax_group_id':data['tax_group_id'],
                    # 'country_id':data['country_id'],
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
    
    # """"ENDPOINT TO ALLOW READING OF JOURNALS""
    @http.route('/update_journal', type='json', auth='public', cors='*', method=['POST'])
    def update_journal(self,**kw):
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
                    "name":data['name'],
                    'type':data['type'],
                    'code':data['code'],
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
            
    # """"ENDPOINT TO ALLOW READING OF JOURNAL ENTRY""
    @http.route('/update_journalentry', type='json', auth='public', cors='*', method=['POST'])
    def update_journalentry(self,**kw):
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
                    "ref":data['ref'],
                    "name":data['name'],
                    'date':data['date'],
                    'journal_id':data['journal_id'],
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
            
    # FLEET
    
    # """"ENDPOINT TO ALLOW READING OF SERVICE""
    @http.route('/update_service', type='json', auth='public', cors='*', method=['POST'])
    def update_service(self,**kw):
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
                "message": "You have successful updated your information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
            
    # """"ENDPOINT TO ALLOW READING OF VEHICLE""
    @http.route('/update_fleet', type='json', auth='public', cors='*', method=['POST'])
    def update_fleet(self,**kw):
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
                "message": "You have successful updated your information"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    # """"ENDPOINT TO ALLOW READING OF MANUFACTURER""
    @http.route('/update_manufacturer', type='json', auth='public', cors='*', method=['POST'])
    def update_manufacturer(self,**kw):
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
            
    # """"ENDPOINT TO ALLOW READING OF VEHICLE MODEL""
    @http.route('/update_model', type='json', auth='public', cors='*', method=['POST'])
    def update_model(self,**kw):
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
                    "name":data['name'],
                    "brand_id":data['name'],
                    "vehicle_type":data['vehicle_type'],
                    "category_id":data['category_id'],
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
            
    # EMPLOYEE
    
    # """"ENDPOINT TO ALLOW READING OF EMPLOYEE""
    @http.route('/update_employee', type='json', auth='public', cors='*', method=['POST'])
    def update_employee(self,**kw):
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
                    "name":data['name'],
                    "mobile_phone":data['mobile_phone'],
                    "employee_type":data['employee_type'],
                    "work_email":data['work_email'],
                    "department_id":data['department_id'],
                    "parent_id":data['parent_id'],
                    "country_id":data['country_id'],
                    "identification_id":data['identification_id'],
                    "passport_id":data['passport_id'],
                    "birthday":data['birthday'],
                    # "kra_number":data['kra_number'],
                    'company_id':verrification['company_id'][0],
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

    # """"ENDPOINT TO ALLOW READING OF SERVICE TYPE""
    @http.route('/update_service_type', type='json', auth='public', cors='*', method=['POST'])
    def update_employee(self,**kw):
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
                    "name":data['name'],
                    'category':data['category'],
                    'company_id':verrification['company_id'][0],
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

    # """"ENDPOINT TO ALLOW READING OF DEPARTMENTS""
    @http.route('/update_department', type='json', auth='public', cors='*', method=['POST'])
    def update_department(self,**kw):
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
                    "name":data['name'],
                    'manager_id':data['manager_id'],
                    'company_id':verrification['company_id'][0],
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

    # """"ENDPOINT TO ALLOW READING OF PRODUCT CATEGORY""
    @http.route('/update_category', type='json', auth='public', cors='*', method=['POST'])
    def update_category(self,**kw):
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
                    "name":data['name'],
                    'company_id':verrification['company_id'][0],
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

    # """"ENDPOINT TO ALLOW READING OF PRODUCT""
    @http.route('/update_product', type='json', auth='public', cors='*', method=['POST'])
    def update_product(self,**kw):
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
                    "name":data['name'],
                    "list_price":data['list_price'],
                    "categ_id":data['categ_id'],
                    "detailed_type":data['detailed_type'],
                    'company_id':verrification['company_id'][0],
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
    
    # TRIPS
    
    # """"ENDPOINT TO ALLOW READING OF TRIPS""
    @http.route('/update_trip', type='json', auth='public', cors='*', method=['POST'])
    def update_trip(self,**kw):
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
                    "internal_driver":data['internal_driver'],
                    'internal_truck':data['internal_truck'],
                    "internal_turnboy":data['internal_turnboy'],
                    "related_file":data['related_file'],
                    'departure_date':data['departure_date'],
                    'return_date':data['return_date'],
                    "type":data['type'],
                    'company_id':verrification['company_id'][0],
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
            
    # """"ENDPOINT TO ALLOW READING OF CUSTOMERS""
    @http.route('/update_customer', type='json', auth='public', cors='*', method=['POST'])
    def update_customer(self,**kw):
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
                    "company_type":data['company_type'],
                    'country_id':data['country_id'],
                    "city":data['city'],
                    "name":data['name'],
                    'phone':data['phone'],
                    'email':data['email'],
                    'property_account_receivable_id':data['property_account_receivable_id'],
                    'property_account_payable_id':data['property_account_payable_id'],
                    'company_id':verrification['company_id'][0],
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
            
    # """"ENDPOINT TO ALLOW READING OF FILES""
    @http.route('/update_file', type='json', auth='public', cors='*', method=['POST'])
    def update_file(self,**kw):
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
                    "bill_ref":data['bill_ref'],
                    # 'date':today,
                    'arr_date':data['arr_date'],
                    "dep_date":data['dep_date'],
                    'customer_id':data['customer_id'],
                    'journal_id':data['journal_id'],
                    "country_id":data['country_id'],
                    'return_date':data['return_date'],
                    'invoice_payment_term_id':data['invoice_payment_term_id'],
                    'company_id':verrification['company_id'][0],
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

    