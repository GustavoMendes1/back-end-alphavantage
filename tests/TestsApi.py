import pytest
import requests
import re

baseURL = 'http://127.0.0.1:5000/'

#Testing status code
def test_getBovespaSuccessfully():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200

def test_getCompanySuccessfully():
    response = requests.request('GET',baseURL+'VALE/5min')
    assert response.status_code == 200

def test_getCompanyNotFound():
    response = requests.request('GET',baseURL+'123/1min')
    assert response.status_code == 404

def test_getValueNotFoundBovespa():
    response = requests.request('GET',baseURL+'VALE/2min')
    assert response.status_code == 404

#Testing keys of json 
def test_fieldsCompany():
    response = requests.request('GET',baseURL+'VALE/1min')
    assert response.status_code == 200
    data = response.json()
    data['data'][0]['dateTime']
    data['data'][0]['points']
    
def test_fieldsBovespa():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200
    data = response.json()
    data['data'][0]['dateTime']
    data['data'][0]['points']

#Testing format response
def test_dateTimeFormatBovespa():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200
    data = response.json()
    dateTime = data['data'][0]['dateTime']
    regex = re.findall("[0-9]{2}/[0-9]{2}", dateTime)
    assert len(regex) == 1
     
def test_dateTimeFormatCompany():
    response = requests.request('GET',baseURL+'IBM/5min')
    assert response.status_code == 200
    data = response.json()
    dateTime = data['data'][0]['dateTime']
    regex = re.findall("[0-9]{2}:[0-9]{2} [0-9]{2}/[0-9]{2}", dateTime)
    assert len(regex) == 1

def test_pointsNotNullCompany():
    response = requests.request('GET',baseURL+'IBM/15min')
    assert response.status_code == 200
    data = response.json()
    points = data['data'][0]['points']
    assert points is not None

def test_pointsNotNullBovespa():
    response = requests.request('GET',baseURL)
    assert response.status_code == 200
    data = response.json()
    points = data['data'][0]['points']
    assert points is not None