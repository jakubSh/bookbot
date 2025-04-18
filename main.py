from stats import word_count, char_count, sorting, dict_to_list

def get_book_text(path):
    with open(path, encoding="latin-1") as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    num_chars = char_count(book_text)
    sorted_chars = dict_to_list(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")

main()
