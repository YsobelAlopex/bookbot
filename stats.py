def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    low_text = text.lower()
    for character in low_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def list_dicts(char_count):
    list = []
    for char in char_count:
        list.append({"character": char, "num": char_count[char]})
    def sort_on(list):
        return list["num"]
    list.sort(reverse=True, key=sort_on)
    return list



