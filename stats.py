def get_total_words(content):
    total_words = len(content.split())

    return total_words

def get_total_characters(content):
    total_chars = {}

    for char in content:
        char = char.lower()

        if char in total_chars:
            total_chars[char] = total_chars[char] + 1
        else:
            total_chars[char] = 1

    return total_chars

def get_total_characters_sorted(content_dict):
    array_of_characters = []

    for item in content_dict:
        dict_of_characters = {}

        if not item.isalpha():
            continue

        dict_of_characters["name"] = item
        dict_of_characters["num"] = content_dict[item]

        array_of_characters.append(dict_of_characters)
    
    def sort_item(item):
        return item["num"]

    array_of_characters.sort(reverse=True, key=sort_item)

    return array_of_characters
