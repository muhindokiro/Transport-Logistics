import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class ReadValues(http.Controller):

    @http.route('/get_countries', type='json', auth='public', cors='*', method=['POST'])
    def get_countries(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            country = request.env["res.country"].sudo().search([('name', '!=', False),("name", 'ilike', data['name'])])
            [values.append({
            "name": x.name if x.name else "",
            'id': x.id
            })
                for x in country]
            return {
                "code": 200,
                "status": "success",
                "countries": values,
                "message": "All Countries"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    @http.route('/account_types', type='json', auth='public', cors='*', method=['POST'])
    def get_account_types(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            types = request.env["account.account.type"].sudo().search([('name', '!=', False),("name", 'ilike', data['name'])])
            [values.append({
            "name": x.name if x.name else "",
            "type": x.type if x.type else "",
            'id': x.id
            })
             for x in types]
            return {
                "code": 200,
                "status": "success",
                "account_types": values,
                "message": "All Account Types"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


        # """ENDPOINT TO GET ALL CHARTS OF ACCOUNT"""

    @http.route('/journal_items', type='json', auth='public', cors='*', method=['POST'])
    def get_journal_items(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["account.move.line"]
            items = len(obj.sudo().search([('company_id.id', '=', verrification['company_id'][0])]))
            journal_items = obj.sudo().search([('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "date": x.date if x.date else "",
                "name": x.move_name if x.move_name else "",
                "account":x.account_id.name if x.account_id.name else "",
                "partner":x.partner_id.name if x.partner_id.name else "",
                "debit":x.debit if x.debit else "",
                "credit":x.credit if x.credit else 0.00,
                'id': x.id,
                }) for x in journal_items]
            return {
                "code": 200,
                "status": "success",
                "journal_items": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/journal_entries', type='json', auth='public', cors='*', method=['POST'])
    def get_journal_entries(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["account.move"]
            items = len(obj.sudo().search([('company_id.id', '=', verrification['company_id'][0])]))
            journal_entries = obj.sudo().search([('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "date": x.date if x.date else "",
                "journal":x.journal_id.name if x.journal_id else "",
                "partner":x.partner_id.name if x.partner_id else "",
                "state":x.state,
                "amount": x.amount_total_signed,
                'id': x.id,
                }) for x in journal_entries]
            return {
                "code": 200,
                "status": "success",
                "journal_entries": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    # """ENDPOINT TO GET ALL CHARTS OF ACCOUNT"""
    @http.route('/accounts', type='json', auth='public', cors='*', method=['POST'])
    def get_account(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["account.account"]
            items = len(obj.sudo().search([('company_id.id', '=', verrification['company_id'][0])]))
            accounts = obj.sudo().search([("internal_type","ilike",data['type']),('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
            "name": x.name if x.name else "",
            "type": x.user_type_id.name if x.user_type_id else "",
            'id': x.id,
            "code": x.code if x.code else ""
            }) for x in accounts]
            return {
                "code": 200,
                "status": "success",
                "account": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/journals', type='json', auth='public', cors='*', method=['POST'])
    def get_journals(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["account.journal"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            journals = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
            "name": x.name if x.name else "",
            "type": x.type if x.type else "",
            'id': x.id,
            "code": x.code if x.code else ""
            }) for x in journals]
            return {
                "code": 200,
                "status": "success",
                "journals": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/taxes', type='json', auth='public', cors='*', method=['POST'])
    def get_taxes(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["account.tax"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            taxes = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
            "name": x.name if x.name else "",
            "type_tax_use": x.type_tax_use if x.type_tax_use else "",
            "amount": x.amount if x.amount else "",
            'id': x.id
            }) for x in taxes]
            return {
                "code": 200,
                "status": "success",
                "taxes": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/files', type='json', auth='public', cors='*', method=['POST'])
    def get_files(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["open.file"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            files = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "client": x.customer_id.name if x.customer_id else "",
                "name": x.name if x.name else "",
                "bill_ref": x.bill_ref if x.bill_ref else "",
                "return_date": x.return_date if x.return_date else "",
                "arr_date": x.arr_date if x.arr_date else "",
                "dep_date": x.dep_date if x.dep_date else "",
                "inv_ref": x.inv_ref if x.inv_ref else "",
                "journal_name": x.journal_id.name if x.journal_id else "",
                "country_id": x.country_id.name if x.country_id else "",
                "state": x.state if x.state else "",
                'id': x.id
            }) for x in files]
            return {
                "code": 200,
                "status": "success",
                "files": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/trips', type='json', auth='public', cors='*', method=['POST'])
    def get_trips(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["vehicle.trip"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            files = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "related_file": x.related_file.name if x.related_file else "",
                "partner_id": x.partner_id.name if x.partner_id else "",
                "departure_date": x.departure_date if x.departure_date else "",
                "return_date": x.return_date if x.return_date else "",
                "type": x.type if x.type else "",
                'id': x.id
            }) for x in files]
            return {
                "code": 200,
                "status": "success",
                "trips": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/employees', type='json', auth='public', cors='*', method=['POST'])
    def get_employees(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["hr.employee"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            employees = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "work_phone": x.work_phone if x.work_phone else "",
                "work_email": x.work_email if x.work_email else "",
                "department_id": x.department_id.name if x.department_id else "",
                "job_title": x.job_title if x.job_title else "",
                'id': x.id
            }) for x in employees]
            return {
                "code": 200,
                "status": "success",
                "employee": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/customers', type='json', auth='public', cors='*', method=['POST'])
    def get_customers(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["res.partner"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            customer = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "company_type": x.company_type,
                "email": x.email if x.email else "",
                "phone": x.phone if x.phone else "",
                "vat": x.vat if x.vat else "",
                'id': x.id
            }) for x in customer]
            return {
                "code": 200,
                "status": "success",
                "customers": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/users', type='json', auth='public', cors='*', method=['POST'])
    def get_users(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["logistic.users"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            users = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "email": x.email if x.email else "",
                "mobile": x.mobile if x.mobile else "",
                "state": x.state if x.state else "",
                'id': x.id
            }) for x in users]
            return {
                "code": 200,
                "status": "success",
                "users": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

        # """ENDPOINT TO GET ALL CHARTS OF ACCOUNT"""

    @http.route('/models', type='json', auth='public', cors='*', method=['POST'])
    def get_models(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["fleet.vehicle.model"]
            items = len(obj.sudo().search(
                [('vehicle_type', 'in', ['car', 'bike'])]))
            models = obj.sudo().search([('vehicle_type', 'in', [
                'car', 'bike']),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "brand": x.brand_id.name if x.brand_id else "",
                "model": x.name if x.name else "",
                "type": x.vehicle_type if x.vehicle_type else "",
                'id': x.id
            }) for x in models]
            return {
                "code": 200,
                "status": "success",
                "model": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/services', type='json', auth='public', cors='*', method=['POST'])
    def get_services(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["fleet.vehicle.log.services"]
            items = len(obj.sudo().search([('description', '!=', False),('company_id.id', '=', verrification['company_id'][0])]))
            services = obj.sudo().search([('company_id.id', '=', verrification['company_id'][0]),("description", 'ilike', data['name'])],limit=data['limit'], offset=data['offset'])
            [values.append({
                "vehicle": x.vehicle_id.license_plate if x.vehicle_id else "",
                "service": x.service_type_id.name if x.service_type_id else "",
                "date": x.date if x.date else "",
                "cost": x.amount if x.amount else "",
                "provider": x.vendor_id.name if x.vendor_id else "",
                "odometer": x.odometer if x.odometer else "",
                "driver": x.purchaser_id.name if x.purchaser_id else "",
                "state": x.state if x.state else "",
                'id': x.id
            }) for x in services]
            return {
                "code": 200,
                "status": "success",
                "service": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/service_types', type='json', auth='public', cors='*', method=['POST'])
    def get_service_types(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["fleet.service.type"]
            items = len(obj.sudo().search([('name', '!=', False),('company_id.id', '=', verrification['company_id'][0])]))
            manufacturers = obj.sudo().search([('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])],limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                  "categ": x.category if x.category else "",
                'id': x.id
            }) for x in manufacturers]
            return {
                "code": 200,
                "status": "success",
                "service_types": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/manufacture', type='json', auth='public', cors='*', method=['POST'])
    def get_manufacture(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["fleet.vehicle.model.brand"]
            items = len(obj.sudo().search([('name', '!=', False)]))
            manufacturers = obj.sudo().search([('name', '!=', False),("name", 'ilike', data['name'])],limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                'id': x.id
            }) for x in manufacturers]
            return {
                "code": 200,
                "status": "success",
                "manufacture": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/vehicles', type='json', auth='public', cors='*', method=['POST'])
    def get_vehicles(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["fleet.vehicle"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            vehicles = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "model": x.model_id.name if x.model_id else "",
                "license_plate": x.license_plate if x.license_plate else "",
                "driver": x.driver_employee_id.name if x.driver_employee_id else "",
                "net_car_value": x.net_car_value if x.net_car_value else "",
                "model_year": x.model_year if x.model_year else "",
                "fuel_type": x.fuel_type if x.fuel_type else "",
                "horsepower": x.horsepower if x.horsepower else "",
                "odometer": x.odometer if x.odometer else "",
                'id': x.id
            }) for x in vehicles]
            return {
                "code": 200,
                "status": "success",
                "vehicles": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/products', type='json', auth='public', cors='*', method=['POST'])
    def get_products(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["product.template"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            products = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "detailed_type": x.detailed_type if x.detailed_type else "",
                "list_price": x.list_price if x.list_price else "",
                "uom": x.uom_id.name if x.uom_id else "",
                "sale_ok": x.sale_ok if x.sale_ok else "",
                "categ_id": x.categ_id.name if x.categ_id else "",
                "categ": x.categ_id.id if x.categ_id else "",
                'id': x.id
            }) for x in products]
            return {
                "code": 200,
                "status": "success",
                "products": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/departments', type='json', auth='public', cors='*', method=['POST'])
    def get_departments(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["hr.department"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            departments = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "manager": x.manager_id.name if x.manager_id else "",
                "manager_id": x.manager_id.id if x.manager_id else "",
                'id': x.id
            }) for x in departments]
            return {
                "code": 200,
                "status": "success",
                "departments": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/contracts', type='json', auth='public', cors='*', method=['POST'])
    def get_contracts(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["hr.contract"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            contracts = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "employee_id": x.employee_id.name if x.employee_id else "",
                "job_id": x.job_id.name if x.job_id else "",
                "date_start": x.date_start if x.date_start else "",
                "date_end": x.date_end if x.date_end else "",
                "salary_structure": x.structure_type_id.name if x.structure_type_id else "",
                "state": x.state if x.state else "",
                "hr_responsible": x.hr_responsible_id.name if x.hr_responsible_id else "",
                "contract_type_id": x.contract_type_id.name if x.contract_type_id else "",
                'id': x.id
            }) for x in contracts]
            return {
                "code": 200,
                "status": "success",
                "contracts": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    @http.route('/structure', type='json', auth='public', cors='*', method=['POST'])
    def get_structure(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["hr.payroll.structure"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            structure = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                "code": x.code if x.code else "",
                'id': x.id
            }) for x in structure]
            return {
                "code": 200,
                "status": "success",
                "structure": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }


    @http.route('/category', type='json', auth='public', cors='*', method=['POST'])
    def get_category(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["product.category"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            category = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0]),("name", 'ilike', data['name'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name if x.name else "",
                'id': x.id
            }) for x in category]
            return {
                "code": 200,
                "status": "success",
                "category": values,
                "total_items": items,
                "items_per_page": data['limit']
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }

    # https://www.softaox.info/1000-angular-material-icons-list-mat-icon/
