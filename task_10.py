def index_of_min(values):
    if not values:
        return -1

    min_value = min(values)
    return values.index(min_value)
