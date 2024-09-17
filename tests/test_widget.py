import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "nums, masks",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_widget_mask_account_card(nums, masks):
    """Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки
    в зависимости от типа входных данных (карта или счет)."""
    assert mask_account_card(nums) == masks


@pytest.mark.parametrize(
    "new_date, rev_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-05-11T02:26:18.671407", "11.05.2024"),
        ("asd1234568987", None),
    ],
)
def test_get_date(new_date, rev_date):
    """Тестирование правильности преобразования даты"""
    assert get_date(new_date) == rev_date
