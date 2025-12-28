data = [
    ("Model X", 250),
    ("Model S", 320),
    ("Model A", 180),
    ("Model B", 250)
]
by_speed = sorted(data, key=lambda x: x[1])
by_model = sorted(data, key=lambda x: x[0])
print("По скорости:", by_speed)
print("По модели:", by_model)
