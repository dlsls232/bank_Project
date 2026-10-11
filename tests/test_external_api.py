from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rub


def test_convert_rub():
    """Проверяет возврат суммы в рублях без запроса к API."""
    transaction = {
        "operationAmount": {
            "amount": "1500.50",
            "currency": {"code": "RUB", "name": "руб."},
        }
    }

    with patch("src.external_api.requests.get") as mock_get:
        result = convert_to_rub(transaction)

    assert result == 1500.50
    mock_get.assert_not_called()


def test_convert_usd_to_rub():
    """Проверяет конвертацию долларов в рубли."""
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD", "name": "USD"},
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}

    with (
        patch("src.external_api.API_KEY", "test_key"),
        patch(
            "src.external_api.requests.get",
            return_value=mock_response,
        ) as mock_get,
    ):
        result = convert_to_rub(transaction)

    assert result == 9000.0
    mock_get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()


def test_convert_eur_to_rub():
    """Проверяет конвертацию евро в рубли."""
    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {"code": "EUR", "name": "EUR"},
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {"result": 5000.0}

    with (
        patch("src.external_api.API_KEY", "test_key"),
        patch(
            "src.external_api.requests.get",
            return_value=mock_response,
        ),
    ):
        result = convert_to_rub(transaction)

    assert result == 5000.0


def test_unsupported_currency():
    """Проверяет ошибку для неподдерживаемой валюты."""
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "GBP", "name": "GBP"},
        }
    }

    with pytest.raises(ValueError, match="Unsupported currency"):
        convert_to_rub(transaction)


def test_missing_api_key():
    """Проверяет ошибку при отсутствии API-ключа."""
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD", "name": "USD"},
        }
    }

    with patch("src.external_api.API_KEY", None):
        with pytest.raises(ValueError, match="API key is missing"):
            convert_to_rub(transaction)
