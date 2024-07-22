def main():
    book_path = "books/frankenstein.txt"
    b_text = get_book_text(book_path)
    num_w_in_b_text = get_num_words(b_text)
    num_c_in_b_text = get_num_char(b_text)
    char_list = char_dict_to_list(num_c_in_b_text)

    print(f"=== Begin Character and Word Report of {book_path} ===")
    print()

    print(f"Number of words found in doc: {num_w_in_b_text}")
    print()

    for setto in char_list:
        if not setto["char"].isalpha():
            continue
        print(f"Character '{setto['char']}' was found #{setto['num']} times")

    print(f"=== End ===")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_char(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict 

def char_dict_to_list(dict):
    list = []
    for ch in dict:
        list.append({"char": ch, "num": dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(dict):
    return dict["num"]

main()
