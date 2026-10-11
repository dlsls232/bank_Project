import json
from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_success():
    """Проверяет чтение списка словарей из JSON."""
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    mocked_file = mock_open(read_data=json.dumps(data))

    with patch("builtins.open", mocked_file):
        result = read_json_file("operations.json")

    assert result == data


def test_read_json_file_empty():
    """Проверяет пустой JSON-файл."""
    mocked_file = mock_open(read_data="")

    with patch("builtins.open", mocked_file):
        result = read_json_file("operations.json")

    assert result == []


def test_read_json_file_not_list():
    """Проверяет JSON, содержащий не список."""
    mocked_file = mock_open(read_data='{"id": 1}')

    with patch("builtins.open", mocked_file):
        result = read_json_file("operations.json")

    assert result == []


def test_read_json_file_not_found():
    """Проверяет ситуацию, когда файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("missing.json")

    assert result == []
