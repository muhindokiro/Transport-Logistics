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

    