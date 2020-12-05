import pytest
import requests

baseURL = 'http://127.0.0.1:5000/'

def test_getBovespa():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200

def test_getVale():
    response = requests.request('GET',baseURL+'VALE')
    assert response.status_code == 200

def test_getValueNotFound():
    response = requests.request('GET',baseURL+'123')
    assert response.status_code == 404