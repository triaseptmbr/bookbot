from stats import get_total_words

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()

        return file_contents

def main():
    content_path = "books/frankenstein.txt"
    num_words = get_total_words(get_book_text(content_path).replace('\n', ' '))

    print(f"Found {num_words} total words")

main()
