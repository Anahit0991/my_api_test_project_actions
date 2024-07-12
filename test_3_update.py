import pytest
import requests
import allure
import random


base_url = "https://reqres.in/api"

@allure.feature("TEST REQRES UPDATE")
@allure.suite("UPDATE")
class TestReqresUpdate():


    @allure.story("User Update")
    @allure.title("Put Update User")
    @allure.description("Verify that we can update a user's details successfully using PUT.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_put_update_user(self):
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        headers = {'Content-Type': 'application/json'}
        user_id = random.randint(1, 12)
        with allure.step(f"PUT request to {base_url}/users/{user_id}"):
            response = requests.put(
                f"{base_url}/users/{user_id}",
                json=data,
                headers=headers
            )
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check User's Name"):
            assert response.json()["name"] == data["name"]
        with allure.step("Check User's Job"):
            assert response.json()["job"] == data["job"]


    @allure.story("User Update")
    @allure.title("Patch Update User")
    @allure.description("Verify that we can partially update a user's details successfully using PATCH.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_patch_update_user(self):
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        headers = {'Content-Type': 'application/json'}
        user_id = random.randint(1, 12)
        with allure.step(f"PATCH request to {base_url}/users/{user_id}"):
            response = requests.patch(
                f"{base_url}/users/{user_id}",
                json=data,
                headers=headers
            )
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check User's Name"):
            assert response.json()["name"] == data["name"]
        with allure.step("Check User's Job"):
            assert response.json()["job"] == data["job"]


