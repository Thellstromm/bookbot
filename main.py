from stats import print_book_report, number_of_words, character_count, sort_char_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    # Kontrollera att användaren har angett bokväg
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Hämta bokvägen från argumentet
    book_path = sys.argv[1]

    # Läs in boken
    book_text = get_book_text(book_path)

    # Skriv ut hela rapporten
    print_book_report(book_text, book_path)

if __name__ == "__main__":
    main()