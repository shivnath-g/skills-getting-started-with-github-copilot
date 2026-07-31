from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.delete(
        "/activities/Chess%20Club/participants/michael%40mergington.edu"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"

    activities_response = client.get("/activities")
    activity = activities_response.json()["Chess Club"]
    assert "michael@mergington.edu" not in activity["participants"]


def test_unregister_participant_returns_404_for_unknown_participant():
    response = client.delete(
        "/activities/Chess%20Club/participants/unknown%40example.com"
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
