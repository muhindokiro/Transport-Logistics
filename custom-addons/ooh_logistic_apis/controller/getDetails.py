import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class ValuesDetails(http.Controller):
    @http.route('/contract_details', type='json', auth='public', cors='*', method=['POST'])
    def get_contract_details(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            contract = request.env["hr.contract"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['contract_id'])])
            contract_details={
                "name":contract.name,
                "employee_name":contract.employee_id.name,
                "employee_email":contract.employee_id.work_email,
                "employee_phone":contract.employee_id.work_phone,
                "country":contract.employee_id.country_id.name,
                "start":contract.date_start,
                "end":contract.date_end,
                "struct":contract.struct_id.name,
                "hra":contract.hra,
                "sacco_loan":contract.sacco_loan,
                "sacco_saving":contract.sacco_saving,
                "bank_loan":contract.bank_loan,
                "travel_allowance":contract.travel_allowance,
                "medical_allowance":contract.medical_allowance,
                "other_allowance":contract.other_allowance,
                "wage":contract.wage,
                "state":contract.state
            }
            return {
                "code": 200,
                "status": "success",
                "information":contract_details,
                "message": "My Details"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        # """"ENDPOINT TO ALLOW READING OF JOURNl TYPES"""
    
    @http.route('/structure_details', type='json', auth='public', cors='*', method=['POST'])
    def get_structure_details(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            struct = request.env["hr.payroll.structure"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['structure_id'])])
            struct_details={
                "name":struct.name,
                "ref":struct.code,
                # "mobile":struct.work_phone,
            }
            [values.append({
            "name": x.name if x.name else "",
            "code": x.code if x.code else "",
            "category_id": x.category_id.name if x.category_id else "",
            'id': x.id
            })
             for x in struct.rule_ids]
            return {
                "code": 200,
                "status": "success",
                "rules": values,
                "information":struct_details,
                "message": "My Details"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
    
    @http.route('/employee_details', type='json', auth='public', cors='*', method=['POST'])
    def get_employee_details(self,**kw):
        values = []
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            employee = request.env["hr.employee"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['employee_id'])])
            emp_details={
                "name":employee.name,
                "email":employee.work_email,
                "mobile":employee.work_phone,
                "department":employee.department_id.name,
                "manager":employee.parent_id.name,
                "country":employee.country_id.name,
                "gender":employee.gender,
                "marital":employee.marital,
                "dob":employee.birthday,
                "kra":employee.kra,
                "huduma":employee.huduma,
                "nhif":employee.nhif,
                "nssf":employee.nssf,
                "title":employee.job_title,
                "national_id":employee.identification_id,
                "passsport":employee.passport_id,
                "type":employee.employee_type
            }
            return {
                "code": 200,
                "status": "success",
                "information":emp_details,
                "message": "My Details"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
    
    
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
