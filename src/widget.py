from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """Функция которая обрабатывает информацию как о картах, так и о счетах"""

    account = bank_info.split()
    number = account[-1]

    if len(number) == 16:
        account[-1] = get_mask_card_number(number)
    else:
        account[-1] = get_mask_account(number)

    return " ".join(account)


def get_date(user_date: str) -> str:
    """Функция для форматирования даты"""

    formatted_date = user_date.split("-")

    return f"{formatted_date[2][:2]}.{formatted_date[1]}.{formatted_date[0]}"
