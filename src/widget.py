from typing import Any

from src.masks import get_mask_card_number


def mask_account_card(new_mask_number: Any) -> Any:
    """Функция которая возвращает маску и номер карты/счета"""
    if "Счет" in new_mask_number:
        return f"{new_mask_number[:5]}{'**' + new_mask_number[-4:]}"
    else:
        return get_mask_card_number(new_mask_number)


def get_date(new_date: Any) -> Any:
    """Функция которая возвращает дату"""
    return f"{new_date[8:10]}.{new_date[5:7]}.{new_date[:4]}"
