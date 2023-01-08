import pytest

from flask import g
from flask import session

# import get application database

""" Testing that viewing the page renders without template errors"""
def test_register(client, app):
	assert client.get("/register").status_code == 200

	# testing that successful registration redirects to the login page
	response = client.post("/register", data={"username": "a", "password": "a"})
	assert "https://localhost/login" == response.headers["Location"]

	# testing that the user was inserted into the database

	#with app.app_context():
		#assert {
			# execute sql command ("SELECT * FROM USER WHERE username = 'a'")
		#}


@pytest.mark.parametrize(
	("username", "password", "message"),
	(
		("", "", b"Username is required."),
		("a", "", b"Password is required."),
		("test", "test", b"Already registered"),
		),
)

# method for checking validate input in register
def test_register_validate_input(client, username, password, message):
	response = client.post(
		"/register", data={"username": username, "password": password}
	)
	assert message in response.data

# method for testing login
def test_login(client, auth):
	# test whether viewing the page renders without any errors
	assert client.get("/login").status_code == 200

	# test whether successful login redirects to the index page
	response = auth.login()
	assert response.headers["Location"] == "https://localhost/"

	# check if the user id is set in the session
	# check if username is set in the session
	with client:
		client.get("/")
		assert session["user_id"] == 1
		assert g.user["username"] == "test"

@pytest.mark.parametrize(
	("username", "password", "message"),
	(("a", "test", b"Incorrect username."), ("test", "a", b"Incorrect password.")),
)

# method for checking validate input in login
def test_login_validate_input(auth, username, password, message):
	response = auth.login(username, password)
	assert message in response.data

# method for checking logout
def test_logout(client, auth):
	auth.login()

	with client:
		auth.logout()
		assert "user_id" not in session