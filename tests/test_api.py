from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_prediction():
    file_path = Path("tests/images/cat.jpeg")
    with open(file_path, "rb") as f:
        filebody = f.read()
    response = client.post("/predict", files={"image": (file_path.name, filebody)})
    assert response.status_code == 200
    assert response.json() == {"response": "Persian cat"}


@pytest.mark.xfail()
def test_empty_file():
    file_path = Path("tests/images/empty_file.jpeg")
    with open(file_path, "rb") as f:
        filebody = f.read()
    response = client.post("/predict", files={"image": (file_path.name, filebody)})


@pytest.mark.skip(reason="Todo")
def test_non_square_image():
    pass


@pytest.mark.skip(reason="Todo")
def test_image_too_small():
    pass


@pytest.mark.skip(reason="Todo")
def test_image_too_large():
    pass
