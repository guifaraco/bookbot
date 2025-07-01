import sys
from stats import get_chars_dict, count_words, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        path = sys.argv[1] 
        file_contents = get_book_text(path)
        word_count = count_words(file_contents)
        chars_num_dict = get_chars_dict(file_contents)
        sorted_list = chars_dict_to_sorted_list(chars_num_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            if not item["character"].isalpha():
                continue
            print(f"{item['character']}: {item['number']}")
        print("============= END ===============")

if __name__ == "__main__":
    main()
