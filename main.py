import sys
from stats import get_book_text_count, count_characters, sort_dictionary
if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    num = 0
    word_count = get_book_text_count(f"{sys.argv[1]}")

    for i in word_count:
        num += 1
    
    chars = count_characters(word_count)
    sorted_list = sort_dictionary(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha() == True:
             print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()