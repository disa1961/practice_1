def multiplication_table(n):
    result = []
    for i in range(1, 11):
        line = f"{n} x {i} = {n * i}"
        result.append(line)
    return result
