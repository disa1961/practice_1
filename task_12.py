def shortest_distance(kilometers, meters):
    km_in_meters = kilometers * 1000
    if km_in_meters < meters:
        return km_in_meters
    else:
        return meters
