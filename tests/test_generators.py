import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions():
    return [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод от Иван Иванов",
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Оплата покупки",
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
    ]


def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(
        item["operationAmount"]["currency"]["code"] == "USD"
        for item in result
    )


def test_filter_by_currency_rub(transactions):
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 1


def test_filter_by_currency_no_matches(transactions):
    assert list(filter_by_currency(transactions, "EUR")) == []


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод от Иван Иванов",
        "Оплата покупки",
        "Перевод организации",
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    ("start", "end", "expected"),
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (0, 0, ["0000 0000 0000 0000"]),
        (
            1234567890123456,
            1234567890123456,
            [
                "1234 5678 9012 3456",
            ],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


def test_card_number_generator_empty_range():
    assert list(card_number_generator(5, 3)) == []
