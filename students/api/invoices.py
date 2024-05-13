import json
import urllib.request
import requests
import urllib.error
from datetime import datetime, timedelta
def get_date():
    return (datetime.now().date() + timedelta(days=5)).strftime("%Y-%m-%d")


def new_invoice(amount, invoice_type, student_id):
    json_data = {
        "amount": amount,
        "dueDate": get_date(),
        "type": invoice_type,
        "account": {
            "studentId": student_id
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post("http://localhost:8081/invoices/", json=json_data, headers=headers)
        if response.status_code == 201:
            invoice_data = response.json()
            return {
                "invoice_created": True,
                "invoice_reference": invoice_data.get('reference', None)
            }
        elif response.status_code == 422:
            return {
                "invoice_created": False,
                "invalid_student": True
            }
        else:
            return {
                "invoice_created": False,
            }
    except requests.RequestException as e:
        return {
            "invoice_created": False,
        }


def delete_invoice(invoice_reference):
    url = f"http://localhost:8081/invoices/{invoice_reference}/cancel"

    try:
        req = urllib.request.Request(url, method='DELETE')

        with urllib.request.urlopen(req) as response:
            status_code = response.status

            if status_code == 200:
                return {'status': 200, 'message': 'Your Invoice is Cancelled'}
            elif status_code == 405:
                return {'status': 405, 'message': "Invoice is already paid."}
            elif status_code == 404:
                return {'status': 404, 'message': "Invoice not found"}
            elif status_code == 400:
                return {'status': 400, 'message': "Something Went Wrong. Start the finance module"}
    
    except urllib.error.URLError as e:
        return {'status': 400, "message": "Something Went Wrong. Please Start Finance Module."}


def fetch_all_invoices(user_id):
    url = f"http://localhost:8081/invoices"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            all_invoices = response.json()
            invoices = [invoice for invoice in all_invoices.get("_embedded", {}).get("invoiceList", []) if invoice.get("studentId") == user_id]
            return invoices
        else:
            print(f"Failed to retrieve invoices. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
