from typing import Any


def get_mask_card_number(card_number: Any) -> Any:
    """Функция которая принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) >= 16:
        return f'{card_number[-16:-12]} {card_number[-12:-10]}{"**"} {"****"} {card_number[-4:]}'
    else:
        return None


def get_mask_account(account_number: Any) -> Any:
    """Функция которая принимает на вход номер счета и возвращает его маску"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"{"**"}{account_number[-4:]}"
    else:
        return None

