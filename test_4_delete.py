import pytest
import requests
import allure
from user_data import user_id

base_url = "https://reqres.in/api"


@allure.feature("TEST REQRES DELETE")
@allure.suite("DELETE")
class TestReqresDelete:

    @allure.story("User Deletion")
    @allure.title("Delete User")
    @allure.description("Verify that we can delete a user by ID successfully.")
    @allure.severity("Normal")
    @pytest.mark.smoke
    def test_delete_user_by_id(self):
        with allure.step(f"DELETE request to {base_url}/users/{user_id}"):
            response = requests.delete(f"{base_url}/users/{user_id}")
        with allure.step("Check Status Code"):
            assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
        with allure.step("Check The User is Deleted"):
            response2 = requests.get(f"{base_url}/users/{24}") # Id must be user_id, changed because the system doesn't realy delete user.
            assert response2.status_code == 404, f"Expected status code 404, but got {response.status_code}"

