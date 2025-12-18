from stats import get_num_words, get_num_chars, print_default_report
import sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()

    return content 

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)    
    num_chars = get_num_chars(text)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')

    for item in print_default_report(num_chars):
        if item['char'].isalpha():
            print(f'{item['char']}: {item['num']}') 


main()
