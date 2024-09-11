def filter_by_state(list_of_dict, state_id = 'EXECUTED'):
    """Функция которая принимает на вход список словарей и выводит список по ключу"""
    new_list = []
    for i in list_of_dict:
        if i['state'] == state_id:
            new_list.append(i)
    return new_list

def sort_by_date(list_of_dict, reverse = True):
    """Функция которая возвращает новый список, отсортированный по дате"""
    new_sort_list = sorted(list_of_dict, key=lambda new_dict: new_dict['date'], reverse=reverse)
    return new_sort_list

print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))