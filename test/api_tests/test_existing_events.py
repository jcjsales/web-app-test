import requests
import pytest
from test_data.event_data import API_URL, API_TOKEN, EVENT_IDS, EXPECTED_DATA

@pytest.fixture(params=EVENT_IDS)
def event_data(request):
    event_id = request.param
    response = requests.get(API_URL + "/events/" + event_id + "/?token=" + API_TOKEN)
    assert response.status_code == 200, f"Event {event_id} not found: {response.status_code}"
    return event_id, response.json()

def test_event_name(event_data):
    event_id, data = event_data
    expected_name = EXPECTED_DATA[event_id]["name"]
    assert data["name"]["text"] == expected_name, f"Event {event_id} name mismatch"

def test_event_description(event_data):
    event_id, data = event_data
    expected_description = EXPECTED_DATA[event_id]["description"]
    assert data["description"]["text"] == expected_description, f"Event {event_id} description mismatch"

def test_event_start(event_data):
    event_id, data = event_data
    expected_start = EXPECTED_DATA[event_id]["local"]
    assert data["start"]["local"] == expected_start, f"Event {event_id} start time mismatch"

def test_event_capacity(event_data):
    event_id, data = event_data
    expected_capacity = int(EXPECTED_DATA[event_id]["capacity"])
    assert data["capacity"] == expected_capacity, f"Event {event_id} capacity mismatch"
