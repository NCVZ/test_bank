from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по ключу state.

    :param transactions: Список словарей с транзакциями.
    :param state: Состояние транзакции для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список транзакций.
    """
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате.

    :param transactions: Список словарей с транзакциями.
    :param ascending: Порядок сортировки (по умолчанию True - по возрастанию).
    :return: Отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x.get("date"), reverse=not ascending)
