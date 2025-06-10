from stats import count_words
from stats import character_count
from stats import sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    
    total_words = count_words(file_contents)
    characters, sorted_list = character_count(file_contents)
    
    return(total_words, characters, sorted_list)


def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath=sys.argv[1]
    
    word_count, character_count, sorted_list = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()