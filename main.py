import sys
from stats import get_word_count, get_character_count_dic, sort_character_count_dic

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars_dic = get_character_count_dic(text)
    sorted_num_chars_list = sort_character_count_dic(num_chars_dic)
    for num_char_dic in sorted_num_chars_list:
        if num_char_dic['char'].isalpha():
            print(f"{num_char_dic['char']}: {num_char_dic['num']}")

    print("============= END ===============")

main()