import pytest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import create_app
from server.models import db

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def runworker():
    app.run(debug=False)


@manager.command
def test():
    pytest.main(["tests"])


@manager.command
def recreate_db():
    """
    Recreates a local database. Do not use in prod
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
