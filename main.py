import sys
from stats import get_num_words
from stats import get_num_char_count
from stats import sort_char_list

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char_count = get_num_char_count(text)
    sorted_char_list = sort_char_list(num_char_count)
    print_report(book_path, num_words, sorted_char_list)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path, num_words, sorted_char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        c = i["char"]
        n = i["num"]
        if c.isalpha():
            print(f"{c}: {n} ")
    print("============= END ===============")

main()
