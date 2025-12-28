def find_speed(data_list, target_model):
    for model, speed in data_list:
        if model == target_model:
            return speed
    return "Модель не найдена"
current_data = [("Tesla", 250), ("BMW", 240), ("Audi", 260)]
search_model = "BMW"
print(f"Скорость {search_model}:", find_speed(current_data, search_model))
