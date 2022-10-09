def filter_min_green_index(list_object, min_index = 0.1):
    count_territory = 0
    for object in list_object:
        if object.green_index < min_index:
            count_territory += 1
    return count_territory

print(filter_min_green_index(list_territories_class, 10))