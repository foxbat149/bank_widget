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
