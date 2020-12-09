import pytest
import requests

baseURL = 'http://127.0.0.1:5000/'

def test_getBovespa():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200

def test_getVale():
    response = requests.request('GET',baseURL+'VALE/5min')
    assert response.status_code == 200

def test_getValueNotFound():
    response = requests.request('GET',baseURL+'123/1min')
    assert response.status_code == 404

def test_getValueNotFoundBovespa():
    response = requests.request('GET',baseURL+'VALE/2min')
    assert response.status_code == 404
