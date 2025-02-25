import pytest
import requests
from selenium import webdriver

from constants import Constants
from route_user import APIUser
from test_data import TestData


@pytest.fixture()
def api_user():
    user = requests.post(f'{Constants.URL}/api/auth/register',data=TestData.new_user)
    access_token = user.json().get('accessToken')
    print(access_token)
    yield access_token
    cleaning = requests.delete(f'{Constants.URL}/api/auth/user', headers={'Authorization': f'{access_token}'})
    print(cleaning.text)

@pytest.fixture()
def api_user_and_order(data=TestData.new_user, ingr=TestData.ingr):
    user = requests.post(f'{Constants.URL}/api/auth/register', data)
    access_token = user.json().get('accessToken')
    print(access_token)
    order = requests.post(f'{Constants.URL}/api/orders', ingr, headers={'Authorization': f'{access_token}'})
    order_info = order.json()
    order_number = order_info['order']['number']
    print(order_number)


    yield access_token
    cleaning = requests.delete(f'{Constants.URL}/api/auth/user', headers={'Authorization': f'{access_token}'})
    print(cleaning.text)
    return order_number


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    #browser = webdriver.Firefox()
    yield browser
    browser.quit()

#@pytest.fixture(params=['chrome', 'firefox'])
#def driver(request):
#    if request.param == 'firefox':
#        browser = webdriver.Firefox()
#    elif request.param == 'chrome':
#        browser = webdriver.Chrome()
#    else:
#        raise ValueError('Unknown browser type')
#    yield browser
#    browser.quit()

