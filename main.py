from stats import get_book_text_count, count_characters

def main():
    num = 0
    word_count = get_book_text_count("./books/frankenstein.txt")

    for i in word_count:
        num += 1
    
    chars = count_characters(word_count)
    
    print(f"Found {num} total words")
    print(f"{chars}")

main()