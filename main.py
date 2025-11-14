from stats import print_book_report, number_of_words, character_count, sort_char_counts
import sys

def get_book_text(file_path): # get books file to a string
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    # controlls command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get book path from argument
    book_path = sys.argv[1]

    # Read the book
    book_text = get_book_text(book_path)

    # Print the full report
    print_book_report(book_text, book_path)

if __name__ == "__main__":
    main()