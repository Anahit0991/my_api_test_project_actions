import pytest
import requests
import allure
import random


base_url = "https://reqres.in/api"

@allure.feature("TEST REQRES GET")
@allure.suite("GET")
class TestReqresGet():


    @allure.story("Get Users")
    @allure.title("Get Users List")
    @allure.description("Verify that we can retrieve a list of users successfully.")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_get_users_per_page(self):
        page = random.randint(1, 2)
        with allure.step(f"GET request to {base_url}/users?page={page}"):
            response = requests.get(f"{base_url}/users?page={page}")
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check the page number"):
            assert response.json()["page"] == page
        with allure.step("Check Users' quantity per page"):
            assert len(response.json()["data"]) == 6


    @allure.story("Get User Details")
    @allure.title("Get Single User")
    @allure.description("Verify that we can retrieve a single user by ID.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_user_by_id(self):
        user_id = random.randint(1, 12)
        with allure.step(f"GET request to {base_url}/users/{user_id}"):
            response = requests.get(f"{base_url}/users/{user_id}")
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check User's Id"):
            assert response.json()["data"]["id"] == user_id


    @allure.story("Get User Details")
    @allure.title("Get Single User Not Found")
    @allure.description("Verify that requesting a non-existing user returns a 404 status.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_get_user_negative(self):
        user_id = random.randint(13, 100)
        with allure.step(f"GET request to {base_url}/users/{user_id}"):
            response = requests.get(f"{base_url}/users/{user_id}")
        with allure.step("Check Status Code"):
            assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        with allure.step("Check No Data was Found"):
            assert len(response.json()) == 0


    @allure.story("Get Resource List")
    @allure.title("Get List Resource")
    @allure.description("Verify that we can retrieve a list of resources successfully.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_get_resources(self):
        with allure.step(f"GET request to {base_url}/unknown"):
            response = requests.get(f"{base_url}/unknown")
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check Users' quantity per page"):
            assert len(response.json()["data"]) == 6


    @allure.story("Get Resource Details")
    @allure.title("Get Single Resource")
    @allure.description("Verify that we can retrieve a single resource by ID.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_get_resource_by_id(self):
        resource_id = random.randint(1, 12)
        with allure.step(f"GET request to {base_url}/unknown/{resource_id}"):
            response = requests.get(f"{base_url}/unknown/{resource_id}")
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        with allure.step("Check Resource's Id"):
            assert response.json()["data"]["id"] == resource_id


    @allure.story("Get Resource Details")
    @allure.title("Get Single Resource Not Found")
    @allure.description("Verify that requesting a non-existing resource returns a 404 status.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_get_resource_negative(self):
        resource_id = random.randint(13, 100)
        with allure.step(f"GET request to {base_url}/unknown/{resource_id}"):
            response = requests.get(f"{base_url}/unknown/{resource_id}")
        with allure.step("Check Status Code"):
            assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
        with allure.step("Check No Data was Found"):
            assert len(response.json()) == 0


@allure.feature("TEST REQRES GET")
@allure.suite("GET DELAYED RESPONSE")
class TestReqresDelayedResponse():


    @allure.story("Delayed Response")
    @allure.title("Delayed Response")
    @allure.description("Verify that we can retrieve users with a delay.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_delayed_response(self):
        time = random.randint(1, 6)
        with allure.step(f"GET request to {base_url}/users?delay={time}"):
            response = requests.get(f"{base_url}/users?delay={time}")
        with allure.step("Check Status Code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

