import json
from .. import verrifyAuth
from odoo import http
from odoo.http import request

import logging
import string

_logger = logging.getLogger(__name__)


class ValuesDetails(http.Controller):
    @http.route('/get_batch_details', type='json', auth='public', cors='*', method=['POST'])
    def get_batch_details(self, **kw):
        values = {}
        batchValues=[]
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            obj = request.env["hr.payslip"]
            items = len(obj.sudo().search([('company_id.id', '=', verrification['company_id'][0])]))
            batch = request.env["hr.payslip.run"].sudo().search([('company_id.id', '=', verrification['company_id'][0]),("id", '=', data['batch_id'])])
            if batch:
                values={
                    "name":batch.name,
                    "date_from":batch.date_start,
                    "date_to":batch.date_end,
                    "status":batch.state
                }
            # payslips = batch.slip_ids.search([("name","ilike",data["name"]),('company_id.id', '=', verrification['company_id'][0])],limit=data['limit'], offset=data['offset'])
            for res in batch.slip_ids:
                batchValues.append({
                    "employee":res.employee_id.name,
                    "basic":res.line_ids[0].total,
                    "gross":res.line_ids[1].total,
                    "net":res.line_ids[2].total,
                    "status":res.state
                })
                # for rec in res.line_ids:
                #         batchValues.update({rec.category_id.name:rec.total})
            return {
                "code": 200,
                "status": "success",
                "batch": values,
                "batchValues":batchValues,
                "total_items": items,
                "items_per_page": data['limit'],
                "message": "Payrol Batches"
            }
        else:
            return {
                "code": 403,
                "status": "Failed",
                "Message": "NOT AUTHORISED!"
            }
        
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
                "hr_responsible_id":contract.hr_responsible_id.name,
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
    
    @http.route('/customer_details', type='json', auth='public', cors='*', method=['POST'])
    def get_customer_details(self,**kw):
        files = []
        invoices=[]
        bills=[]
        trips=[]
        bills=[]
        data = json.loads(request.httprequest.data)
        # """verrification of the token passed to the payload to make sure its valid!!!!!!!!!"""
        verrification = verrifyAuth.validator.verify_token(data['token'])
        if verrification['status']:
            # """get all account types"""
            customer = request.env["res.partner"].sudo().search([("company_id.id","=",verrification['company_id'][0]),("id","=",data['customer_id'])])
            cust_details={
                "name":customer.name if customer.name else "",
                "email":customer.email if customer.email else "",
                "mobile":customer.phone if customer.phone else "",
                "country_id":customer.country_id.id if customer.country_id else "",
                "receivable_id":customer.property_account_receivable_id.id if customer.property_account_receivable_id else "",
                "payable_id":customer.property_account_payable_id.id if customer.property_account_payable_id else "",
                "city":customer.city if customer.city else "",
                "vat":customer.vat if customer.vat else "",
                "country":customer.country_id.name if customer.country_id else "",
                "type":customer.company_type if customer.company_type else "",
            }
            [files.append({
            "name": x.name if x.name else "",
            "bill_ref": x.bill_ref if x.bill_ref else "",
            "inv_ref": x.inv_ref if x.inv_ref else "",
            "return_date": x.return_date if x.return_date else "",
            "country": x.country_id.id if x.country_id else "",
            "arr_date": x.arr_date if x.arr_date else "",
            "state":x.state,
            'id': x.id
            })for x in request.env["open.file"].sudo().search([("customer_id.id","=",customer.id)])]
            [invoices.append({
            "name": x.name if x.name else "",
            "date": x.invoice_date if x.invoice_date else "",
            "due_date": x.invoice_payment_term_id.name if x.invoice_payment_term_id else "",
            "paid": x.amount_paid	 if x.amount_paid	 else "",
            "due_amount": x.amount_residual if x.amount_residual else "",
            "invoice_total": x.amount_total if x.amount_total else "",
            'id': x.id
            })for x in request.env["account.move"].sudo().search([("partner_id.id","=",customer.id),("move_type","=","out_invoice")])]
            [bills.append({
            "name": x.name if x.name else "",
            "date": x.invoice_date if x.invoice_date else "",
            "due_date": x.invoice_payment_term_id.name if x.invoice_payment_term_id else "",
            "paid": x.amount_paid	 if x.amount_paid	 else "",
            "due_amount": x.amount_residual if x.amount_residual else "",
            "invoice_total": x.amount_total if x.amount_total else "",
            'id': x.id
            })for x in request.env["account.move"].sudo().search([("partner_id.id","=",customer.id),("move_type","=","in_invoice")])]
            [trips.append({
            "name": x.name if x.name else "",
            "date": x.invoice_date if x.invoice_date else "",
            "customer": x.partner_id.name if x.partner_id else "",
            "departure": x.departure_date	 if x.departure_date	 else "",
            "return": x.return_date if x.return_date else "",
            "type": x.type if x.type else "",
            "car":x.license_plate if x.type=="internal" else x.external_truck,
            "driver":x.internal_driver.name if x.type=="internal" else x.external_driver,
            'id': x.id
            })for x in request.env["vehicle.trip"].sudo().search([("partner_id.id","=",customer.id)])]
            return {
                "code": 200,
                "status": "success",
                "information":cust_details,
                "invoices":invoices,
                "bills":bills,
                "files":files,
                "trips":trips,
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
        if verrification['status']:
            # """get all account types"""
            types = request.env["logistic.users"].sudo().search([('name', '!=', False),("company_id.id","=",verrification['company_id'][0]),("id","=",verrification['id'])])
            [values.append({
            "name": x.name if x.name else "",
            "login": x.email if x.email else "",
            "mobile": x.mobile if x.mobile else "",
            "state": x.state if x.state else "",
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
