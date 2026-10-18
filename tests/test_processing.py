from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations: list[dict[str, Any]]) -> None:
    result = filter_by_state(operations)
    assert [operation["id"] for operation in result] == [1, 3]


@pytest.mark.parametrize(
    ("state", "expected_ids"),
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state_by_state(
    operations: list[dict[str, Any]], state: str, expected_ids: list[int]
) -> None:
    result = filter_by_state(operations, state)
    assert [operation["id"] for operation in result] == expected_ids


def test_filter_by_state_ignores_operation_without_state() -> None:
    operations = [{"id": 1, "date": "2025-01-01T00:00:00"}]
    assert filter_by_state(operations) == []


def test_filter_by_state_does_not_change_input(
    operations: list[dict[str, Any]],
) -> None:
    original = [operation.copy() for operation in operations]
    filter_by_state(operations)
    assert operations == original


def test_sort_by_date_descending(operations: list[dict[str, Any]]) -> None:
    result = sort_by_date(operations)
    assert [operation["id"] for operation in result] == [2, 1, 4, 3]


def test_sort_by_date_ascending(operations: list[dict[str, Any]]) -> None:
    result = sort_by_date(operations, descending=False)
    assert [operation["id"] for operation in result] == [3, 1, 4, 2]


def test_sort_by_date_equal_dates_is_stable(
    operations: list[dict[str, Any]],
) -> None:
    result = sort_by_date(operations, descending=False)
    same_date_ids = [
        operation["id"]
        for operation in result
        if operation["date"] == "2025-01-15T10:00:00"
    ]
    assert same_date_ids == [1, 4]


def test_sort_by_date_uses_empty_date_for_missing_value() -> None:
    operations = [
        {"id": 1, "date": "2025-01-01T00:00:00"},
        {"id": 2},
    ]
    result = sort_by_date(operations, descending=True)
    assert [operation["id"] for operation in result] == [1, 2]


def test_sort_by_date_does_not_change_input(
    operations: list[dict[str, Any]],
) -> None:
    original = [operation.copy() for operation in operations]
    sort_by_date(operations)
    assert operations == original
