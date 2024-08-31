from typing import Any


def get_mask_card_number(card_number: Any) -> Any:
    """Функция которая принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) == 30 or 27 or 29 or 26 or 24:
        return (
            f"{card_number[:-16]}{card_number[-16:-12]} {card_number[-12:-10] + "**"} "
            f"{len(card_number[-10:-6]) * "*"} {card_number[-4:30]}"
        )
    else:
        return None


card_number = input()
