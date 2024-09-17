import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, mask",
    [
        ("1234567894561234", "1234 56** **** 1234"),
        ("9876543219876543", "9876 54** **** 6543"),
        ("1472583691472583", "1472 58** **** 2583"),
        ("369258147369", None),
        ("asdjhkjhfaksj", None),
    ],
)
def test_mask_card_number(number, mask):
    assert get_mask_card_number(number) == mask


@pytest.mark.parametrize(
    "number, mask",
    [
        ("12345678945612345678", "**5678"),
        ("32165498765432165498", "**5498"),
        ("98765432165498765432", "**5432"),
        ("ldflklqlwkejlkd", None),
        ("1234567", None),
    ],
)
def test_get_mask_account(number, mask):
    assert get_mask_account(number) == mask


def test_get_mask_account():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
    assert get_mask_card_number("") == None
