from unittest.mock import patch

from src.main import (
    filter_operations_by_description,
    filter_ruble_operations,
    get_operations_by_status,
    load_transactions,
    sort_operations_by_date,
)


def test_load_transactions_invalid_type() -> None:
    """Проверяет обработку неправильного типа файла."""
    assert load_transactions("4") == []


def test_get_operations_by_status() -> None:
    """Проверяет фильтрацию операций по статусу."""
    operations = [
        {"state": "EXECUTED", "amount": 100},
        {"state": "CANCELED", "amount": 200},
        {"state": "EXECUTED", "amount": 300},
    ]

    with patch("builtins.input", return_value="executed"):
        result = get_operations_by_status(operations)

    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_get_operations_by_status_invalid_then_valid() -> None:
    """Проверяет повторный ввод при неправильном статусе."""
    operations = [{"state": "PENDING"}]

    with patch("builtins.input", side_effect=["wrong", "pending"]):
        result = get_operations_by_status(operations)

    assert result == operations


def test_sort_operations_by_date_ascending() -> None:
    """Проверяет сортировку по возрастанию даты."""
    operations = [
        {"date": "2023-02-01"},
        {"date": "2021-01-01"},
        {"date": "2022-01-01"},
    ]

    with patch("builtins.input", side_effect=["да", "1"]):
        result = sort_operations_by_date(operations)

    assert [item["date"] for item in result] == [
        "2021-01-01",
        "2022-01-01",
        "2023-02-01",
    ]


def test_sort_operations_by_date_descending() -> None:
    """Проверяет сортировку по убыванию даты."""
    operations = [
        {"date": "2021-01-01"},
        {"date": "2023-01-01"},
    ]

    with patch("builtins.input", side_effect=["да", "2"]):
        result = sort_operations_by_date(operations)

    assert [item["date"] for item in result] == [
        "2023-01-01",
        "2021-01-01",
    ]


def test_sort_operations_by_date_without_sorting() -> None:
    """Проверяет отказ от сортировки."""
    operations = [{"date": "2022-01-01"}, {"date": "2021-01-01"}]

    with patch("builtins.input", return_value="нет"):
        result = sort_operations_by_date(operations)

    assert result == operations


def test_filter_ruble_operations() -> None:
    """Проверяет фильтрацию операций в рублях."""
    operations = [
        {"currency_code": "RUB"},
        {"currency_code": "USD"},
        {"currency_code": "rub"},
    ]

    with patch("builtins.input", return_value="да"):
        result = filter_ruble_operations(operations)

    assert result == [
        {"currency_code": "RUB"},
        {"currency_code": "rub"},
    ]


def test_filter_ruble_operations_without_filtering() -> None:
    """Проверяет отказ от фильтрации по валюте."""
    operations = [{"currency_code": "USD"}]

    with patch("builtins.input", return_value="нет"):
        result = filter_ruble_operations(operations)

    assert result == operations


def test_filter_operations_by_description() -> None:
    """Проверяет поиск по описанию операции."""
    operations = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
    ]

    with patch("builtins.input", side_effect=["да", "перевод"]):
        result = filter_operations_by_description(operations)

    assert result == [{"description": "Перевод организации"}]


def test_filter_operations_by_description_without_filtering() -> None:
    """Проверяет отказ от поиска по описанию."""
    operations = [{"description": "Оплата услуг"}]

    with patch("builtins.input", return_value="нет"):
        result = filter_operations_by_description(operations)

    assert result == operations


def test_filter_operations_by_description_empty_search() -> None:
    """Проверяет пустой поисковый запрос."""
    operations = [{"description": "Оплата услуг"}]

    with patch("builtins.input", side_effect=["да", ""]):
        result = filter_operations_by_description(operations)

    assert result == operations
