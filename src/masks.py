def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    card_number_str = str(card_number)
    masked_card_number = "{} {}** **** {}".format(card_number_str[:4], card_number_str[4:6], card_number_str[-4:])
    return masked_card_number


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    account_number_str = str(account_number)
    masked_account_number = "**{}".format(account_number_str[-4:])
    return masked_account_number


card_number = 7000792289606361
print(get_mask_card_number(card_number))  # 7000 79** **** 6361

account_number = 73654108430135874305
print(get_mask_account(account_number))  # **4305
