import pytest

@pytest.fixture(scope='module')
def client():
    from app.app import app
    app.TESTING = True
    return app.test_client()