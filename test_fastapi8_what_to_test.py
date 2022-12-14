from fastapi.testclient import TestClient

from fastapi8_what_to_test import app

client = TestClient(app)


def test_read_item():

    # Send the Query-Variable 'x_token'=coneofsilence and Path-Variable 'item_id'=foo
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


def test_read_item_bad_token():
    # Send the Query-Variable 'x_token'=hailhydra and Path-Variable 'item_id'=foo
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_read_inexistent_item():
    # Send the Query-Variable 'x_token'=coneofsilence and Path-Variable 'item_id'=baz
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_create_item():
    # Send the Body-Variable 'item: Item' and Query-Variable 'x_token'=coneofsilence
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_bad_token():
    # Send the Body-Variable 'item: Item' and Query-Variable 'x_token'=hailhydra
    response = client.post(
        "/items/",
        headers={"X-Token": "hailhydra"},
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_create_existing_item():
    # Send the Body-Variable 'item: Item' and Query-Variable 'x_token'=coneofsilence
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}
