def is_palindrome(model_name):
    clean_name = "".join(model_name.split()).lower()
    return clean_name == clean_name[::-1]
model = "јзиза"
print(f"явл€етс€ ли '{model}' палиндромом?:", is_palindrome(model))
