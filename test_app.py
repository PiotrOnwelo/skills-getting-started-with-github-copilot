from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    activity_name = "Soccer Team"
    email = "teststudent@mergington.edu"
    activities[activity_name]["participants"] = []

    # Act
    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    delete_response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    # Assert
    assert signup_response.status_code == 200
    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert "Unregistered" in delete_response.json()["message"]
