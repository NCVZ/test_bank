import datetime


def mask_account_card(info_string):
    """
    Маскирует номер карты или счета в строке.

    Аргумент:
    info_string (str): строка, содержащая тип и номер карты или счета,
    например, "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".

    Возвращает:
    str: строку с замаскированным номером.
    """
    if info_string.startswith("Счет"):
        return mask_account(info_string)
    else:
        return mask_card(info_string)


def mask_card(card_info):
    """
    Маскирует номер карты, оставляя лишь некоторые части видимыми.

    Аргумент:
    card_info (str): строка, содержащая тип карты и номер,
    например, "Visa Platinum 7000792289606361".

    Возвращает:
    str: строку с замаскированным номером карты.
    """
    parts = card_info.split()
    card_type = " ".join(parts[:-1])
    card_number = parts[-1]

    masked_number = card_number[:4] + " " + "**** " * 2 + card_number[-4:]

    return f"{card_type} {masked_number}"


def mask_account(account_info):
    """
    Маскирует номер счета, оставляя лишь последние четыре цифры видимыми.

    Аргумент:
    account_info (str): строка, содержащая тип и номер счета,
    например, "Счет 73654108430135874305".

    Возвращает:
    str: строку с замаскированным номером счета.
    """
    parts = account_info.split()
    account_number = parts[1]

    masked_number = "**** " * 4 + account_number[-4:]

    return f"Счет {masked_number}"


def get_date(date_string):
    """
    Преобразует строку с датой из формата ISO в формат "ДД.ММ.ГГГГ".

    Аргумент:
    date_string (str): строка с датой в формате "YYYY-MM-DDThh:mm:ss.ssssss".

    Возвращает:
    str: строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")


# Примеры
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Maestro 1596837868705199"))  # Maestro 1596 83** **** 5199
print(mask_account_card("Счет 64686473678894779589"))  # Счет **9589
print(mask_account_card("MasterCard 7158300734726758"))  # MasterCard 7158 30** **** 6758
print(mask_account_card("Счет 35383033474447895560"))  # Счет **5560
print(mask_account_card("Visa Classic 6831982476737658"))  # Visa Classic 6831 98** **** 7658
print(mask_account_card("Visa Platinum 8990922113665229"))  # Visa Platinum 8990 92** **** 5229
print(mask_account_card("Visa Gold 5999414228426353"))  # Visa Gold 5999 41** **** 6353
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305
print(get_date("2024-03-11T02:26:18.671407"))
