from typing import Any


def filter_by_state(list_of_dict: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция которая принимает на вход список словарей и выводит список по ключу"""
    new_list = []
    for i in list_of_dict:
        if i["state"] == state_id:
            new_list.append(i)
    return new_list


def sort_by_date(list_of_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция которая возвращает новый список, отсортированный по дате"""
    new_sort_list = sorted(list_of_dict, key=lambda new_dict: new_dict["date"], reverse=reverse)
    return new_sort_list
