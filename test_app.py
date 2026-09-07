from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Soccer Team"
    email = "teststudent@mergington.edu"
    activities[activity_name]["participants"] = []

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert delete_response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert "Unregistered" in delete_response.json()["message"]
