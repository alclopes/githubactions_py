from src.app import home, status


def test_home():
    assert home() == 'Hello'


def test_status():
    assert status() == 'ok'
