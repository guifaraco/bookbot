def main():
        path = "books/frankenstein.txt"
        file_contents = get_book_text(path)
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        print(f"The number of words in the book is {word_count}")
        print(f"The count of characters is {character_count}")


def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def count_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
