import sys

from stats import get_num_words, get_char_freq, get_sorted

def get_book_text(f):
    # Converts the contents of the book into one string of text
    return f.read()

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit the program with an error code
    user_input = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {user_input}...")
    try:
        # To open the file
        with open(user_input) as f:
            text = get_book_text(f)
            word_count = get_num_words(text)
            char_dict = get_char_freq(text)
            # pass the dictionary containing character and frequency to sort
            sorted_chars = get_sorted(char_dict)
            print("----------- Word Count ----------")
            print(f"Found {word_count} total words")
            print("--------- Character Count -------")
            # To filter the dictionary to get only the count of alphabets
            for item in sorted_chars:
                if item["char"].isalpha():
                    print(f"{item['char']}: {item['num']}")
            print("============= END ===============")
            print(sys.argv)
    except FileNotFoundError:
        print("Error")
main()