def get_mean_green_index(list_object):
    sum_index_green = 0
    for object in list_object:
      sum_index_green += object.green_index
    avg_index_green = sum_index_green / len(list_object)
    return avg_index_green


print(get_mean_green_index(list_territories_class))