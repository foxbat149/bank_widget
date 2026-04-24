def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрации операций"""
    filter_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filter_operations.append(operation)
    return filter_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки операций по дате"""
    sort_operations = sorted(operations, key=lambda x: x["date"], reverse=reverse)
    return sort_operations
