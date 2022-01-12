from fastapi import responses
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all():
    response = client.get("/law")
    print(response.json())
    assert response.status_code == 200


# def test_create_firm():
#     response = client.post("/law", json = {"Law_Firm_Name":"str", "Law_Firm_Email_Address":"firm@gmail.com", "Load_Range":"10000", "Legal_Fee":"200", "Law_Firm_Priority":"str", "Remarks":"str","Law_Firm_Status":"Active",
#     "Display_Hierarchy": "5"})
#     print(response.json())
#     assert response.status_code == 201


def test_delete_firm():
    response = client.post("/law")
    print(response.json())

    response = client.delete(f"/law/4/")
    assert response.status_code == 200
