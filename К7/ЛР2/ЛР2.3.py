students = ["Ali_2004", "Zuhra_2003", "mansur_2005", "RUSTAM_2004"]
result = []
for student in students:
    name_raw, year_raw = student.split("_")
    name = name_raw.capitalize()
    year = int(year_raw)
    age = 2025 - year
    result.append(f"{name}, возраст: {age}")
print(result)
