import requests
import pytest
from datetime import datetime
from test_data.event_data import API_URL, API_TOKEN, EVENT_ID_TO_UPDATE

@pytest.fixture
def event_id_to_update():
    return EVENT_ID_TO_UPDATE

def test_update_event_name(event_id_to_update):
    now = datetime.now().strftime("%d%m%H%M%S")
    updated_event_name = "Dance Revo 2025 - Updated - " + now
    payload = {
        "event": {
            "name": {"html": updated_event_name},
        }
    }
    response = requests.post(
        f"{API_URL}/events/{event_id_to_update}/?token={API_TOKEN}",
        json=payload
    )
    assert response.status_code == 200, f"Failed to update event {event_id_to_update}"
    get_response = requests.get(f"{API_URL}/events/{event_id_to_update}/?token={API_TOKEN}")
    event = get_response.json()
    assert event["name"]["text"] == updated_event_name

def test_update_event_description(event_id_to_update):
    now = datetime.now().strftime("%d%m%H%M%S")
    updated_event_description = "Get ready to groove at Dance Revo 2025 - Updated - " + now
    payload = {
        "event": {
            "description": {"html": updated_event_description}
        }
    }
    response = requests.post(
        f"{API_URL}/events/{event_id_to_update}/?token={API_TOKEN}",
        json=payload
    )
    assert response.status_code == 200, f"Failed to update event {event_id_to_update}"
    get_response = requests.get(f"{API_URL}/events/{event_id_to_update}/?token={API_TOKEN}")
    event = get_response.json()
    assert event["description"]["text"] == updated_event_description
