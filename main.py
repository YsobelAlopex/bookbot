import sys
def get_book_text(book):
    with open(book) as f:
        return f.read()
    
from stats import count_words
from stats import count_characters
from stats import list_dicts
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    dict_list = list_dicts(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in dict_list:
        if i["character"].isalpha():
            print(i["character"]+":", i["num"])
    print("============= END ===============")
    return
    
main()