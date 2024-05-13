import urllib.request
import json

def register_student_to_library_account(registrationId):
    try:
        url = "http://localhost/api/register"
        payload = json.dumps({
            "studentId": registrationId
        }).encode('utf-8') 

        headers = {
            'Content-Type': 'application/json'
        }

        req = urllib.request.Request(url, data=payload, headers=headers, method='POST')

        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return True
            else:
                print(f"Failed to create library account. Status code: {response.status}")
                return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
