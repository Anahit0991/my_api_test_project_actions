import pytest
import requests
import allure
import user_data

base_url = "https://reqres.in/api"


@allure.feature("TEST REQRES POST")
@allure.suite("CREATE")
class TestReqresPost:

    @allure.story("User Creation")
    @allure.title("Create a User")
    @allure.description("Verify that we can create a new user successfully.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_create_user(self):
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step(f"POST request to {base_url}/users"):
            response = requests.post(
                f"{base_url}/users",
                json=data,
                headers=headers
            )
        with allure.step("Check Status Code"):
            assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        with allure.step("Check User's Name"):
            assert response.json()["name"] == data["name"]

        user_data.user_id = response.json()["id"]


@allure.feature("TEST REQRES POST")
@allure.suite("AUTHORIZATION")
class TestReqresAuthorization:

    @allure.story("User Registration")
    @allure.title("Register Successful")
    @allure.description("Verify that we can register a user successfully.")
    @allure.severity("Blocker")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_registration(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step(f"POST request to {base_url}/register"):
            response = requests.post(
                f"{base_url}/register",
                json=data,
                headers=headers)
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check Token"):
            assert "token" in response.json(), "Token hasn't been generated"

        user_data.token = response.json()["token"]

    @allure.story("User Registration")
    @allure.title("Register Unsuccessful")
    @allure.description("Verify that registering without a password returns an error.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_registration_without_password(self):
        data = {
            "email": "sydney@fife"
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step(f"POST request to {base_url}/register"):
            response = requests.post(
                f"{base_url}/register",
                json=data,
                headers=headers)
        with allure.step("Check Status Code"):
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        with allure.step("Check Error Message"):
            assert "error" in response.json(), "Account registered without password"

    @allure.story("User Login")
    @allure.title("Login Successful")
    @allure.description("Verify that we can log in a user successfully.")
    @allure.severity("Blocker")
    @pytest.mark.smoke
    def test_login(self):
        data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka",
            "token": user_data.token
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step(f"POST request to {base_url}/login"):
            response = requests.post(
                f"{base_url}/login",
                json=data,
                headers=headers)
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check Token"):
            assert "token" in response.json(), "Token hasn't been generated"

    @allure.story("User Login")
    @allure.title("Login Unsuccessful")
    @allure.description("Verify that logging in without a password returns an error.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_login_without_password(self):
        data = {
            "email": "peter@klaven"
        }
        headers = {'Content-Type': 'application/json'}
        with allure.step(f"POST request to {base_url}/login"):
            response = requests.post(
                f"{base_url}/login",
                json=data,
                headers=headers)
        with allure.step("Check Status Code"):
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        with allure.step("Check Error Message"):
            assert "error" in response.json(), "Account registered without password"


