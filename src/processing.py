def filter_by_state(operations, state='EXECUTED'):
    filter_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filter_operations.append(operation)
    return filter_operations


def sort_by_date(operations, reverse=True):
    sort_operations = sorted(operations, key=lambda x: x["date"], reverse=reverse)
    return sort_operations
