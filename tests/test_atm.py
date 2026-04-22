import pytest
import json
import sys
import os
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modified import load_data, save_data, ATM, DAILY_LIMIT

@pytest.fixture
def sample_data():
    data = {
        'testuser': {
            'pin': '1234',
            'balance': 1000.0,
            'transactions': [],
            'daily_withdraw': {}
        }
    }
    return data

def test_deposit(sample_data):
    data = sample_data.copy()
    atm = ATM('testuser', data)
    atm.deposit(500)
    assert data['testuser']['balance'] == 1500.0
    assert len(data['testuser']['transactions']) == 1
    assert data['testuser']['transactions'][0]['type'] == 'Deposit'

def test_withdraw_success(sample_data):
    data = sample_data.copy()
    atm = ATM('testuser', data)
    atm.withdraw(300)
    assert data['testuser']['balance'] == 700.0

def test_withdraw_insufficient(sample_data):
    data = sample_data.copy()
    atm = ATM('testuser', data)
    atm.withdraw(2000)
    assert data['testuser']['balance'] == 1000.0

def test_daily_limit(sample_data):
    data = sample_data.copy()
    data['testuser']['daily_withdraw'] = {'2024-10-01': 19000}  # Mock date
    atm = ATM('testuser', data)
    atm.withdraw(2000)
    assert data['testuser']['balance'] == 1000.0

def test_transfer(sample_data):
    data = sample_data.copy()
    data['receiver'] = {'pin': '5678', 'balance': 0.0, 'transactions': [], 'daily_withdraw': {}}
    atm = ATM('testuser', data)
    atm.transfer('receiver', 500)
    assert data['testuser']['balance'] == 500.0
    assert data['receiver']['balance'] == 500.0

print("ATM Tests ready - `pytest tests/test_atm.py -v` (run in venv with pytest installed)")
