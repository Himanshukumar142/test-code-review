def calculate_discount(price, discount):
    return price - (price * discount / 100)
def group_by_first_letter(words):
    grouped = {}

    for word in words:
        first_char = word[0].lower()
        grouped[first_char].append(word)

    return grouped


sample_words = ["Apple", "apricot", "", "Banana", "blueberry"]
print(group_by_first_letter(sample_words))
