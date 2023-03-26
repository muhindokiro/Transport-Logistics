import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class ReadValues(http.Controller):

    # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    @http.route('/account_types', type='json', auth='public', cors='*', method=['POST'])
    def get_account_types(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            types = request.env["account.account.type"].sudo().search(
                [('name', '!=', False)])
            [values.append({"name": x.name, "type": x.type, 'id': x.id})
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

    @http.route('/accounts', type='json', auth='public', cors='*', method=['POST'])
    def get_account(self, **kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            _logger.error(verrification['company_id'][0])
            obj = request.env["account.account"]
            items = len(obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])]))
            accounts = obj.sudo().search(
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({"name": x.name, "type": x.user_type_id,
                           'id': x.id, "code": x.code}) for x in accounts]
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({"name": x.name, "type": x.type,
                           'id': x.id, "code": x.code}) for x in journals]
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({"name": x.name, "type_tax_use": x.type_tax_use,
                           "amount": x.amount, 'id': x.id}) for x in taxes]
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "client": x.customer_id.name,
                "name": x.name,
                "bill_ref": x.bill_ref,
                "return_date": x.return_date,
                "arr_date": x.arr_date,
                "dep_date": x.dep_date,
                "inv_ref": x.inv_ref,
                "journal_name": x.journal_id.name,
                "country_id": x.country_id.name,
                "state": x.state,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "related_file": x.related_file.name,
                "partner_id": x.partner_id.name,
                "departure_date": x.departure_date,
                "return_date": x.return_date,
                "type": x.type,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "work_phone": x.work_phone,
                "work_email": x.work_email,
                "department_id": x.department_id.name,
                "job_title": x.job_title,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "company_type": x.company_type,
                "email": x.email,
                "phone": x.phone,
                "vat": x.vat,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            _logger.error(users)
            _logger.error(
                "THE SYSTEM USERS FOR THE USERS!!!!!!!!!!!!!!!!!!!!!11111")
            [values.append({
                "name": x.name,
                "email": x.email,
                "mobile": x.mobile,
                "state": x.state,
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
                'car', 'bike'])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "brand": x.brand_id.name,
                "model": x.name,
                "type": x.vehicle_type,
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
            manufacturers = obj.sudo().search([('name', '!=', False)],limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "model": x.model_id.name,
                "license_plate": x.license_plate,
                "model": x.driver_id.name,
                "net_car_value": x.net_car_value,
                "model_year": x.model_year,
                "fuel_type": x.fuel_type,
                "horsepower": x.horsepower,
                "odometer": x.odometer,
                'id': x.id
            }) for x in vehicles]
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "detailed_type": x.detailed_type,
                "list_price": x.list_price,
                "uom": x.uom_id.name,
                "sale_ok": x.sale_ok,
                "categ_id": x.categ_id.name,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "manager": x.manager_id.name,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                "employee_id": x.employee_id.name,
                "job_id": x.job_id.name,
                "date_start": x.date_start,
                "date_end": x.date_end,
                "salary_structure": x.structure_type_id.name,
                "state": x.state,
                "hr_responsible": x.hr_responsible_id.name,
                "contract_type_id": x.contract_type_id.name,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
                # "type_id": x.type_id.name,
                "country_id": x.country_id.name,
                "scheduled_pay": x.scheduled_pay,
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
                [('company_id.id', '=', verrification['company_id'][0])], limit=data['limit'], offset=data['offset'])
            [values.append({
                "name": x.name,
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
