def main():
        path = "books/frankenstein.txt"
        file_contents = get_book_text(path)
        print(count_words(file_contents))

def count_words(file_contents):
    return len(file_contents.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
