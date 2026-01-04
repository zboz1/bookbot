from stats import get_book_text_count, count_characters, sort_dictionary

def main():
    num = 0
    word_count = get_book_text_count("./books/frankenstein.txt")

    for i in word_count:
        num += 1
    
    chars = count_characters(word_count)
    sorted_list = sort_dictionary(chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha() == True:
             print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()