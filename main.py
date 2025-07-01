def main():
        path = "books/frankenstein.txt"
        file_contents = get_book_text(path)
        word_count = count_words(file_contents)
        chars_num_dict = get_chars_dict(file_contents)
        sorted_list = chars_dict_to_sorted_list(chars_num_dict)

        print(f"--- {path} ---")
        print(f"{word_count} words found in the document")

        for dictionary in sorted_list:
            if not dictionary["character"].isalpha():
                continue
            print(f"The '{dictionary["character"]}' character was found {dictionary["number"]} times")

        print("--- END ---")

def sort_on(dictionary):
    return dictionary["number"]

def chars_dict_to_sorted_list(chars_num_dict):
    sorted_list = []
    for character in chars_num_dict:
        sorted_list.append({"character": character, "number": chars_num_dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars_num_dict = {}
    for character in text.lower():
        if character in chars_num_dict:
            chars_num_dict[character] += 1
        else:
            chars_num_dict[character] = 1
    return chars_num_dict

def count_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()
