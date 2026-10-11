from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Проверяет маскировку номера карты."""
    result = mask_account_card("Visa 1234567890123456")

    assert result == "Visa 1234 56** **** 3456"


def test_mask_account():
    """Проверяет маскировку банковского счёта."""
    result = mask_account_card("Счет 1234567890123456")

    assert result == "Счет **3456"


def test_get_date():
    """Проверяет преобразование даты."""
    result = get_date("2024-03-11T02:26:18.671407")

    assert result == "11.03.2024"
