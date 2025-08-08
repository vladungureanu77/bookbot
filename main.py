from stats import count_words, count_characters, sort_chars
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_counts = count_characters(text)
    #print(char_counts)
    Sort_char = sort_chars(char_counts)
    print("--------- Character Count -------")
    for item in Sort_char:
        print(f"{item['char']}: {item['num']}")

main()