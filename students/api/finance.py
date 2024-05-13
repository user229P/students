import json
import urllib.request
import urllib.error
import requests
def register_student_to_finance_module(registrationID):
    try:
        url = 'http://localhost:8081/accounts/'
        data = json.dumps({"studentId": registrationID}).encode('utf-8')
        headers = {'Content-Type': 'application/json'}

        req = urllib.request.Request(url, data=data, headers=headers, method='POST')

        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                return True
            else:
                print(f"Failed to create finance account. Status code: {response.status}")
                return False

    except urllib.error.URLError as e:
        print(f"An error occurred: {e}")
        return False


def eligible_for_graduation(registrationID):
    url = f"http://localhost:8081/accounts/student/{registrationID}"
    
    try:
        req = urllib.request.Request(url)
        
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                account_info = json.loads(response.read().decode('utf-8'))
                if account_info.get('hasOutstandingBalance', False):
                    return False
                else:
                    return True
            else:
                return {'error': "Something Went Wrong!"}
    
    except urllib.error.URLError as e:
        return {'error': "Request not send. Start Finance Module"}