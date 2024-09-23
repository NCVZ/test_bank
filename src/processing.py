def filter_by_state(lst, state="EXECUTED"):
    """
    Функция фильтрует список словарей по заданному значению ключа 'state'.

    Аргументы:
    lst -- список словарей, каждый из которых может содержать ключ 'state'
    state -- значение состояния для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    Новый список словарей, содержащий только те элементы,
    у которых значение по ключу 'state' соответствует указанному.
    """
    return [item for item in lst if item.get("state") == state]


def sort_by_date(lst, reverse=True):
    """
    Функция сортирует список словарей по значению ключа 'date'.

    Аргументы:
    lst -- список словарей, каждый из которых содержит ключ 'date' в формате строки
    reverse -- определяет порядок сортировки:
               True для сортировки по убыванию (по умолчанию),
               False для сортировки по возрастанию

    Возвращает:
    Новый список словарей, отсортированный по значению ключа 'date'.
    """
    return sorted(lst, key=lambda x: x.get("date"), reverse=reverse)


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтрация по состоянию 'EXECUTED'
executed_transactions = filter_by_state(data)
print("Отфильтрованные операции (state='EXECUTED'):")
print(executed_transactions)
print()

# Сортировка отфильтрованных операций по дате
sorted_transactions = sort_by_date(executed_transactions)
print("Отсортированные операции по дате:")
print(sorted_transactions)
