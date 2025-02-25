import requests
from constants import Constants


class APIUser:
    def create_user(data):
        return requests.post(f'{Constants.URL}/api/auth/register',data=data)
        #access_token = user.json().get('accessToken')


    def delete_user(tok):
        return requests.delete(f'{Constants.URL}/api/auth/user', headers={'Authorization': f'{tok}'})

    def clean_user(tok):
        result = APIUser.delete_user(tok)
        print(result.text)

