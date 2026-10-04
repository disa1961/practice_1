def guests_by_seat(seats):
    n = len(seats)
    result = [0] * n

    for i, seat in enumerate(seats):
        guests_number = i + 1
        result[seat -1] = guests_number

    return result
