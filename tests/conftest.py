import pytest
from server import create_app, db


@pytest.fixture
def client():
    config_dict = {
        "SQLALCHEMY_DATABASE_URI": "postgresql://testusr:password@127.0.0.1:5432/testdb",
        "DEBUG": True,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config_dict)
    app.app_context().push()

    db.create_all()
    client = app.test_client()
    yield client
