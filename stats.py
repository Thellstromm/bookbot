
def number_of_words(text): #counts number of words in text
    word = text.split() # split text into words
    return f"Found {len(word)} total words" # return number of words

def character_count(text): # counts number of characters in text
    count = {}
    for char in text: # iterate through each character in text
        char = char.lower()
        if char in count: # if character is already in dictionary, increment its count
            count[char] += 1
        else:
            count[char] = 1 # if character is not in dictionary, add it with count 1
    return count

def sort_char_counts(counts): # sorts character counts from highest to lowest
    
    # Convert dictionary to list of dictionaries
    list_of_dicts = [{"char": char, "num": num} for char, num in counts.items()]

    # HHelper function for sorting
    def get_count(entry):
        return entry["num"]

    # Sort from highest to lowest
    list_of_dicts.sort(key=get_count, reverse=True)

    return list_of_dicts

def print_book_report(book_text, book_path): # prints report of word and character counts
   
    # Word count
    word_count_report = number_of_words(book_text)

    # Character count
    counts = character_count(book_text)
    sorted_counts = sort_char_counts(counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count_report)
    print("--------- Character Count -------")

    for entry in sorted_counts:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():  # skip all non-alphabetic characters
            print(f"{char}: {num}")

    print("============= END ===============")