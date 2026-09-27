from src.processing import filter_by_state, sort_by_date


OPERATIONS = [
    {"id": 1, "state": "EXECUTED", "date": "2025-01-15T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2025-01-20T10:00:00"},
    {"id": 3, "state": "EXECUTED", "date": "2025-01-10T10:00:00"},
]


def test_filter_by_state_default() -> None:
    assert filter_by_state(OPERATIONS) == [OPERATIONS[0], OPERATIONS[2]]


def test_filter_by_state_custom_state() -> None:
    assert filter_by_state(OPERATIONS, "CANCELED") == [OPERATIONS[1]]


def test_sort_by_date_descending() -> None:
    result = sort_by_date(OPERATIONS)
    assert [operation["id"] for operation in result] == [2, 1, 3]


def test_sort_by_date_ascending() -> None:
    result = sort_by_date(OPERATIONS, descending=False)
    assert [operation["id"] for operation in result] == [3, 1, 2]


def test_filter_by_state_does_not_change_input() -> None:
    original = OPERATIONS.copy()
    filter_by_state(OPERATIONS)
    assert OPERATIONS == original


def test_sort_by_date_does_not_change_input() -> None:
    original = OPERATIONS.copy()
    sort_by_date(OPERATIONS)
    assert OPERATIONS == original
