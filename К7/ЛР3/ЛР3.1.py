from collections import Counter
reviews = [
    "Очень быстро доставили, сервис отличный",
    "Плохо упаковано, товар поврежден",
    "Отличное качество, быстро и удобно",
    "Долго ждал доставку, сервис плохой"
]
words = " ".join(reviews).lower().split()
counter = Counter(words)
avg = sum(counter.values()) / len(counter)
positive = {"хороший", "отличный", "быстро", "удобно", "понравилось", "вежливый"}
negative = {"плохо", "долго", "дорогой", "поврежден", "ждал", "среднее"}
positive_words = {w: c for w, c in counter.items() if w in positive}
negative_words = {w: c for w, c in counter.items() if w in negative}
marker_words = {w: c for w, c in counter.items() if c > avg}
print("Позитивные слова:", positive_words)
print("Негативные слова:", negative_words)
print("Слова-маркеры:", marker_words)

