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
