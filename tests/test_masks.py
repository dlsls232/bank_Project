from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    """Проверяет маскировку номера карты."""
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_get_mask_account():
    """Проверяет маскировку номера счёта."""
    assert get_mask_account("1234567890123456") == "**3456"
