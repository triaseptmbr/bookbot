from stats import get_total_words
from stats import get_total_characters
from stats import get_total_characters_sorted

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read().replace('\n', ' ')

        return file_contents

def main():
    content_path = "books/frankenstein.txt"
    num_words = get_total_words(get_book_text(content_path))
    num_characters = get_total_characters(get_book_text(content_path))
    sorted_characters = get_total_characters_sorted(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzingbook found at {content_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for character in sorted_characters:
        print(f"{character["name"]}: {character["num"]}")

    print("============= END ===============")

main()
