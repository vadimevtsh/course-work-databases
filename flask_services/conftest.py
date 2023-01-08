import os
import tempfile

# lib for tests
import pytest

# import the modules to test in here

"""read in SQL for populating test data"""
#with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
	#_data_sql = f.read().decode("utf8")

"""Creating and configuring a new app instance for each test"""
@pytest.fixture
def app():
	db_fd, db_path = tempfile.mkstemp()

	# create application in here
	#app = create_app({"TESTING": True, "DATABASE": db_path})

	with app.app_context():
		# initialize database
		# get database and execute script

	yield app

	# close and remove the temporary database
	os.close(db_fd)
	os.unlink(db_path)

"""A test runner for the app"""
@pytest.fixture
def client(app):
	return app.test_client()

""" A test runner for the app's Click commands."""
@pytest.fixture
def runner(app):
	return app.test_cli_runner()

# client init
class AuthActions(object):
	def __init__(self, client):
		self._client = client

# method for login
	def login(self, username="test", password="test"):
		return self._client.post("/auth/login", data={"username": username, "password": password})
	
# method for logout
	def logout(self):
		return self._client.get("/auth/logout")

# method for authentication
@pytest.fixture
def auth(client):
	return AuthActions(client)