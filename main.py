def count_words(file_contents):
    return len(file_contents.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

main()
