# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import the FastAPI app instance from the controller  module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    #Assert that the response JSON matches the expected date
    assert response.json() == {
        # Expected JSON structure
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    sheep_data = {
        "id": 7,
        "name": "Phoebe",
        "breed": "Babydoll",
        "sex": "ewe"
    }

    response = client.post("/sheep", json=sheep_data)
    assert response.status_code == 201

    assert response.json() == sheep_data

    response = client.get("/sheep/7")
    assert response.status_code == 200
    assert response.json() == sheep_data

def test_delete_sheep():
    response = client.delete("/sheep/?id=6")

    assert response.status_code == 200

    assert response.json() == {
        "id": 6,
        "name": "Esther",
        "breed": "Border Leicester",
        "sex": "ewe"
    }

def test_update_sheep():
    sheep_data ={
        "id": 2,
        "name": "Blondie Update",
        "breed": "Polypay",
        "sex": "ram"
    }
    response = client.put("/sheep/2", json=sheep_data)

    assert response.status_code == 200
    assert response.json() == sheep_data

    # Verify if sheep was updated
    response = client.get("/sheep/2")

    assert response.status_code == 200
    assert response.json() == sheep_data

def test_read_all_sheep():
    response = client.get("/sheep/")

    assert response.status_code == 200
    assert len(response.json()) == 6